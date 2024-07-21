from config.processingCommands import GetCommands
from customtkinter import *


class CommandManager:
    def __init__(self, canvas: CTkCanvas):
        self.canvas = canvas
        self.canvas.delete(ALL)
        self.outputCommands()

    def createControlButtons(self, position, command):
        button_edit = CTkButton(self.canvas, text='📝', font=("Helvetica", 14, "bold"), cursor='hand2', fg_color='black', command=lambda: print(f'Редактировать {command}'))
        button_delete = CTkButton(self.canvas, text='❌', font=("Helvetica", 10, "bold"), cursor='hand2', fg_color='red', command=lambda: print(f'Удалить {command}'))
        
        self.canvas.create_window(564, position + 33, window=button_edit, height=19, width=22)
        self.canvas.create_window(564, position + 55, window=button_delete, height=19, width=22)    

    def outputCommands(self, position:int = 0):
        self.commands = [key for command in GetCommands() for key, value in command.items()]
        
        for command in self.commands:
            self.textbox = CTkTextbox(self.canvas, 530, 40, font=("Helvetica", 14, "bold"))
            self.textbox.place(x = 27 , y = position + 25)
            self.textbox.insert('0.0', text=command)
            self.textbox.configure(state="disabled")

            self.createControlButtons(position, command)
                        
            position += 50

        button_add_command = CTkButton(self.canvas, text = 'Добавить новую команду', font=("Helvetica", 11, "bold"), cursor='hand2')
        self.canvas.create_window(110, position + 40, window = button_add_command)
