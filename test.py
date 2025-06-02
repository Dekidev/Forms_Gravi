import customtkinter as ctk
from Formularios.form_frame import FormFrame
from Resultados.resultado_frame import ResultFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        self.title('Gravi Forms')
        self.geometry('1600x900')
        self.grid_columnconfigure(1, weight= 1)
        self.grid_rowconfigure(0, weight=1)

        self.FormFrame = FormFrame(self)
        self.FormFrame.grid(row=0, column=0, padx=10, pady=10, sticky= 'nsw')

        self.ResultFrame = ResultFrame(self)
        self.ResultFrame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        btn_enviar = ctk.CTkButton(self, text='Enviar')
        btn_enviar.grid(row= 3, column= 0, padx=10, pady= 10, sticky= 'ew', columnspan= 2)

""""
#Frame de formulario
frame_main = ctk.CTkFrame(app)
frame_main.grid(row= 0, column=0, padx=10, pady= (10, 0), sticky= 'nsew')

label_titulo = ctk.CTkLabel(frame_main, text='Preencha as informações da venda', font=('arial bold',20))
label_titulo.place()

#Frame de resposta
frame_return = ctk.CTkFrame(app)
frame_return.grid(row= 0, column= 1, padx=10, pady= (10, 0), sticky= 'nsew')
"""
#botao

app= App()
app.mainloop()