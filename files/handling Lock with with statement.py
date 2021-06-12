Handling Locks in Multithreaded Programs

Another good example of using the with statement effectively in the Python standard library 
is threading.Lock. This class provides a primitive lock to prevent multiple threads from modifying 
a shared resource at the same time in a multithreaded application.

You can use a Lock object as the context manager in a with statement to automatically acquire and 
release a given lock. For example, say you need to protect the balance of a bank account:

/***************************/
import threading

balance_lock = threading.Lock()

# Use the try ... finally pattern
balance_lock.acquire()
try:
    # Update the account balance here ...
finally:
    balance_lock.release()

# Use the with pattern
with balance_lock:
    # Update the account balance here ...

The with statement in the second example automatically acquires and releases a lock when the flow of 
execution enters and leaves the statement. This way, you can focus on what really matters in your code 
and forget about those repetitive operations.

In this example, the lock in the with statement creates a protected region known as the critical 
section, which prevents concurrent access to the account balance.