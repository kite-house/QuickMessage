from config.processingCommands import GetCommands, DeleteCommand, UpdateCommand
from customtkinter import *

class CommandManager:
    def __init__(self, canvas: CTkCanvas):
        self.canvas = canvas
        self.canvas.delete(ALL)
        self.outputCommands()

    def createControlButtons(self, position, command):
        button_edit = CTkButton(self.canvas, text='📝', font=("Helvetica", 14, "bold"), cursor='hand2', fg_color='black', command=lambda: self.editCommand(command))
        button_delete = CTkButton(self.canvas, text='❌', font=("Helvetica", 10, "bold"), cursor='hand2', fg_color='red', command=lambda: self.confirmationDeleteCommand(command))
        
        self.canvas.create_window(564, position + 33, window=button_edit, height=19, width=22)
        self.canvas.create_window(564, position + 55, window=button_delete, height=19, width=22)    

    def outputCommands(self, position:int = 0):
        self.commands = [(key, value) for command in GetCommands() for key, value in command.items()]
        
        for command in self.commands:
            self.textbox = CTkTextbox(self.canvas, 530, 40, font=("Helvetica", 14, "bold"))
            self.textbox.insert('0.0', text=command[0])
            self.textbox.configure(state="disabled")
            self.canvas.create_window(290, position + 45, window=self.textbox)
            self.createControlButtons(position, command)
                        
            position += 50 

        button_add_command = CTkButton(self.canvas, text = 'Добавить новую команду', font=("Helvetica", 11, "bold"), cursor='hand2', command= self.editCommand)
        self.canvas.create_window(110, position + 40, window = button_add_command)

    def confirmationDeleteCommand(self, command):
        self.canvas.delete(ALL)
        
        self.textbox = CTkTextbox(self.canvas, 340 + len(command)*7.5, 40, font=("Helvetica", 14, "bold"))
        self.textbox.insert('0.0', text=f'Вы действительно хотите удалить команду {command}?')
        self.textbox.configure(state="disabled")

        def deleteCommand():
            DeleteCommand(command[0])
            CommandManager(self.canvas)

        button_delete_command = CTkButton(self.canvas, text='Удалить', font=("Helvetica", 10, "bold"), cursor='hand2', fg_color='red', command= deleteCommand)
        button_cancel_command = CTkButton(self.canvas, text='Отмена', font=("Helvetica", 10, "bold"), cursor='hand2', command=lambda: CommandManager(self.canvas))
        

        self.canvas.create_window(300, 50, window=self.textbox)
        self.canvas.create_window(200, 110, window=button_delete_command)
        self.canvas.create_window(400, 110, window=button_cancel_command)

    def editCommand(self, command: str = None):
        self.canvas.delete(ALL)
        
        commandName = CTkEntry(self.canvas, 450, 20, placeholder_text="Введите название команды")
        self.canvas.create_window(270, 50, window=commandName)

        text = CTkTextbox(self.canvas, 450, 200)
        self.canvas.create_window(270, 200, window=text)

        if command != None:
            commandName.insert(index = 0, string = command[0])
            text.insert('0.0', text = command[1])

        else:
            text.insert('0.0', text='Введите текст при выводе команды')


        button_cancel_command = CTkButton(self.canvas, text='Отмена', font=("Helvetica", 10, "bold"), cursor='hand2', command=lambda: CommandManager(self.canvas))
        self.canvas.create_window(450, 350, window=button_cancel_command)


        def saveCommand(commandName, text, command = command):
            if command[0] != commandName.get():
                DeleteCommand(command[0])
                
            if not commandName.get().startswith('/'):
                command = f'/{commandName.get()}'
            else:
                command = commandName.get()
            
            UpdateCommand(command, text.get('0.0', END))
            CommandManager(self.canvas)


        button_save_command = CTkButton(self.canvas, text='Сохранить', font=("Helvetica", 10, "bold"), cursor='hand2', command=lambda: saveCommand(commandName, text))
        self.canvas.create_window(150, 350, window=button_save_command)
        