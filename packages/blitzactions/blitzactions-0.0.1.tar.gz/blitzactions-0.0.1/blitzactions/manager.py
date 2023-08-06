import openai
from .exceptions import NoFunctionFoundException
from .models import Action, Caller

class ActionsManager:
    def __init__(self, openai_api_key: str) -> None:
        self.api_key = openai_api_key
        self.registered_actions = []
        self.caller = Caller()

    def register(self, func):
        self.registered_actions.append(Action(func))
        self.caller.__setattr__(func.__name__, func)
        return func
    
    def get_prompt(self):
        prompt = 'The functions are:\n'
        for action in self.registered_actions:
            prompt += action.get_prompt_substring()
        return prompt
    
    def get_executable(self, prompt: str):
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a program controller that decides which functions get executed based on the incoming request. You dont worry about the implementation or the output of the function. You understand the task to be executed form the request and choose which function to execute. Your response must include only the call signature of the function alone in plain text and no other prose. Do not format the result within parenthesis. The function name must not be formatted in a code block. You need not worry about the implementation or providing output of the functions. Your job is to purely choose which function to call and its parameters. Whenever you are given a prompt that doesnt not have a valid function to call, you only return NO_FUNCTION_FOUND and nothing else. These are the only two possible responses, either you give the function, or NO_FUNCTION_FOUND. You must not ever add comments in your code\n\n{self.get_prompt()}"},
                {"role": "user", "content": prompt},
            ],
            max_tokens=15,
            temperature=0.0,
        )
        return result["choices"][0]["message"]["content"]
    

    def execute(self, prompt: str):
        result = self.get_executable(prompt)
        if result == 'NO_FUNCTION_FOUND':
            raise NoFunctionFoundException(f'No function found for prompt \"{prompt}\"')
        else:
            return eval(f'self.caller.{result}')


