import json

class Commands:
    def __init__(self, file: str = 'config/commands.json', mode: str = 'r'):
        try:
            with open(file, mode, encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            open('config/commands.json', 'w+')
class ApplicationCommands(Commands):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def __str__(self):
        return str(self.data[self.text.split(' ')[0]]).format(*self.text.split(' ')[1:])

class EditCommands(Commands):
    pass