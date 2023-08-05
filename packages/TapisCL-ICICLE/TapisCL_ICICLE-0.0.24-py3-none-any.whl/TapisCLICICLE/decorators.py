import typing
import socket
import sys
import time
from functools import update_wrapper, partial
try:
    from . import helpers
    from . import schemas
    from . import socketOpts
    from . import exceptions
except:
    import helpers
    import schemas
    import socketOpts
    import exceptions


class BaseRequirementDecorator(socketOpts.SocketOpts, helpers.OperationsHelper):
    connection: typing.Optional[socket.socket] = None
    username: typing.Optional[str] = None
    password: typing.Optional[str] = None
    def __init__(self, func: typing.Callable):
        update_wrapper(self, func)
        self.function = func
        self.__code__ = func.__code__
        self.__doc__ = func.__doc__
        self.__name__ = func.__name__
    
    def __get__(self, obj, objtype): 
        """Support instance methods."""
        part = partial(self.__call__, obj)
        part.__code__ = self.__code__
        part.__doc__ = self.__doc__
        part.__name__ = self.__name__
        return part
    
    def __repr__(self):
        return str(self.function)
    
    def __str__(self):
        return str(self.function)


class RequiresForm(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        fields = list(helpers.get_parameters(self.function))
        for key, value in kwargs.items():
            if value or value == False:
                fields.remove(key)
        if not fields:
            raise AttributeError(f"The decorated function {self.function} has no parameters.")
        form_request = schemas.FormRequest(arguments_list=fields)
        self.json_send_explicit(BaseRequirementDecorator.connection, form_request.dict())
        filled_form: schemas.FormResponse = self.schema_unpack_explicit(self.connection).arguments_list
        for key, value in filled_form.items():
            kwargs[key] = value

        return self.function(obj, **kwargs)


class RequiresExpression(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        fields = list(helpers.get_parameters(self.function))
        if 'expression' not in fields:
            raise AttributeError(f"The function {self.function} does not contain an 'expression' parameter")
        form_request = schemas.FormRequest(arguments_list=[])
        self.json_send_explicit(BaseRequirementDecorator.connection, form_request.dict())
        filled_form: schemas.FormResponse = self.schema_unpack()
        kwargs['expression'] = filled_form.arguments_list

        return self.function(obj, **kwargs)
    

class SecureInput(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        fields = list(helpers.get_parameters(self.function))
        if 'password' in fields:
            secure_input_request = schemas.AuthRequest(secure_input=True)
            self.json_send_explicit(BaseRequirementDecorator.connection, secure_input_request.dict())
            secure_input_data: schemas.AuthData = self.schema_unpack_explicit(self.connection)
            kwargs['password'] = secure_input_data.password
            return self.function(obj, **kwargs)
        raise AttributeError(f"The function {self.function} does not contain a 'password' parameter")


class Auth(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        if self.function.__name__ == 'tapis_init' and kwargs['username'] and kwargs['password']:
            return self.function(obj, **kwargs)
        fields = list(helpers.get_parameters(self.function))
        auth_request = schemas.AuthRequest()
        self.json_send_explicit(BaseRequirementDecorator.connection, auth_request.dict())
        auth_data: schemas.AuthData = self.schema_unpack_explicit(self.connection)
        if 'username' in fields and 'password' in fields:
            kwargs['username'], kwargs['password'] = auth_data.username, auth_data.password
            return self.function(obj, **kwargs)
        username, password = auth_data.username, auth_data.password
        if username != BaseRequirementDecorator.username:
            raise exceptions.InvalidCredentialsReceived(self.function, 'username')
        elif password != BaseRequirementDecorator.password:    
            raise exceptions.InvalidCredentialsReceived(self.function, 'password')

        return self.function(obj, **kwargs)


class NeedsConfirmation(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        confirmation_request = schemas.ConfirmationRequest(message=f"You requested to {self.function.__name__}. Please confirm (y/n)")
        self.json_send_explicit(BaseRequirementDecorator.connection, confirmation_request.dict())
        confirmation_reply: schemas.ResponseData = self.schema_unpack_explicit(self.connection)
        confirmed = confirmation_reply.response_message
        if not confirmed:
            raise exceptions.NoConfirmationError(self.function)
        return self.function(obj, **kwargs)
    
class TestDecorator(BaseRequirementDecorator):
    def __call__(self, obj, *args, **kwargs):
        print(BaseRequirementDecorator.connection)
        return self.function(obj, **kwargs)
    
class DecoratorSetup:
    def configure_decorators(self):
        BaseRequirementDecorator.connection = self.connection
        BaseRequirementDecorator.username = self.username
        BaseRequirementDecorator.password = self.password
    

class AnimatedLoading:
    def __init__(self, func: typing.Callable):
        update_wrapper(self, func)
        self.function = func
        self.__code__ = func.__code__
        self.animation_frames = ['|','/','-','\\']

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __repr__(self):
        return self.function
    
    def __str__(self):
        return str(self.function)
    
    def animation(self):
        while True:
            for frame in self.animation_frames:
                sys.stdout.write(f'\rloading ' + frame)
                sys.stdout.flush()
                time.sleep(0.5)
    
    def __call__(self, obj, *args, **kwargs):
        animation_thread = helpers.KillableThread(target=self.animation)
        animation_thread.start()
        result = self.function(obj, *args, **kwargs)
        animation_thread.kill()
        return result


if __name__ == "__main__":
    class Silly(DecoratorSetup):
        def __init__(self):
            self.connection = "x"
            self.username = "y"
            self.password = "v"
            self.configure_decorators()

        @TestDecorator
        def sillify(self, x):
            return "THIS WORKED"
        
    zeugmizer = Silly()
    print(zeugmizer.sillify(x="zed"))