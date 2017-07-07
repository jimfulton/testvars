name = 'testvars'
version = '1.0.0'

extras_require = dict(test=['zope.testing'])

from setuptools import setup

long_description = open('README.rst').read() + '\n' + open('CHANGES.rst').read()

setup(
    author = 'Jim Fulton',
    author_email = 'jim@jimfulton.info',
    url = 'https://github.com/jimfulton/testvars',
    license = 'MIT',

    name = name,
    version = version,
    long_description = long_description,
    description = long_description.strip().split('\n')[1],
    packages = [name],
    package_dir = {'': 'src'},
    zip_safe = False,
    extras_require = extras_require,

    keywords = ["test", "testing"],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
       ],

    )
