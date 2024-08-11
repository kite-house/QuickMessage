from customtkinter import CTk, CTkCanvas
from CTkMenuBar import CTkTitleMenu
from gui.commands import CommandManager
from gui.accounts import Authorization

class Canvas(CTkCanvas):
    def __init__(self):
        super().__init__()
        self.configure(bg = '#242424', highlightbackground = '#242424')
        self.pack(fill = 'both', expand = True)

class Menu(CTkTitleMenu): 
    def __init__(self, master, canvas, user_is_authorized):
        super().__init__(master)
        self.add_cascade(text='Команды', postcommand = lambda: CommandManager(canvas, user_is_authorized))

class Ui(CTk):
    def __init__(self):
        super().__init__()

    def create(self, user_is_authorized):
        self.canvas = Canvas()
        self.title('QuickMessage')
        self.geometry('600x400')        
        self._set_appearance_mode('dark')
        self.config(menu=Menu(self, self.canvas, user_is_authorized))
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.resizable(width=False, height=False)
        if user_is_authorized:
            CommandManager(self.canvas, user_is_authorized)
        else:
            Authorization(self.canvas)

    def close(self):
        self.withdraw()
        self.quit()

ui = Ui()


def launch(user_is_authorized):
    ui.create(user_is_authorized)
    ui.mainloop()