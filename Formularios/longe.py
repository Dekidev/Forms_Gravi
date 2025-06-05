import customtkinter as ctk

class Longe(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Longe', font=('arial bold',14))
        self.label_titulo.grid(row=0, column= 0, padx= 10, pady=(10,0))

        self.label_ESF = ctk.CTkLabel(self, text='Esférico')
        self.label_ESF.grid(row=1, column=1, padx= 10, pady=(10,0))
        self.label_CIL = ctk.CTkLabel(self, text='Cilindrico')
        self.label_CIL.grid(row=1, column=2, padx= 10, pady=(10,0))
        self.label_EIX = ctk.CTkLabel(self, text='Eixo')
        self.label_EIX.grid(row=1, column=3, padx= 10, pady=(10,0))
        self.label_DNP = ctk.CTkLabel(self, text='DNP')
        self.label_DNP.grid(row=1, column=4, padx= 10, pady=(10,0))

        self.label_OD = ctk.CTkLabel(self, text='O.D.:')
        self.label_OD.grid(row=2, column=0, padx= 10, pady=(10,0))
        self.campo_ESF_OD = ctk.CTkEntry(self, width=50)
        self.campo_ESF_OD.grid(row=2, column=1, padx= 10, pady=10)
        self.campo_CIL_OD = ctk.CTkEntry(self, width=50)
        self.campo_CIL_OD.grid(row=2, column=2, padx= 10, pady=10)
        self.campo_EIX_OD = ctk.CTkEntry(self, width=40)
        self.campo_EIX_OD.grid(row=2, column=3, padx= 10, pady=10)
        self.campo_DNP_OD = ctk.CTkEntry(self, width=40)
        self.campo_DNP_OD.grid(row=2, column=4, padx= 10, pady=10)

        self.label_OE = ctk.CTkLabel(self, text='O.E.:')
        self.label_OE.grid(row=3, column=0, padx= 10, pady=(10,0))
        self.campo_ESF_OE = ctk.CTkEntry(self, width=50)
        self.campo_ESF_OE.grid(row=3, column=1, padx= 10, pady=10)
        self.campo_CIL_OE = ctk.CTkEntry(self, width=50)
        self.campo_CIL_OE.grid(row=3, column=2, padx= 10, pady=10)
        self.campo_EIX_OE = ctk.CTkEntry(self, width=40)
        self.campo_EIX_OE.grid(row=3, column=3, padx= 10, pady=10)
        self.campo_DNP_OE = ctk.CTkEntry(self, width=40)
        self.campo_DNP_OE.grid(row=3, column=4, padx= 10, pady=10)

        self.label_ADC = ctk.CTkLabel(self, text='Adição:')
        self.label_ADC.grid(row=4, column=0, padx=10, pady=10)
        self.campo_ADC_OD = ctk.CTkEntry(self,placeholder_text='O.D.', width=40)
        self.campo_ADC_OD.grid(row=4, column=1, padx=10, pady=10)
        self.campo_ADC_OE = ctk.CTkEntry(self, placeholder_text='O.E.', width=40)
        self.campo_ADC_OE.grid(row=4, column=2, padx=10, pady=10)
        self.checkbox_ADC = ctk.CTkCheckBox(self, text='A.O.')
        self.checkbox_ADC.grid(row=4, column=3, padx=10, pady=10, columnspan= 2)

    @property
    def obter_dados(self):
        return {
            "OD_esf": self.campo_ESF_OD.get(),
            "OD_cil": self.campo_CIL_OD.get(),
            "OD_eix": self.campo_EIX_OD.get(),
            "OD_dnp": self.campo_DNP_OD.get(),
            "OE_esf": self.campo_ESF_OE.get(),
            "OE_cil": self.campo_CIL_OE.get(),
            "OE_eix": self.campo_EIX_OE.get(),
            "OE_dnp": self.campo_DNP_OE.get(),
            "OD_adc": self.campo_ADC_OD.get(),
            "OE_adc": self.campo_ADC_OE.get()
        }