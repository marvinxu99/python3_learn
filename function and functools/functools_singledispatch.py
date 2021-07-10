
from dataclasses import dataclass
from functools import singledispatch


@singledispatch
def greet(instance) -> str:
    """Default case."""
    raise NotImplementedError

@greet.register
def _greet_str(instance: str) -> str:
    return 'Hello, {0}!'.format(instance)

# Custom type

@dataclass
class MyUser(object):
    name: str

@greet.register
def _greet_myuser(instance: MyUser) -> str:
    return 'Hello again, {0}'.format(instance.name)


print(greet('world'))
# Hello, world!
print(greet(MyUser(name='example')))
# Hello again, example

