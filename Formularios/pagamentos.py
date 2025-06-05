import customtkinter as ctk

class Pagamento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #tester titulos(row=0, sem column)
        self.label_titulo = ctk.CTkLabel(self, text='Insira as informações de pagamento')
        self.label_titulo.grid(row=0,column=0, padx=10, pady=(10,0),sticky='n')

        self.label_data = ctk.CTkLabel(self, text='Data:')
        self.label_data.grid(row=1,column=0, padx=10, pady=(10,0), sticky='w')
        self.campo_data = ctk.CTkEntry(self, placeholder_text='Insira a Data')
        self.campo_data.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        self.label_forma = ctk.CTkLabel(self, text='Forma de Pagamento:')
        self.label_forma.grid(row=2, column=0, padx=10, pady=(10,0), sticky='w')
        self.campo_forma = ctk.CTkEntry(self,placeholder_text='Digite a forma de pagamento')
        self.campo_forma.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        self.label_ValorPago = ctk.CTkLabel(self, text='Valor pago:') 
        self.label_ValorPago.grid(row=3,column=0, padx=10, pady=(10,0), sticky='w')    
        self.campo_ValorPago = ctk.CTkEntry(self,placeholder_text='Digite valor pago')
        self.campo_ValorPago.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        self.label_saldo = ctk.CTkLabel(self, text='Saldo:') 
        self.label_saldo.grid(row=4,column=0, padx=10, pady=(10,0), sticky='w')    
        self.campo_saldo = ctk.CTkEntry(self,placeholder_text='Digite o saldo')
        self.campo_saldo.grid(row=4, column=1, padx=10, pady=10, sticky='e')

    @property
    def obter_dados(self):
        return {
            "data_pagamento": self.campo_data.get(),
            "forma_pagamento": self.campo_forma.get(),
            "valor_pago": self.campo_ValorPago.get(),
            "saldo": self.campo_saldo.get()
        }