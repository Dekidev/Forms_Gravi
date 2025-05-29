import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Gravi Forms')
app.geometry('1280x720')


frame_detalhes_venda = ctk.CTkFrame(app, width=1000, height=500, border_width=2) # Cria o frame dentro da sua janela/widget principal 'app'
frame_detalhes_venda.pack(anchor= 'nw', pady=10, padx=10, expand= True) # Posiciona o frame

# Título para a seção (opcional, mas recomendado)
label_titulo_detalhes = ctk.CTkLabel(frame_detalhes_venda, text="Detalhes da Venda", font=("Arial", 16, "bold"))
label_titulo_detalhes.pack(pady=(5,10)) # Adiciona um pouco de espaço abaixo do título

# Data Venda
label_data_venda = ctk.CTkLabel(frame_detalhes_venda, text='Data Venda:') # Adiciona ao frame_detalhes_venda
label_data_venda.pack(anchor="w", padx=5, expand= True) # 'anchor="w"' alinha o label à esquerda
campo_data_venda = ctk.CTkEntry(frame_detalhes_venda, placeholder_text='Digite a Data da venda') # Adiciona ao frame_detalhes_venda
campo_data_venda.pack(fill="x", padx=5, pady=(0,5)) # 'fill="x"' faz o campo preencher a largura

# OS
label_OS = ctk.CTkLabel(frame_detalhes_venda, text='Ordem de Serviço:') # Adiciona ao frame_detalhes_venda
label_OS.pack(anchor="w", padx=5)
campo_OS = ctk.CTkEntry(frame_detalhes_venda, placeholder_text='Digite a OS') # Adiciona ao frame_detalhes_venda
campo_OS.pack(fill="x", padx=5, pady=(0,5))

# Desc
label_desc = ctk.CTkLabel(frame_detalhes_venda, text='Descrição:') # Adiciona ao frame_detalhes_venda
label_desc.pack(anchor="w", padx=5)
campo_desc = ctk.CTkEntry(frame_detalhes_venda, placeholder_text='Descreva a venda') # Adiciona ao frame_detalhes_venda
campo_desc.pack(fill="x", padx=5, pady=(0,10)) # Adiciona um pouco mais de pady no final do grupo

# --- Aqui continuaria o restante do seu formulário, que ficaria visualmente separado ---
# Exemplo:
# frame_outra_secao = ctk.CTkFrame(app)
# frame_outra_secao.pack(pady=10, padx=10, fill="x", expand=False)
# label_outra_coisa = ctk.CTkLabel(frame_outra_secao, text="Outra Seção")
# label_outra_coisa.pack()

frame_pg = ctk.CTkFrame(app, width=100, height=500, border_width=2)
frame_pg.pack(anchor= 'nw', pady=10, padx=10, expand= True)

label_pg = ctk.CTkLabel(frame_pg, text="Detalhes de Pagamento", font=("Arial", 16, "bold"))
label_pg.pack(pady=(5,10)) # Adiciona um pouco de espaço abaixo do título

label_bruto = ctk.CTkLabel(frame_pg, text= 'Valor Bruto')
label_bruto.pack(anchor= 'w', padx=5)
campo_bruto = ctk.CTkEntry(frame_pg, placeholder_text='Digite o valor bruto')
campo_bruto.pack(anchor = 'w', padx=5, pady=(0,10))



app.mainloop()