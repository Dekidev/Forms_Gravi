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

class Pagamento(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #tester titulos(row=0, sem column)
        self.label_titulo = ctk.CTkLabel(self, text='Insira as informações de pagamento')
        self.label_titulo.grid(row=0,column=0, padx=10, pady=(10,0),sticky='n')

        self.label_data = ctk.CTkLabel(self, text='Data:')
        self.label_data.grid(row=1,column=0, padx=10, pady=(10,0))
        self.campo_data = ctk.CTkEntry(self, placeholder_text='Insira a Data')
        self.campo_data.grid(row=2, column=0, padx=10, pady=(10,0))

        self.label_forma = ctk.CTkLabel(self, text='Forma de Pagamento:')
        self.label_forma.grid(row=1, column=1, padx=10, pady=(10,0))
        self.campo_forma = ctk.CTkEntry(self,placeholder_text='Digite o desconto')
        self.campo_forma.grid(row=2, column=1, padx=10, pady=(10,0))

        self.label_ValorPago = ctk.CTkLabel(self, text='Valor pago:') 
        self.label_ValorPago.grid(row=1,column=2, padx=10, pady=(10,0))    
        self.campo_ValorPago = ctk.CTkEntry(self,placeholder_text='Digite valor pago')
        self.campo_ValorPago.grid(row=2, column=2, padx=10, pady=(10,0))

        self.label_saldo = ctk.CTkLabel(self, text='Saldo:') 
        self.label_saldo.grid(row=1,column=3, padx=10, pady=(10,0))    
        self.campo_saldo = ctk.CTkEntry(self,placeholder_text='Digite o saldo')
        self.campo_saldo.grid(row=2, column=3, padx=10, pady=(10,0))

class FormFrame(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Formulario')
        self.label_titulo.grid(row=0,column=0,padx=10, pady= 10,sticky= 'nsw', columnspan=2)

        self.InfoVenda = InfoVenda(self)
        self.InfoVenda.grid(row=1, column=0, padx=10, pady= 10,sticky= 'nsw')

        self.ValorVenda = ValorVenda(self)
        self.ValorVenda.grid(row=1, column=1, padx=10, pady=10,sticky='nsw')

        self.Pagamento = Pagamento(self)
        self.Pagamento.grid(row=2,columnspan=2, padx=10, pady=10,sticky='nsw')
        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        app = ctk.CTk()
        self.title('Gravi Forms')
        self.geometry('1600x900')
        self.grid_columnconfigure(0, weight= 1)
        self.grid_rowconfigure(0, weight=1)

        self.FormFrame = FormFrame(self)
        self.FormFrame.grid(row=0, column=0, padx=10, pady= (10,0),sticky= 'nsw')

        btn_enviar = ctk.CTkButton(self, text='Enviar')
        btn_enviar.grid(row= 3, column= 0, padx=10, pady= 10, sticky= 'ew')

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