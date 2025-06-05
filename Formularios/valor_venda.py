import customtkinter as ctk

class ValorVenda(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Insira os valores da venda')
        self.label_titulo.grid(row=0,column=0, padx=10, pady=(10,0),sticky='n')

        self.label_bruto = ctk.CTkLabel(self, text='Valor Bruto:')
        self.label_bruto.grid(row=1,column=0, padx=10, pady=(10,0),sticky='w')
        self.campo_bruto = ctk.CTkEntry(self, placeholder_text='Digite o valor bruto')
        self.campo_bruto.grid(row=1, column=1, padx=10, pady=(10,0),sticky= 'e')

        self.label_desc = ctk.CTkLabel(self, text='Desconto:')
        self.label_desc.grid(row=2, column=0, padx=10, pady=(10,0), sticky='w')
        self.campo_desc = ctk.CTkEntry(self,placeholder_text='Digite o desconto')
        self.campo_desc.grid(row=2, column=1, padx=10, pady=(10,0),sticky= 'e')

        self.label_total = ctk.CTkLabel(self, text='Valor total:') 
        self.label_total.grid(row=3,column=0, padx=10, pady=(10,0), sticky='w')
        #talvez campo total seja texto e nao input        
        self.campo_total = ctk.CTkEntry(self,placeholder_text='Digite o total')
        self.campo_total.grid(row=3, column=1, padx=10, pady=(10,0), sticky='e')

    @property
    def obter_dados(self):
        return {
            "valor_bruto": self.campo_bruto.get(),
            "desconto": self.campo_desc.get(),
            "valor_total": self.campo_total.get()
        }