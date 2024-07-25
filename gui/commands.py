from config.processingCommands import GetCommands, DeleteCommand, UpdateCommand
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from collections import namedtuple

class Scroll:
    def add(self, canvas: CTkCanvas):
        self.scrollbar = CTkScrollbar(canvas, command = canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = 'y')
        canvas.configure(scrollregion = canvas.bbox(ALL), yscrollcommand=self.scrollbar.set)
        canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 110), 'units'))


    def delete(self, canvas: CTkCanvas):
        self.scrollbar.pack_forget()
        canvas.unbind('<MouseWheel>')
        canvas.yview_moveto(0)

        

    
scroll = Scroll()

class CommandManager:
    def __init__(self, canvas: CTkCanvas):
        self.canvas = canvas
        self.canvas.delete(ALL)
        self.outputCommands()

    def createControlCommandButtons(self, position, command):
        buttonEditCommand = CTkButton(self.canvas, text='📝', font=("Helvetica", 14, "bold"), cursor='hand2', fg_color='black', command=lambda: self.editCommand(command))
        buttonDeleteCommand = CTkButton(self.canvas, text='❌', font=("Helvetica", 10, "bold"), cursor='hand2', fg_color='red', command=lambda: self.deleteCommand(command))
        
        self.canvas.create_window(564, position + 33, window=buttonEditCommand, height=19, width=22)
        self.canvas.create_window(564, position + 55, window=buttonDeleteCommand, height=19, width=22)    


    def outputCommands(self, position: int = 0):
        ''' Вывод всех команд в меню '''
        for command in [namedtuple('command', ['name', 'text'])(key, value) for command in GetCommands() for key, value in command.items()]:
            displayCommand = CTkTextbox(self.canvas, 530, 40, font=("Helvetica", 14, "bold"))
            displayCommand.insert('0.0', text=command.name)
            displayCommand.configure(state="disabled")
            displayCommand.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta / -110), 'units'))
        
            self.canvas.create_window(290, position + 45, window=displayCommand)
            self.createControlCommandButtons(position, command) # Добавляем кнопки упраление редактирование/удаление команды
                        
            position += 50 

        button_add_command = CTkButton(self.canvas, text = 'Добавить новую команду', font=("Helvetica", 11, "bold"), cursor='hand2', command= self.editCommand)
        self.canvas.create_window(110, position + 40, window = button_add_command)

        scroll.add(self.canvas)


    def deleteCommand(self, command):
        ''' Удаление команды '''
        scroll.delete(self.canvas)
        self.canvas.delete(ALL)

        dispalyConfirmationDeleteСommand = CTkTextbox(self.canvas, 350 + len(command.name)*7.2, 40, font=("Helvetica", 14, "bold"))
        dispalyConfirmationDeleteСommand.insert('0.0', text=f'Вы действительно хотите удалить команду {command.name}?')
        dispalyConfirmationDeleteСommand.configure(state="disabled")
        self.canvas.create_window(300, 50, window=dispalyConfirmationDeleteСommand)

        button_delete_command = CTkButton(self.canvas, text='Удалить', font=("Helvetica", 10, "bold"), cursor='hand2', fg_color='red', 
                                          command= lambda: (DeleteCommand(command.name), 
                                                            CTkMessagebox(title="Successfully", message='Команда успешно удалена', icon="check", option_1="Понятно", width=400, height=100),
                                                            CommandManager(self.canvas))
                                          )
        self.canvas.create_window(200, 110, window=button_delete_command)

        button_cancel = CTkButton(self.canvas, text='Отмена', font=("Helvetica", 10, "bold"), cursor='hand2', command=lambda: CommandManager(self.canvas))
        self.canvas.create_window(400, 110, window=button_cancel)

    def editCommand(self, command: tuple = None):
        ''' Создание или редактирование команды'''
        scroll.delete(self.canvas)
        self.canvas.delete(ALL)

        inputNameCommand = CTkEntry(self.canvas, 450, 20, placeholder_text="Введите название команды")
        self.canvas.create_window(270, 50, window=inputNameCommand)

        inputTextCommand = CTkTextbox(self.canvas, 450, 200)
        self.canvas.create_window(270, 200, window=inputTextCommand)

        if command:
            inputNameCommand.insert(index = 0, string = command.name)
            inputTextCommand.insert('0.0', text = command.text)

        else:
            inputTextCommand.insert('0.0', text='Введите текст при выводе команды')

        button_cancel = CTkButton(self.canvas, text='Отмена', font=("Helvetica", 10, "bold"), cursor='hand2', command=lambda: CommandManager(self.canvas))
        self.canvas.create_window(450, 350, window=button_cancel)

        def saveCommand(command, inputNameCommand, inputTextCommand):
            command = UpdateCommand.validation(command, inputNameCommand, inputTextCommand)
            
            if type(command).__name__ == 'error':
                CTkMessagebox(title="Error", message=command.text, icon="cancel", option_1="Понятно", width=400, height=100) 
                
            
            else: 
                UpdateCommand(command)


        button_save_command = CTkButton(self.canvas, text='Сохранить', font=("Helvetica", 10, "bold"), cursor='hand2', 
                                        command=lambda: (
                                                        saveCommand(command, inputNameCommand.get(), inputTextCommand.get('0.0', END)),
                                                        CommandManager(self.canvas)
                                                        )
                                        )
        self.canvas.create_window(150, 350, window=button_save_command)
        