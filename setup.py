#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

requirements = [
    'Click>=8.3.1',
    'colorama>=0.4.6',
    'environs>=14.5.0',
]

test_requirements = [
    'pytest==9.0.3',
    'pytest-cov==6.3.0',
    'pytest-dotenv==0.5.2',
]

setup(
    author="Ghassen Telmoudi",
    author_email='ghassen.telmoudi@gmail.com',
    python_requires='>=3.12',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    description="JustDoIt is a tool which help you organize your tasks in different boards.",
    entry_points={'console_scripts': ['justdoit=just_do_it_cli.cli:main']},
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
    version='1.0.0',
    zip_safe=False,
)
