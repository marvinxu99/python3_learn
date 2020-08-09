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

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Protocol, Sequence
from enum import Enum


class Door(Enum):
    certain_death = "certain death"
    castle = "castle"


class Question(Protocol):
    def __call__(
        self, guard: Guard, guards: Sequence[Guard], doors: Sequence[Door]
    ) -> bool:
        ...


@dataclass
class Guard:
    _truth_teller: bool
    _guards: Sequence[Guard]
    _doors: Sequence[Door]

    def ask(self, question: Question) -> bool:
        answer = question(self, self._guards, self._doors)
        if not self._truth_teller:
            answer = not answer
        return answer


def question(guard: Guard, guards: Sequence[Guard], doors: Sequence[Door]) -> bool:
    [other_guard] = (candidate for candidate in guards if candidate != guard)

    def other_question(
        guard: Guard, guards: Sequence[Guard], doors: Sequence[Door]
    ) -> bool:
        return doors[0] == Door.castle

    return other_guard.ask(other_question)


def make_guard_post() -> Sequence[Guard]:
    doors = list(Door)
    guards: List[Guard] = []
    guards[:] = [Guard(True, guards, doors), Guard(False, guards, doors)]
    return guards


def main() -> None:
    print(all(each.ask(question) for each in make_guard_post()))


if __name__ == "__main__":
    main()