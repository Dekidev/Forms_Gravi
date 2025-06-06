import customtkinter as ctk
from Formularios.form_frame import FormFrame

class ResultFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, form_frame_instance):  
        super().__init__(master)
        self.forms = form_frame_instance
        #self.forms = FormFrame()
        

        super().__init__(master) #colocar f e {} para variaveis
        self.label_forms = ctk.CTkLabel(self, text= 'Preencha o formulário e clique no botão "Gerar"', anchor='w', justify= 'left')
        self.label_forms.grid(row=0, column=0, padx=10, pady= 10, sticky= 'nw')


    def get_forms_atualizado(self):
        data_info_venda = self.forms.InfoVenda.obter_dados   
        data_valor_venda = self.forms.ValorVenda.obter_dados
        data_pagamento = self.forms.Pagamento.obter_dados
        data_longe = self.forms.Longe.obter_dados
        data_perto = self.forms.Perto.obter_dados
        data_receita = self.forms.Receita.obter_dados
        data_arm_longe = self.forms.Info_arm_longe.obter_dados
        data_arm_perto = self.forms.Info_arm_perto.obter_dados
        data_arm_multi = self.forms.Info_arm_multi.obter_dados
        return f'''* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
-----------------------------
¦  DATA VENDA  ¦ {data_info_venda['data_venda']}
-----------------------------
¦         O. S.          ¦  {data_info_venda['OS']}
-----------------------------
¦   DESCRIÇÃO   ¦  {data_info_venda['descricao_venda']}
-----------------------------
===================================================
-----------------------------
¦    VLR BRUTO   ¦ R$ {data_valor_venda['valor_bruto']}
-----------------------------
¦   DESCONTO     ¦ R$ {data_valor_venda['desconto']}
-----------------------------
¦    VLR TOTAL    ¦ R$ {data_valor_venda['valor_total']}
============================================================================
¦     D A T A      ¦    DISCRIMINAÇÃO  ¦     Vlr (R$)    ¦      SALDO     ¦ 
=============================================================================
{data_pagamento['data_pagamento']}   | {data_pagamento['forma_pagamento']}  |  {data_pagamento['valor_pago']}  |{data_pagamento['saldo']}

---------------------------------
¦  DATA RECEITA   ¦   {data_receita['data_receita']}
--------------------------------
¦        MEDICO         ¦ {data_receita['medico']} | CRM: {data_receita['CRM']}
---------------------------------
***********************
*     L O N G E       *
***********************
-------------------------------------------------------------------------------- 
¦                  ¦      ESF    ¦    CIL    ¦     EIXO   ¦    DNP    
--------------------------------------------------------------------------------
¦     O.D.     ¦ {data_longe['OD_esf']}   |   {data_longe['OD_cil']}   |   {data_longe['OD_eix']}   |   {data_longe['OD_dnp']}
--------------------------------------------------------------------------------
¦     O.E.     ¦ {data_longe['OE_esf']}   |   {data_longe['OE_cil']}   |   {data_longe['OE_eix']}   |   {data_longe['OE_dnp']}
-----------------------------------------------------------------------------------
¦ 
----------------------------------------------------------------------------------
¦  ALTURA ¦  MATERIAL  ¦   COR/TRATAMENTO   ¦
----------------------------------------------------------------------------------
¦{data_arm_longe['altura']}  |   {data_arm_longe['material']}  |  {data_arm_longe['tratamento']}
------------------------------------------------------------------------------------
--------------------------------
¦       ARMAÇÃO      ¦ {data_arm_longe['armacao']}
---------------------------------
¦     CÓDIGO ARM   ¦ {data_arm_longe['codigo']}
---------------------------------
==================================================
***********************
*     P E R T O       *
***********************
-------------------------------------------------------------------------------- 
¦                  ¦      ESF    ¦    CIL    ¦     EIXO   ¦    DNP    
--------------------------------------------------------------------------------
¦     O.D.     ¦ {data_perto['OD_esf']}   |   {data_perto['OD_cil']}   |   {data_perto['OD_eix']}   |   {data_perto['OD_dnp']}
--------------------------------------------------------------------------------
¦     O.E.     ¦ {data_perto['OE_esf']}   |   {data_perto['OE_cil']}   |   {data_perto['OE_eix']}   |   {data_perto['OE_dnp']}
-----------------------------------------------------------------------------------
¦ 
----------------------------------------------------------------------------------
¦  ALTURA ¦  MATERIAL  ¦   COR/TRATAMENTO   ¦
----------------------------------------------------------------------------------
¦{data_arm_perto['altura']}  |   {data_arm_perto['material']}  |  {data_arm_perto['tratamento']}
------------------------------------------------------------------------------------
--------------------------------
¦       ARMAÇÃO      ¦ {data_arm_perto['armacao']}
---------------------------------
¦     CÓDIGO ARM   ¦ {data_arm_perto['codigo']}
---------------------------------
==================================================

**************************************
¦    MULTIFOCAL/BIFOCAL      ¦
**************************************
¦  
---------------------------------
¦        ADIÇÃO         ¦ {data_longe['OD_adc']} | {data_longe['OE_adc']}
---------------------------------
¦ 
----------------------------------------------------------------------------------
¦  ALTURA ¦  MATERIAL  ¦   COR/TRATAMENTO   ¦
----------------------------------------------------------------------------------
¦{data_arm_multi['altura']}  |   {data_arm_multi['material']}  |  {data_arm_multi['tratamento']}
------------------------------------------------------------------------------------
--------------------------------
¦       ARMAÇÃO      ¦ {data_arm_multi['armacao']}
---------------------------------
¦     CÓDIGO ARM   ¦ {data_arm_multi['codigo']}
---------------------------------
==================================================
---------------------------------
¦  DATA ENTREGA ¦   
---------------------------------
=================================================='''

    def atualizar_valores(self):
        self.label_forms.configure(text= self.get_forms_atualizado() , anchor='w', justify= 'left')
            

        
