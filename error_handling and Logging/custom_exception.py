"""
(1) BaseException is a base class provided for all error types. To create 
a new error type, you must derive your class from BaseException or one 
of its derived classes. 
(2) The convention in Python is to derive your custom error types from 
Exception, which in turn derives from BaseException.

"""
class MyError(Exception):
    pass

raise MyError()