from customtkinter import *
from CTkMessagebox import CTkMessagebox
import auth

class Authorization:
    def __init__(self, canvas: CTkCanvas):
        self.canvas = canvas
        self.canvas.delete(ALL)
        self.inputNumber()

    def inputNumber(self):
        self.canvas.delete(ALL)
        text = CTkLabel(self.canvas, 300, 40, text = 'Авторизация')
        text.configure(font=("Helvetica", 14, "bold"))
        self.canvas.create_window(300, 100, window = text)

        number = CTkEntry(self.canvas, 300, 40, placeholder_text='Введите номер телефона')
        number.configure(font=("Helvetica", 14, "bold"), fg_color = '#1D1E1E', border_color = '#1D1E1E')

        def send_code():
            try:
                auth.SendCode(number.get())
            except Exception as error:
                number.delete(0, END)
                CTkMessagebox(title="Error", message=error, icon="cancel", option_1="Понятно", width=400, height=100)

            else:
                self.inputCode()


        number.bind('<Return>', lambda event: send_code())

        self.canvas.create_window(300, 150, window=number)

    def inputCode(self):
        self.canvas.delete(ALL)

        text = CTkLabel(self.canvas, 300, 40, text = 'Авторизация')
        text.configure(font=("Helvetica", 14, "bold"))
        self.canvas.create_window(300, 100, window = text)

        code = CTkEntry(self.canvas, 300, 40, placeholder_text='Введите код')
        code.configure(font = ('Helvetica', 14, 'bold'), fg_color = '#1D1E1E', border_color = '#1D1E1E')
        
        fixNumber = CTkButton(self.canvas, text = 'Ввести другой номер', font=("Helvetica", 10, "bold"), cursor = 'hand2', command= self.inputNumber)
        self.canvas.create_window(300, 200, window = fixNumber)


        def sign():
            try:
                auth.Sign(code.get())
            except Exception as error:
                code.delete(0, END)
                CTkMessagebox(title="Error", message=error, icon="cancel", option_1="Понятно", width=400, height=100)

            else:
                self.finish()

        code.bind('<Return>', lambda event: sign())

        self.canvas.create_window(300, 150, window = code)

    def finish(self):
        self.canvas.delete(ALL)

        text = CTkLabel(self.canvas, 300, 40, text = 'Авторизация')
        text.configure(font=("Helvetica", 14, "bold"))
        self.canvas.create_window(300, 100, window = text)

        result = CTkLabel(self.canvas, 300, 40, text= 'Поздравляем вы завершили авторизацию')
        result.configure(font = ('Helvetica', 14, 'bold'), fg_color = '#1D1E1E')

        self.canvas.create_window(300, 150, window = result)

        # задержка 2 секунды

        self.canvas.after(2000, self.canvas.quit)  # завершение через 2 секунды

