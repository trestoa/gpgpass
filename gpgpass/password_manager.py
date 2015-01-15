import gnupg
import os.path
import json

class PasswordManager:
    def __init__(self, key_id, passphrase, homedir=os.path.join(os.path.expanduser('~'), '.gnupg'), password_file=os.path.join(os.path.expanduser('~'), '.gpgpass'), operation_mode=1):
        self._gpg = gnupg.GPG(homedir=homedir, binary='gpg')
        self._gpg.encoding = 'utf-8'
        self._operation_mode = operation_mode
        self.password_file = password_file
        self.passwords = None
        self._passphrase = passphrase
        self.key_id = key_id
        self.reload()

    def store_password(self, name, value):
        if self._operation_mode == 1:
            self.passwords[name] = value;
        return None

    def retrieve_password(self, name):
        if self._operation_mode == 1:
            return self.passwords[name]

    def lookup_password(self, searchstring):
        """NYI"""
        pass

    def delete_password(self, name):
        if self._operation_mode:
            del self.passwords[name]

    def reload(self):
        if os.path.isfile(self.password_file):
            fp = open(self.password_file, 'r', encoding='ascii')
            password_file_content = fp.read()
            if self._operation_mode == 1:
                self.passwords = json.loads(str(self._gpg.decrypt(password_file_content, passphrase=self._passphrase)))
            fp.close()
        else:
            self.passwords = {}
        return None

    def save(self):
        fp = open(self.password_file, 'w', encoding='ascii')
        if self._operation_mode == 1:
            password_file_content = str(self._gpg.encrypt(json.dumps(self.passwords), self.key_id, passphrase=self._passphrase, default_key=self.key_id))
        fp.write(password_file_content)
        fp.close()
        return None
