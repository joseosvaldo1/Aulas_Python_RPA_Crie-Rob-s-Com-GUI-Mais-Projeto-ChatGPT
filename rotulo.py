# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:59:02 2023

@author: 02501445309
"""

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
window.geometry("850x850")

# O método 'label' permite a inclusão de textos na janela.

# Label é onde escrevermos os textos que queremos que o usuário leia.
# Background - bg - Cor do Fundo.
# Foreground - fg - Cor do Texto.
# Relief - Relevo - borda decorativa  
rotulo_1 = Label(window, text="FLAT",relief="flat", background="green", foreground="white", font="Arial 40")
rotulo_2 = Label(window, text="RAISED",relief="raised", background="blue", foreground="white", font="Arial 40")
rotulo_3 = Label(window, text="SUNKEN",relief="sunken", background="white", foreground="black", font="Arial 40")
rotulo_4 = Label(window, text="GROOVE",relief="groove", background="black", foreground="white", font="Arial 40")
#rotulo_5 = Label(window, text="SOLID",relief="solid", background="orange", foreground="white", font="Arial 40")
#rotulo_6 = Label(window, text="RIDGE",relief="ridge", background="purple", foreground="white", font="Arial 40")

# O método 'pack' coloca os objetos dentro da janela/tela.
# O pack cria, entraliza e deixa um elemento abaixo do outro.
rotulo_1.pack()
rotulo_2.pack()
rotulo_3.pack()
rotulo_4.pack()
#rotulo_5.pack()
#rotulo_6.pack()


texto = """Curso de Tkinter
Aprendendo como criar 
Interface Gráfica com
Python"""

rotulo_7 = Label(window,
                 font="Arial 40 bold",
                 text=texto,
                 )

rotulo_7.pack()



# mainloop - No Tkinter, uma janela funciona como 
# um loop infinito. A janela que o Python mostra
# é,na verdade, um programa em funcionamento. """
window.mainloop()