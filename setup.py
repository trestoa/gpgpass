from setuptools import setup

setup(
    name='gpgpass',
    version='0.1',
    description='GPG password manager',
    url='https://github.com/kleiinnn/gpgpass',
    author='Markus Klein',
    author_email='m@mklein.co.at',
    license='MIT',
    keywords='gpg gnupg password manager',
    packages=['gpgpass'],
    entry_points={
        'console_scripts': [
            'gpgpass = gpgpass.main:main'
        ]
    },
    install_requires=[
        'gnupg',
        'pyperclip'
    ]
)
