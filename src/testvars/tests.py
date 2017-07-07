from zope.testing import doctestcase
import unittest

class MyTest(unittest.TestCase):

    test_README = doctestcase.file('README.rst')
