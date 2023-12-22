# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:35:07 2023

@author: 02501445309
"""


from tkinter import Tk, Button, messagebox


# Tk - é uma biblioteca do Tkinter

# Tk - Janela/tela
window = Tk()

# O método 'title' do Tkinter altera o título da tela.
window.title("Interface Gráfica - Button")
    

#Método para exibir mensagem do botão olá mundo:
def exibir_mensagem():
    messagebox.showinfo("Mensagem", "Olá, Mundo!")
    
  

# O método 'button' cria botões para interação.
button = Button(window,text="Enviar", font="Arial 40" )

button_ola_mundo = Button(window,
                          text = "Mensagem", 
                          font = "Arial 40",
                          command = exibir_mensagem)

button_sair = Button(window,
                     text = "Sair", 
                     font = "Arial 40",
                     command = window.destroy) # => window.destroy fecha a 
                                               # janela criada pelo Tkinter 

button_green = Button(window, 
                      text = "VERDE",
                      font = "Arial 40", # Muda a fonte e o tamanho da letra
                      bg = "green",    # Define a cor de fundo do botão
                      fg = "white")     # Define a cor da letra do botão
button_yellow = Button(window,
                       text = "AMARELO",
                       font = "Arial 40", # Muda a fonte e o tamanho da letra
                       bg = "yellow",     # Define a cor de fundo do botão
                       fg = "white")      # Define a cor da letra do botão 


# O método 'pack' coloca os objetos dentro da janela/tela.
# O pack cria, entraliza e deixa um elemento abaixo do outro
button.pack()
button_ola_mundo.pack()
button_sair.pack()
button_green.pack() 
button_yellow.pack()

# O método 'geometry' altera o tamanho inicial da janela.
window.geometry("600x600")



# mainloop - No Tkinter, uma janela funciona como 
# um loop infinito. A janela que o Python mostra
# é,na verdade, um programa em funcionamento. 
window.mainloop()