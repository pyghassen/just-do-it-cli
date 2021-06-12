from setuptools import setup

setup(
    name='just-do-it-cli',
    version='0.1.0',
    py_modules=['just_do_it_cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'justdoit = app.main:cli',
        ],
    },
)
