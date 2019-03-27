class AuthException(Exception):
    def __init__(self, username='', user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

    def __str__(self):
        return self.__class__.__name__


class TooEasyPassword(AuthException):
    def __str__(self):
        return self.__class__.__name__ + \
               ': you need to have one or more numbers'


class UsernameAlreadyExists(AuthException):
    def __str__(self):
        return self.__class__.__name__ + \
               ': please, use another username'


class PasswordTooShort(AuthException):
    def __str__(self):
        return self.__class__.__name__ + \
               ': you need to have password with more than 6 characters'


class IncorrectPassword(AuthException):
    def __str__(self):
        return self.__class__.__name__ + \
               ': incorrect password, please try again'


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass
