import json
from collections import namedtuple

class Commands:
    def __init__(self, file: str = 'config/commands.json', mode: str = 'r', **kwargs):
        try:
            with open(file, mode, encoding='utf-8') as file:
                if mode == 'r':
                    self.data = json.load(file)

                if mode == 'w+':
                    self.data = json.dump(kwargs['data'], file, ensure_ascii=False)
                
        except FileNotFoundError:
            open('config/commands.json', 'w+')

        except json.decoder.JSONDecodeError:
            self.data = {}

class ExecuteCommand(Commands):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def __str__(self):
        return str(self.data[self.text.split(' ')[0]]).format(*self.text.split(' ')[1:])

class GetCommands(Commands):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        for attr in self.data:
            yield {attr : self.data[attr]} 

class UpdateCommand(Commands):
    def __init__(self, command: tuple):
        super().__init__()
        self.data[command.name] = command.text
        super().__init__(mode = 'w+', data = self.data)

    @classmethod
    def validation(src, command:tuple, inputNameCommand:str, inputTextCommand:str):
        error = namedtuple('error', 'text')
        
        if not inputNameCommand:
            return error('Поле название команды не может быть пустым')

        if not inputTextCommand:
            return error('Поле сообщение не может быть пустым')

        if len(inputNameCommand) > 30:
            return error('Название команды не должно содержать больше 30 символов!')
        
        if inputNameCommand.count(' '):
            return error('Название команды не может содержать в себе пробелы!')

        if len(inputTextCommand) > 4096:
            return error('Сообщение не может содержать больше 4096 символов')
        
        if not inputNameCommand.startswith('/'):
            inputNameCommand = f'/{inputNameCommand}'

        if command:
            if command.name != inputNameCommand:
                DeleteCommand(command.name)

        return namedtuple('command', ['name', 'text'])(inputNameCommand, inputTextCommand)

class DeleteCommand(Commands):
    def __init__(self, command: str):
        super().__init__()
        del self.data[command]
        super().__init__(mode = "w+", data = self.data)