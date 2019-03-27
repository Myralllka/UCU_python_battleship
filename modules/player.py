import hashlib
from modules.exceptions import *


class Player:
    """class for representing Player of the game"""

    def __init__(self, username: str, password):
        """
        initialization of class
        :param name: player name
        """
        self.__name = username
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def __str__(self):
        """
        representing player in string function
        :return: name of the player
        """
        return self.__name

    def __repr__(self):
        """
        representing player in repr function
        :return: self name
        """
        return self.__name

    @property
    def name(self):
        return self.__name

    @staticmethod
    def converter_to_normal_coordinates(coordinates: tuple) -> tuple:
        """
        function to convert inputted coordinates in normal format
        :param coordinates: inputted coordinates
        :return: normal format of inputted coordinates
        """
        columns = list('ABCDEFGHIJ')
        assert coordinates[0] in columns, 'incorrect input'
        assert int(coordinates[1]) in range(1, 11), 'incorrect input'
        # print(coordinates[1])
        i = int(coordinates[1]) - 1
        j = columns.index(coordinates[0])
        return tuple([i, j])

    def read_position(self):
        """
        read coordinates where player wants to shoot
        :return: coordinates where to shoot
        """
        tmp = input('{} > '.format(self.name))
        tmp = tuple([tmp[:1], tmp[1:]])
        return Player.converter_to_normal_coordinates(tmp)

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        if encrypted == self.password:
            return True
        else:
            raise IncorrectPassword()


class Authenticator:
    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""
        self.users = {}

    def sign_up(self, username, password):
        if username in self.users:
            print(self.users)
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        number_count = 0
        letters_count = 0
        for each in password:
            if each.isdigit():
                number_count += 1
            if each.isalpha():
                letters_count += 1
        if number_count == 0 or letters_count == 0:
            raise TooEasyPassword(username)
        self.users[username] = Player(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class Authorizer:

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, username, perm_name):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, username, perm_name):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
