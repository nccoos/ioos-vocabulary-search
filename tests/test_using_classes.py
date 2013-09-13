# Demo showing how to create tests using classes
#
# The class methods are tests, with setup and teardown of fixtures.
# This demonstrates how setup and teardown get used by nose on every
# test method. 


import sys

class TestClass():

    def setup(self):
        print >> sys.stderr, 'TestClass.setup() -----------|'
        self.a = 'a'
        self.b = 'b'

    def teardown(self):
        print >> sys.stderr, 'TestClass.teardown() -------|'
        self.a = None
        self.b = None

    def test_simple_fail(self):
        print >> sys.stderr, 'TestClass.test_simple_fail()'
        assert self.a != self.b

    def test_simple_pass(self):
        print >> sys.stderr, 'TestClass.test_simple_pass()'
        assert self.a == self.a
 
