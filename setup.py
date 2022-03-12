#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

requirements = ['Click==8.0.0', 'colorama==0.4.4', 'environs==9.3.2']

test_requirements = [
    'pytest==6.2.4',
    'pytest-cov==2.12.0',
    'pytest-dotenv==0.5.2'
]

setup(
    author="Ghassen Telmoudi",
    author_email='ghassen.telmoudi@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="JustDoIt is a tool which help you organize your tasks in different boards.",
    entry_points={
        'console_scripts': [
            'justdoit=just_do_it_cli.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    package_data={'': ['.env']},
    include_package_data=True,
    keywords='just_do_it_cli',
    name='just_do_it_cli',
    packages=find_packages(include=['just_do_it_cli', 'just_do_it_cli.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pyghassen/just_do_it_cli',
    version='0.1.3',
    zip_safe=False,
)
