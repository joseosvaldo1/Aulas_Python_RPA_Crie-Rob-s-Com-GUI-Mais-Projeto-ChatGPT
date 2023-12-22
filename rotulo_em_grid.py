# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:42:56 2023

@author: 02501445309
"""
from tkinter import Tk, Label, Frame

# Tk - é uma biblioteca do Tkinter

# Tk - Janela/tela
window = Tk()

# O método 'title' do Tkinter altera o título da tela.
window.title("Interface Gráfica")

# O método 'geometry' altera o tamanho inicial da janela.
window.geometry("300x300")

# For - para - estrutura de repetição:
for linha in range(5):
    for coluna in range(3):
        # master - mestre - representa a janela pai
        table = Frame(
            master = window,
            relief = "sunken",
            borderwidth = 1 
            )
        table.grid(row=linha, column=coluna, padx=5, pady=5)
        criaLabel = Label(master=table, text=f"Linha {linha} \n Colinha {coluna}")
        criaLabel.pack()
        
window.mainloop()