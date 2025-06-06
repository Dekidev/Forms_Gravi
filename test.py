import customtkinter as ctk
from Formularios.form_frame import FormFrame
from Resultados.resultado_frame import ResultFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        self.title('Gravi Forms')
        self.geometry('1600x900')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.form_frame = FormFrame(self)
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsw')

        self.result_frame = ResultFrame(self, form_frame_instance=self.form_frame)
        self.result_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        btn_enviar = ctk.CTkButton(self, text='Gerar Formulário', command=self.result_frame.atualizar_valores)
        btn_enviar.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

if __name__ == '__main__':
    app = App()
    app.mainloop()
