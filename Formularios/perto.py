import customtkinter as ctk

class Perto(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.label_titulo = ctk.CTkLabel(self, text='Perto')
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
        self.campo_ESF_OD = ctk.CTkEntry(self, width=50)
        self.campo_ESF_OD.grid(row=2, column=1, padx= 10, pady=10)
        self.campo_CIL_OD = ctk.CTkEntry(self, width=50)
        self.campo_CIL_OD.grid(row=2, column=2, padx= 10, pady=10)
        self.campo_EIX_OD = ctk.CTkEntry(self, width=40)
        self.campo_EIX_OD.grid(row=2, column=3, padx= 10, pady=10)
        self.campo_DNP_OD = ctk.CTkEntry(self, width=40)
        self.campo_DNP_OD.grid(row=2, column=4, padx= 10, pady=10)

        self.label_OE = ctk.CTkLabel(self, text='OE')
        self.label_OE.grid(row=3, column=0, padx= 10, pady=(10,0))
        self.campo_ESF_OE = ctk.CTkEntry(self, width=50)
        self.campo_ESF_OE.grid(row=3, column=1, padx= 10, pady=10)
        self.campo_CIL_OE = ctk.CTkEntry(self, width=50)
        self.campo_CIL_OE.grid(row=3, column=2, padx= 10, pady=10)
        self.campo_EIX_OE = ctk.CTkEntry(self, width=40)
        self.campo_EIX_OE.grid(row=3, column=3, padx= 10, pady=10)
        self.campo_DNP_OE = ctk.CTkEntry(self, width=40)
        self.campo_DNP_OE.grid(row=3, column=4, padx= 10, pady=10)