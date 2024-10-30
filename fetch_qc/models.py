from dataclasses import dataclass


@dataclass
class Question:
    number: str
    body: str
    choices: str
    url: str
