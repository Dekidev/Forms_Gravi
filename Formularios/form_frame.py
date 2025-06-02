import customtkinter as ctk
from Formularios.info_venda import InfoVenda 
from Formularios.valor_venda import ValorVenda
from Formularios.pagamentos import Pagamento
from Formularios.receita import Receita
from Formularios.longe import Longe
from Formularios.perto import Perto
from Formularios.info_arm_longe import InfoArmLonge
from Formularios.info_arm_perto import InfoArmPerto
from Formularios.info_arm_multi import InfoArmMulti

class FormFrame(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Formulario', font=('arial bold',20))
        self.label_titulo.grid(row=0, columnspan= 2, padx=10, pady= 10, sticky= 'ew')

        self.InfoVenda = InfoVenda(self)
        self.InfoVenda.grid(row=1, column=0, padx=5, pady= 10,sticky= 'nsw')

        self.ValorVenda = ValorVenda(self)
        self.ValorVenda.grid(row=1, column=1, padx=5, pady=10, sticky= 'nsw')

        self.Pagamento = Pagamento(self)
        self.Pagamento.grid(row=1,column=2, padx=5, pady=10, sticky='nsw')

        self.label_titulo =  ctk.CTkLabel(self, text='Receita', font=('arial bold',20))
        self.label_titulo.grid(row=3, columnspan=2, padx=10, pady=10, sticky='ew')

        self.Receita = Receita(self)
        self.Receita.grid(row=4, column=2, padx=5, pady=10,sticky='nswe')

        self.Longe = Longe(self)
        self.Longe.grid(row=4, column=0, padx=5, pady=10, sticky= 'ew')

        self.Perto = Perto(self)
        self.Perto.grid(row=4, column= 1, padx=5, pady=10, sticky='ns')

        self.Info_arm_longe = InfoArmLonge(self)
        self.Info_arm_longe.grid(row=5, column=0, padx=5, pady= 10, sticky= 'ew')

        self.Info_arm_perto = InfoArmPerto(self)
        self.Info_arm_perto.grid(row=5, column=1, padx=5, pady= 10, sticky= 'ew')
                
        self.Info_arm_multi = InfoArmMulti(self)
        self.Info_arm_multi.grid(row=5, column=2, padx=5, pady= 10, sticky= 'ew')
    