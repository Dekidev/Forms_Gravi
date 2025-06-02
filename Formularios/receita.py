import customtkinter as ctk

class Receita(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_data = ctk.CTkLabel(self, text='Data da receita:')
        self.label_data.grid(row= 1, column=0, padx= 10, pady= (10,0))
        self.campo_data = ctk.CTkEntry(self,placeholder_text='Digite a data')
        self.campo_data.grid(row=2, column= 0, padx= 10, pady= (10,0))

        self.label_CRM = ctk.CTkLabel(self, text='CRM:')
        self.label_CRM.grid(row= 1, column=1, padx= 10, pady= (10,0))
        self.campo_CRM = ctk.CTkEntry(self,placeholder_text='Digite o CRM')
        self.campo_CRM.grid(row=2, column= 1, padx= 10, pady= (10,0))

        self.label_Medico = ctk.CTkLabel(self, text='Nome do médico:')
        self.label_Medico.grid(row= 3, column=0, padx= 10, pady= (10,0))
        self.campo_Medico = ctk.CTkEntry(self,placeholder_text='Digite o nome')
        self.campo_Medico.grid(row=4, column= 0, padx= 10, pady= 10, stick= 'ew', columnspan=3)
