from password_manager import PasswordManager
from getpass import getpass
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
gpgpass is a password simple command line password manager.
It encrypts the passwords using gpg and stores the passwords in a file.
''',
    epilog='''
gpgpass is free software and licensed under the MIT license.
Copyright (c) 2015, Markus Klein
'''
)

parser.add_argument('command', choices=['-s', '--store', '-r', '--retrieve', '-d', '--delete', '-l', '-L', '--list', '--list-passwords'], help='the command tells gpgpass what to do');
parser.add_argument('id', help='fingerprint of your gpg key')
parser.add_argument('-c', '--clipboard', action='store_true', help='can be used with the retrieve command to copy the password to the clipboard instead of printing it')
parser.add_argument('-p', '--passphrase', help='your key\'s passphrase, you will be asked for the passphrase if no provided')
parser.add_argument('-H', '--homedir', help='path to your pgp home directory (the directory wich contains keyrings), default is "~/.gnupg"')
parser.add_argument('-f', '--file', help='path to the password file, default is "~/.gpgpass"')
parser.add_argument('--password', help='can be used with the store command ')
args = parser.parse_args();


#password = getpass(prompt='Enter your key\'s passphrase: ')
#manager = PasswordManager('7662CEFD', password)
#manager.add_password('foo', 'bar')
#manager.save()