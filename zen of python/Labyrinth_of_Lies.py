'''

https://orbifold.xyz/labyrinth.html
In the 1986 movie Labyrinth, a young girl (played by Jennifer Connelly) is faced with a dilemma. 
The adorable Jim Henson puppets explain to her that one guard always lies, and one guard always 
tells the truth. She needs to figure out which door leads to the castle at the center of the 
eponymous Labyrinth, and which one to certain death (dun-dun-dun!).

I decided that like any reasonable movie watcher, I need to implement this in Python.

First, I implemented two guards: one who always tells the truth, and one who always lies. 
The guards know who they are, and what the doors are, but can only answer True or False.

This being a children’s movie, the girl defeats all odds and figures out what to 
ask the guard: “would he (points to the other guard) tell me that 
this (points to the door on the left) door leads to the castle?”
'''
import dataclasses
from typing import List

guards = [None, None]
doors = ["certain death", "castle"]

@dataclasses.dataclass
class Guard:
    _truth_teller: bool
    _guards: List
    _doors: List[str]

    def ask(self, question):
        answer = bool(question(self, self._guards, self._doors))
        if not self._truth_teller:
            answer = not answer
        return answer

guards[0] = Guard(True, guards, doors)
guards[1] = Guard(False, guards, doors)

def question(guard, guards, doors):
    other_guard, = (candidate for candidate in guards if candidate != guard)
    def other_question(ignored, guards, doors):
        return doors[0] == "castle"
    return other_guard.ask(other_question)

    