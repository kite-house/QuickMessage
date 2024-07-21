from customtkinter import *
from CTkMenuBar import *
from gui.commands import CommandManager

root = CTk()
root.title('QuickMessage')
root.geometry('600x400')
root._set_appearance_mode('dark')

canvas = CTkCanvas(root, bg = '#242424', highlightbackground = '#242424')
canvas.pack(fill= 'both', expand=True)

menu = CTkTitleMenu(master=root)
menu.add_cascade(text='Аккаунты')
menu.add_cascade(text='Команды', postcommand = lambda: CommandManager(canvas))
menu.add_cascade(text='Настройки')




root.config(menu=menu)
root.mainloop()