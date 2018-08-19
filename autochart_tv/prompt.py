from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import FileHistory

from fuzzyfinder import fuzzyfinder

class AutoChartCompleter(Completer):
    def __init__(self, words):
        super().__init__()
        self.words = words

    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, self.words)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))


class AutoChartPrompt:
    def __init__(self, commands=['Exit']):
        self.commands = commands

    def get_prompt(self):
        return prompt('>',
                      completer=AutoChartCompleter(self.commands),
                      complete_while_typing=True,
                      history=FileHistory('autochart_history.txt')
                      )
