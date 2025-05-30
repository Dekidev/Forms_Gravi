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

class Longe(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Longe')
        self.label_titulo.grid(row=0, column= 0, padx= 10, pady=(10,0))

        self.label_ESF = ctk.CTkLabel(self, text='Esférico')
        self.label_ESF.grid(row=1, column=1, padx= 10, pady=(10,0))
        self.label_CIL = ctk.CTkLabel(self, text='Cilindrico')
        self.label_CIL.grid(row=1, column=2, padx= 10, pady=(10,0))
        self.label_EIX = ctk.CTkLabel(self, text='Eixo')
        self.label_EIX.grid(row=1, column=3, padx= 10, pady=(10,0))
        self.label_DNP = ctk.CTkLabel(self, text='DNP')
        self.label_DNP.grid(row=1, column=4, padx= 10, pady=(10,0))

        self.label_OD = ctk.CTkLabel(self, text='OD:')
        self.label_OD.grid(row=2, column=0, padx= 10, pady=(10,0))
        self.campo_ESF_OD = ctk.CTkEntry(self)
        self.campo_ESF_OD.grid(row=2, column=1, padx= 10, pady=10)
        self.campo_CIL_OD = ctk.CTkEntry(self)
        self.campo_CIL_OD.grid(row=2, column=2, padx= 10, pady=10)
        self.campo_EIX_OD = ctk.CTkEntry(self)
        self.campo_EIX_OD.grid(row=2, column=3, padx= 10, pady=10)
        self.campo_DNP_OD = ctk.CTkEntry(self)
        self.campo_DNP_OD.grid(row=2, column=4, padx= 10, pady=10)

        self.label_OE = ctk.CTkLabel(self, text='OE')
        self.label_OE.grid(row=3, column=0, padx= 10, pady=(10,0))
        self.campo_ESF_OE = ctk.CTkEntry(self)
        self.campo_ESF_OE.grid(row=3, column=1, padx= 10, pady=10)
        self.campo_CIL_OE = ctk.CTkEntry(self)
        self.campo_CIL_OE.grid(row=3, column=2, padx= 10, pady=10)
        self.campo_EIX_OE = ctk.CTkEntry(self)
        self.campo_EIX_OE.grid(row=3, column=3, padx= 10, pady=10)
        self.campo_DNP_OE = ctk.CTkEntry(self)
        self.campo_DNP_OE.grid(row=3, column=4, padx= 10, pady=10)



class FormFrame(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Formulario', font=('arial bold',20))
        self.label_titulo.grid(row=0, columnspan= 3, padx=10, pady= 10, sticky= 'ew')

        self.InfoVenda = InfoVenda(self)
        self.InfoVenda.grid(row=1, column=0, padx=10, pady= 10,sticky= 'nsw')

        self.ValorVenda = ValorVenda(self)
        self.ValorVenda.grid(row=1, column=1, padx=10, pady=10,sticky='ns')

        self.Pagamento = Pagamento(self)
        self.Pagamento.grid(row=1,column=2, padx=10, pady=10,sticky='nse')

        self.label_titulo =  ctk.CTkLabel(self, text='Receita', font=('arial bold',20))
        self.label_titulo.grid(row=3, columnspan=3, padx=10, pady=10, sticky='ew')

        self.Receita = Receita(self)
        self.Receita.grid(row=4, column=0, padx=10, pady=10,sticky='nsw')

        self.Longe = Longe(self)
        self.Longe.grid(row=4, column=1, padx=10, pady=10, sticky= 'nse')
        
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