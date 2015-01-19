# This file is part of gpgpass.
#
# simple command line password manager using gnupg
# Copyright (c) 2015, Markus Klein
# MIT Licensed

from gpgpass.password_manager import PasswordManager
from getpass import getpass
import argparse
import pyperclip

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

parser.add_argument('id', help='fingerprint of your gpg key')

subparsers = parser.add_subparsers(dest='command', title='commands', description='tells gpgpass what to do')
store_parser = subparsers.add_parser('store', aliases=['s'], help='stores a new password to the password safe')
store_parser.add_argument('name')
store_parser.add_argument('-P', '--password')

retrieve_parser = subparsers.add_parser('retrieve', aliases=['r'], help='retrieves a password')
retrieve_parser.add_argument('name')
retrieve_parser.add_argument('-c', '--clipboard', action='store_true', help='copy the password to the clipboard instead of printing it')

delete_parser = subparsers.add_parser('delete', aliases=['d'], help='deletes a password from the safe')
delete_parser.add_argument('name')

list_parser = subparsers.add_parser('list', aliases=['l'], help='prints a list of all password names')
list_parser.add_argument('-P', '--with-passwords', help='show also the passwords (very dangerous!!)', action='store_true')

password_group = parser.add_mutually_exclusive_group()
password_group.add_argument('-p', help='interactively ask for the passphrase', action='store_true')
password_group.add_argument('--passphrase', help='your key\'s passphrase')

parser.add_argument('-H', '--homedir', help='path to your pgp home directory (the directory wich contains keyrings), default is "~/.gnupg"')
parser.add_argument('-f', '--file', help='path to the password file, default is "~/.gpgpass"')
args = parser.parse_args();

while args.p and not args.passphrase:
    args.passphrase = getpass(prompt='Enter your key\'s passphrase: ')

manager_args = {}
if args.homedir:
    manager_args['homedir'] = args.homedir
if args.file:
    manager_args['password_file'] = args.file

manager = PasswordManager(args.id, args.passphrase, **manager_args)


if args.command == 'store' or args.command == 's':
    if args.password is None:
        args.password = getpass(prompt='Enter the password: ')
    manager.store_password(args.name, args.password)
    manager.save()
elif args.command == 'retrieve' or args.command == 'r':
    if args.clipboard:
        pyperclip.copy(manager.retrieve_password(args.name))
    else:
        print(manager.retrieve_password(args.name))
elif args.command == 'delete' or args.command == 'd':
    manager.delete_password(args.name)
    manager.save()
elif args.command == 'list' or args.command == 'l':
    if args.with_passwords:
        passwords = manager.retrieve_passwords()
        max_length = len(max(passwords, key=len))
        for name in passwords:
            print(('{0:' + str(max_length) + '}: {1}').format(name, passwords[name]))
    else:
        for name in manager.retrieve_passwords():
            print(name)
