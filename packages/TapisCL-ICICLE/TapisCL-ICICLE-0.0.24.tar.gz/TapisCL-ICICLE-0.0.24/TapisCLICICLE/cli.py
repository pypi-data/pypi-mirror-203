#!/usr/bin/python3

import socket
import argparse
from argparse import SUPPRESS
import sys
import pyfiglet
from getpass import getpass
import os
import time
from pprint import pprint
import json

try:
    from . import schemas
    from . import socketOpts as SO
    from . import helpers
    from . import decorators
    from . import args
except:
    import schemas
    import socketOpts as SO
    import helpers
    import decorators
    import args


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
server_path = os.path.join(__location__, 'server.py')


class CLI(SO.SocketOpts, helpers.OperationsHelper, decorators.DecoratorSetup, helpers.Formatters):
    def __init__(self, IP: str, PORT: int):
        self.ip, self.port = IP, PORT
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        # sets up connection with the server
        self.username, self.url = self.connect()

        # set up argparse
        self.parser = argparse.ArgumentParser(description="Command Line Argument Parser", exit_on_error=False, usage=SUPPRESS)
        self.parser.add_argument('command_group')

        for parameters in args.Args.argparser_args.values():
            self.parser.add_argument(*parameters["args"], **parameters["kwargs"])

    def initialize_server(self): 
        """
        detect client operating system. The local server intitialization is different between unix and windows based systems
        """
        if 'win' in sys.platform:
            os.system(f"pythonw {server_path}")
        else: # unix based
            os.system(f"python {server_path} &")

    @decorators.AnimatedLoading
    def connection_initialization(self): # patience. This sometimes takes a while
        """
        start the local server through the client
        """
        startup_flag = False # flag to tell code not to run multiple server setup threads at once
        timeout_time = time.time() + 30 # server setup timeout. If expires, there is a problem!
        while True:
            if time.time() > timeout_time: # connection timeout condition
                sys.stdout.write("\r[-] Connection timeout")
                os._exit(0)
            try:
                self.connection.connect((self.ip, self.port)) # try to establish a connection
                if startup_flag:
                    startup.kill()
                break
            except Exception as e:
                if not startup_flag:
                    startup = helpers.KillableThread(target=self.initialize_server) # run the server setup on a separate thread
                    startup.start() 
                    startup_flag = True # set the flag to true so the thread runs only once
                    continue

    def connect(self):
        """
        connect to the local server
        """
        self.connection_initialization() # connect to the server
        #self.connection.connect((self.ip, self.port)) # enable me for debugging. Requires manual server start
        connection_info: schemas.StartupData = self.schema_unpack() # receive info from the server whether it is a first time connection
        if connection_info.initial: # if the server is receiving its first connection for the session\
            while True:
                try:
                    url = str(input("\nEnter the link for the tapis service you are connecting to: ")).strip()
                except KeyboardInterrupt:
                    url = " "
                    pass
                url_data = schemas.StartupData(url=url)
                self.json_send(url_data.dict())
                auth_request: schemas.AuthRequest = self.schema_unpack()
                try:
                    username = str(input("\nUsername: ")).strip() # take the username
                    password = getpass("Password: ").strip() # take the password
                except KeyboardInterrupt:
                    username, password = " ", " "
                    pass
                auth_data = schemas.AuthData(username = username, password = password)
                self.json_send(auth_data.dict()) # send the username and password to the server to be used

                verification: schemas.ResponseData | schemas.StartupData = self.schema_unpack() # server responds saying if the verification succeeded or not
                if verification.schema_type == 'StartupData': # verification success, program moves forward
                    return verification.username, verification.url
                else: # verification failed. User has 3 tries, afterwards the program will shut down
                    print(f"[-] verification failure, attempt # {verification.response_message[1]}")
                    if verification.response_message[1] == 3:
                        sys.exit(0)
                    continue

        print(f"[+] Connected to the Tapis service at {connection_info.url}")
        return connection_info.username, connection_info.url # return the username and url

    def process_command(self, command: str) -> list[str]: 
        """
        split the command string into a list. Not sure why this was even made
        """
        command = command.strip().split(' ') 
        return command

    def expression_input(self) -> str: # for subclients. Pods and apps running through Tapis will have their own inputs. This gives user an interface
        print("Enter 'exit' to submit") # user must enter exit to submit their input
        expression = ''
        line = ''
        while line != 'exit': # handles multiple lines of input. Good for neo4j expressions
            line = str(input("> "))
            expression += line
        return expression

    def fillout_form(self, form: list) -> dict:
        filled_form = dict()
        for field in form:
            value = str(input(f"{field}: "))
            filled_form.update({field:value})
        return filled_form

    def command_operator(self, kwargs: dict | list, exit_: int=0): # parses command input
        if isinstance(kwargs, list): # check if the command input is from the CLI, or direct input
            kwargs = vars(self.parser.parse_args(kwargs)) # parse the arguments
        if not kwargs['command_group']:
            return False
        command = schemas.CommandData(kwargs = kwargs, exit_status = exit_)
        return command
    
    def special_forms_ops(self):
        while True:
            response = self.schema_unpack()
            if response.schema_type == 'FormRequest' and not response.arguments_list:
                form = self.expression_input()
                filled_form = schemas.FormResponse(arguments_list=form)
            elif response.schema_type == 'FormRequest':
                form = self.fillout_form(response.arguments_list)
                filled_form = schemas.FormResponse(arguments_list=form)
            elif response.schema_type == 'AuthRequest':
                if not response.secure_input:
                    username = input("Username: ")
                    password = getpass("Password: ")
                else:
                    username = None
                    password = getpass("Password: ")
                filled_form = schemas.AuthData(username=username, password=password)
            elif response.schema_type == "ConfirmationRequest":
                print(response.message)
                while True:
                    decision = str(input("(y/n)"))
                    if decision == 'y':
                        decision = True
                        break
                    elif decision == 'n':
                        decision = False
                        break
                    else:
                        print("Enter valid response")
                filled_form = schemas.ResponseData(response_message=decision)
            else:
                return response
            self.json_send(filled_form.dict())

    def print_response(self, response_message):
        if type(response_message) == dict:
            self.recursive_dict_print(response_message)
        elif (type(response_message) == list or 
             type(response_message) == tuple or 
             type(response_message) == set):
            for value in response_message:
                print(value)
        else:
            print(response_message)

    def main(self):
        if len(sys.argv) > 1: # checks if any command line arguments were provided. Does not open CLI
            try:
                kwargs = self.parser.parse_args()
            except:
                print("Invalid Arguments")
                os._exit(0)
            kwargs = vars(kwargs)
            command = self.command_operator(kwargs, exit_=1) # operate with args, send them over
            self.json_send(command.dict())
            response = self.special_forms_ops()
            if response.schema_type == 'ResponseData':
                self.print_response(response.response_message)
            os._exit(0)

        title = pyfiglet.figlet_format("---------\nTapiconsole\n---------", font="slant") # print the title when CLI is accessed
        print(title)
        
        while True: # open the CLI if no arguments provided on startup
            try:
                time.sleep(0.01)
                kwargs = self.process_command(str(input(f"[{self.username}@{self.url}] "))) # ask for and process user input
                try:
                    command = self.command_operator(kwargs) # run operations
                except:
                    continue
                if not command:
                    continue
                self.json_send(command.dict())
                response = self.special_forms_ops()
                if response.schema_type == 'ResponseData' and response.exit_status: # if the command was a shutdown or exit, close the program
                    self.print_response(response.response_message)
                    os._exit(0)
                elif response.schema_type == 'ResponseData':
                    self.print_response(response.response_message)
            except KeyboardInterrupt:
                pass # keyboard interrupts mess with the server, dont do it! it wont work anyway, hahahaha
            except WindowsError: # if connection error with the server (there wont be any connection errors)
                print("[-] Connection was dropped. Exiting")
                os._exit(0)
            except Exception as e: # if something else happens
                print(e)


if __name__ == "__main__":
    client = CLI(socket.gethostbyname(socket.gethostname()), 30000)
    client.main()