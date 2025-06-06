import customtkinter as ctk
from Resultados.resultado_frame import ResultFrame

class copiar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.btn = ctk.CTkButton(self, text='Copiar Formulário', command=self.copiar_clipboard)
        self.btn.grid(row=0, column=0, sticky='ew')

    def copiar_clipboard(self):
        texto_para_copiar = ResultFrame.get_forms_atualizado()
        self.clipboard_clear()
        self.clipboard_append(texto_para_copiar)
        self.btn.configure(text='Copiado Com Sucesso!')
        self.after(2000, self.restaurar_texto_btn)
    
    def restaurar_texto_btn(self):
        self.btn.configure(text='Copiar Formulário')
       
        