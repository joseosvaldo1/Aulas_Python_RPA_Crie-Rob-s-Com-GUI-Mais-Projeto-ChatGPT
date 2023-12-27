from tkinter import *

# Tk - é uma biblioteca do Tkinter
# Tk - Janela/tela
window = Tk()
# O método 'title' do Tkinter altera o título da tela.

window.title("Entry")
# O método 'geometry' altera o tamanho inicial da janela.
window.geometry("900x600")


#grid - Divide a tela em grades / parte
#sticky - Usamos para preencher o item na tela toda, ou seja
#para não ficar espaços em branco nas laterais
#sticky - NSEW - (Norte, Sul, Leste e Oeste)
nome = Label(text="Nome: ",
             font="Arial 40")
nome.grid(row=1, column=0, sticky="W")

#Entry - Campo de entrada de dados
exibir_nome = Entry(window, font= "Arial 40")
exibir_nome.grid(row=1, column=1, sticky="W")

# grid - Divide a tela em grades / parte (linhas e colunas).
# sticky - Usamos para preencher o item na tela toda, ou seja
# para não ficar espaços em branco nas laterais
# sticky - NSEW - (Norte-North-N, Sul-South-S, Leste-East-E e Oeste-West-W)
sobrenome = Label(text="Sobrenome: ",
                  font="Arial 40")
sobrenome.grid(row=2, column=0, sticky="W")

# Entry - Campo de entrada de dados.
exibir_sobrenome = Entry(font= "Arial 40")
exibir_sobrenome.grid(row=2, column=1, sticky="W")


# mainloop - No Tkinter, uma janela funciona como # um loop infinito.
# A janela que o Python mostra é, na verdade, um programa ,em
# funcionamento.
window.mainloop()