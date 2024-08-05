from customtkinter import CTk, CTkCanvas
from CTkMenuBar import CTkTitleMenu
from gui.commands import CommandManager
from gui.accounts import Authorization
from auth import User

class Canvas(CTkCanvas):
    def __init__(self):
        super().__init__()
        self.configure(bg = '#242424', highlightbackground = '#242424')
        self.pack(fill = 'both', expand = True)

class Menu(CTkTitleMenu): 
    def __init__(self, master, canvas):
        super().__init__(master)
        if User.is_authorized:
            CommandManager(canvas)
        else:
            Authorization(canvas)
        self.add_cascade(text='Команды', postcommand = lambda: CommandManager(canvas))

class Ui(CTk):
    def __init__(self):
        super().__init__()

    def create(self):
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
    ui.create()
    ui.mainloop()