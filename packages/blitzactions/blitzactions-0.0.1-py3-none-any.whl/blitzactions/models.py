from inspect import signature
from typing import Callable, Any

class Action:
    def __init__(self, function: Callable) -> None:
        self.func = function
        self.description = function.__doc__

    def get_prompt_substring(self):
        return f'{self.func.__name__}{signature(self.func)}: {self.description}\n'
    
    def __repr__(self) -> str:
        return f'<Action {signature(self.func)} | {self.func.__name__} | {self.description}>'
    

class Caller:
    def __init__(self) -> None:
        pass