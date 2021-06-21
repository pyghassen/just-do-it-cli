from setuptools import setup

setup(
    name='just-do-it-cli',
    version='0.1.1',
    author='Ghassen Telmoudi',
    author_email='ghassen.telmoudi@gmail.com',
    py_modules=['just_do_it_cli'],
    install_requires=[
        'Click==8.0.0',
        'colorama==0.4.4',
        'environs==9.3.2'
    ],
    entry_points={
        'console_scripts': [
            'justdoit = app.main:cli',
        ],
    },
)
