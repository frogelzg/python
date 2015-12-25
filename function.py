#! /usr/bin/python

#This is a test program for function in python language.

import os
import sys

print "Test one hello world:"

def helloworld():
    print "Hello world!"

print "'__name__ is'  ", __name__

if __name__ == '__main__':
    helloworld()

print "\nTest two Method:"

def Method(x, y):
    return x**y

result = Method(3, 5)
print "The result of Method(3, 5) is ", result

print "\nTest three fib:"

def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print ""

fib(12)


print "\nTest four split:"

def _split():
    name = "Froge Liu"
    print "name is ", name
    firstname = name.split(' ')[0]
    lastname = name.split(' ')[1]
    print "first name is ", firstname
    print "last name is ", lastname

_split()

print "\nTest five test:"

def test(*keys):
    print "keys's type is ", type(keys)
    length = len(keys)
    print "keys's length is ", length
    for i in range(length):
        print "keys[%d]: " %i, keys[i] 

test(1,2,3,4)

print "\nTest six double_satr:"

def double_star(**args):
    print "args's type is ", type(args)
    length = len(args)
    print "args's length is ", length
    for property in args:
        print "args[%s] is " %property, args[property]

double_star(name="Froge", sex="Male", age="24")

print "\nTest seven _print:"

def _print(*objects, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    out = kwargs.get('file', sys.stdout)
    out.write(sep.join(objects) + end)

print "Python Current version is ", sys.version.split(' ')[0]

_print('error:Python version %s unsupported.\n'
        'Please use Python 2.6 - 2.7 instaed.'
        % sys.version.split(' ')[0], file=sys.stderr)
