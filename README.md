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
Since your gpg key's fingderprint normally does not change, you can also put arguments into the `~/.gpgpass_args` file.
for the rest, type `gpgpass -h` :)

## Dependencies
- gnupg
- pyperclip (for copying passwords into the clipboard)