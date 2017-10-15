import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'flask_restplus_patched/__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-restplus-patched",
    version=__version__,
    url="https://github.com/Jaza/flask-restplus-patched",

    author="Jeremy Epstein",
    author_email="jazepstein@gmail.com",

    description="Extends Flask-RESTplus so it can handle Marshmallow schemas and Webargs arguments.",
    long_description=open('README.md').read(),

    py_modules=['flask_restplus_patched'],
    zip_safe=False,
    platforms='any',

    install_requires=[
        'Flask', 'flask-restplus', 'marshmallow', 'flask-marshmallow',
        'webargs', 'apispec'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
