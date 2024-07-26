from customtkinter import CTk, CTkCanvas
from CTkMenuBar import CTkTitleMenu
from gui.commands import CommandManager

class Canvas(CTkCanvas):
    def __init__(self):
        super().__init__()
        self.configure(bg = '#242424', highlightbackground = '#242424')
        self.pack(fill = 'both', expand = True)

class Menu(CTkTitleMenu): 
    def __init__(self, master, canvas):
        super().__init__(master)
        self.add_cascade(text='Аккаунты')
        self.add_cascade(text='Команды', postcommand = lambda: CommandManager(canvas))
        self.add_cascade(text='Настройки')

class Ui(CTk):
    def __init__(self):
        super().__init__()
        self.title('QuickMessage')
        self.geometry('600x400')
        self._set_appearance_mode('dark')
        self.config(menu=Menu(self, Canvas()))
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.resizable(width=False, height=False)

    def close(self):
        self.withdraw()
        self.quit()

ui = Ui()

def launch():
    ui.mainloop()