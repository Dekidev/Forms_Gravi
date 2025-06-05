import customtkinter as ctk

class InfoVenda(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Insira as informações da venda')
        self.label_titulo.grid(row=0,column=0, padx=10, pady=(10,0),sticky='n')

        self.label_data_venda = ctk.CTkLabel(self, text='Data Venda:')
        self.label_data_venda.grid(row=1,column=0, padx=10, pady=(10,0),sticky='w')
        self.campo_data_venda = ctk.CTkEntry(self,placeholder_text='Digite a data da venda')
        self.campo_data_venda.grid(row=1, column=1, padx=10, pady=(10,0),sticky= 'e')
        
        self.label_OS = ctk.CTkLabel(self, text='Ordem de Serviço')
        self.label_OS.grid(row=2, column=0, padx=10, pady=(10,0), sticky='w')
        self.campo_OS = ctk.CTkEntry(self,placeholder_text='Digite a OS')
        self.campo_OS.grid(row=2, column=1, padx=10, pady=(10,0),sticky= 'e')

        self.label_desc = ctk.CTkLabel(self, text='Descrição:') 
        self.label_desc.grid(row=3,column=0, padx=10, pady=(10,0), sticky='w')    
        #Lembrar de fazer o campo preencher a "linha toda"    
        self.campo_desc = ctk.CTkEntry(self,placeholder_text='Descreva a venda')
        self.campo_desc.grid(row=4, column=0, padx=10, pady=10, stick= 'ew', columnspan=3)

    @property
    def obter_dados(self):
        return {
            "data_venda": self.campo_data_venda.get(),
            "OS": self.campo_OS.get(),
            "descricao_venda": self.campo_desc.get()
        }