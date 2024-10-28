# fetch_qc/models.py
from dataclasses import dataclass

@dataclass
class Question:
    number: str
    body: str
    choices: str  # Change to List[str] if you prefer to store choices as a list
