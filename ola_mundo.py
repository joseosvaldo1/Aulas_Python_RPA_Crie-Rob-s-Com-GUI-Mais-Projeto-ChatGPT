# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 09:48:37 2023

@author: 02501445309
"""

from tkinter import Tk, Label


# Tk - é uma biblioteca do Tkinter

# Tk - Janela/tela
window = Tk()

# O método 'title' do Tkinter altera o título da tela.
window.title("Interface Gráfica")

# O método 'geometry' altera o tamanho inicial da janela.
window.geometry("600x600")

# O método 'label' permite a inclusão de textos na janela.

# Label é onde escrevermos os textos que queremos que o usuário leia.
instrucao = Label(text="Olá, Mundo", font="Arial 40")
instrucao_2 = Label(text="Curso de Tkinter!", font="Arial 30")

# O método 'pack' coloca os objetos dentro da janela/tela.
# O pack cria, entraliza e deixa um elemento abaixo do outro.
instrucao.pack()
instrucao_2.pack()

# mainloop - No Tkinter, uma janela funciona como 
# um loop infinito. A janela que o Python mostra
# é,na verdade, um programa em funcionamento. """
window.mainloop()
