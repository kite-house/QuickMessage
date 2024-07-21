import json

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
    def __init__(self, text: str):
        super().__init__()
        text = text.replace('/editCommand', '').strip()
        if not text:
            return
        self.data[text.split(' ')[0]] = text.replace(text.split(" ")[0], '').strip()
        super().__init__(mode = 'w+', data = self.data)
