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
        self.campo_desc.grid(row=4, column=0, padx=10, pady=(10,0),sticky= 'e')

class FormFrame(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Formulario')

        self.InfoVenda = InfoVenda(self)
        self.InfoVenda.grid(row=0, column=0, padx=1, pady= (10,0),sticky= 'nsw')


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
        self.FormFrame.grid(row=0, column=0, padx=1, pady= (10,0),sticky= 'nsw')

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