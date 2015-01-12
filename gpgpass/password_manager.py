import gnupg
import os.path

class PasswordManager:
    def __init__(self, homedir = os.path.expanduser('~'), password_file = os.path.join(os.path.expanduser('~'), '.gpgpass'), key_id = None):
        self._gpg = gnupg.GPG(homedir=homedir)
        self._gpg.encoding = 'utf-8'
        self._password_file = password_file
        self._passwords = ''
        self.reload()
        if key_id != None:
            self.key_id = key_id

    def add_password(self):

        pass

    def retrieve_password(self, name):
        pass

    def lookup_password(self, searchstring):
        pass

    def delete_password(self):
        pass

    def reload(self):
        fp = open(self._password_file, 'r', 'ascii')
        self._passwords = fp.read()
        fp.close()
        return None

    def save(self):
        fp = open(self._password_file, 'w', 'ascii')
        fp.write(self._passwords)
        fp.close()
        return None
