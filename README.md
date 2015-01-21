# gpgpass
gpgpass is a password simple command line password manager written in python.
It encrypts the passwords using gpg and stores them passwords in a file.

## Installation
I recommend to use python 3 although it is not required.
Python 2 works as well but command aliases are not supported.
Clone the repository and either install the dependencies:
```
$ virtualenv env
$ . ./env/bin/activate
$ python setup.py -e .
```
and run it local
```
$ python -m gpgpass
```
or install is globally (more convenient and recommended)
```
$ python[3] setup.py install
```
this also installs a script so your can run gpgpass like this:
```
$ gpgpass
```

## Usage
    optional arguments:
      -h, --help            show this help message and exit
      -p                    interactively ask for the passphrase
      --passphrase PASSPHRASE
                            your key's passphrase
      -H HOMEDIR, --homedir HOMEDIR
                            path to your pgp home directory (the directory wich
                            contains keyrings), default is "~/.gnupg"
      -f FILE, --file FILE  path to the password file, default is "~/.gpgpass"
      -k KEY_ID, --key_id KEY_ID
                            fingerprint of your gpg key, this will override the
                            fingerprint specified in "~/.gpgpass_id"
    
    commands:
      tells gpgpass what to do
    
      {store,s,retrieve,r,delete,d,list,l}
        store (s)           stores a new password to the password safe
        retrieve (r)        retrieves a password
        delete (d)          deletes a password from the safe
        list (l)            prints a list of all password names
Since your gpg key's fingerprint normally does not change, you can put it into the `~/.gpgpass_id` file.

## Dependencies
- gnupg
- pyperclip (for copying passwords into the clipboard)