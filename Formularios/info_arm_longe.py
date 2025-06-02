import customtkinter as ctk

class InfoArmLonge(ctk.CTkFrame):
    def __init__(self, master):  
        super().__init__(master)
        self.checkbox_titulo = ctk.CTkCheckBox(self, text='Longe')
        self.checkbox_titulo.grid(row=0, column= 0, padx= 10, pady=(10,0), columnspan= 2)

        self.label_alt = ctk.CTkLabel(self, text='Altura')
        self.label_alt.grid(row=1, column=0, padx=10, pady=10)
        self.campo_alt = ctk.CTkEntry(self, width=40)
        self.campo_alt.grid(row=2, column=0, padx=10, pady=10)

        self.label_material = ctk.CTkLabel(self, text='Material')
        self.label_material.grid(row=1, column=1, padx=10, pady=10)
        self.campo_material = ctk.CTkEntry(self, width=40)
        self.campo_material.grid(row=2, column=1, padx=10, pady=10)

        self.label_trat = ctk.CTkLabel(self, text='Cor/Tratamento')
        self.label_trat.grid(row=1, column=2, padx=10, pady=10)
        self.campo_trat = ctk.CTkEntry(self, width=100)
        self.campo_trat.grid(row=2, column=2, padx=10, pady=10)

        
        self.label_ARM = ctk.CTkLabel(self, text='Armação:')
        self.label_ARM.grid(row=3, column=0, padx=10, pady=10)
        self.campo_ARM = ctk.CTkEntry(self)
        self.campo_ARM.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        self.label_COD = ctk.CTkLabel(self, text='Código:')
        self.label_COD.grid(row=4, column=0, padx=10, pady=10)
        self.campo_COD = ctk.CTkEntry(self)
        self.campo_COD.grid(row=4, column=1, padx=10, pady=10, columnspan=2)