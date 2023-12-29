# -*- coding: utf-8 -*-


#from tkinter import *


from tkinter import Tk, Button, StringVar, Entry
import math

# Tk - é uma biblioteca do Tkinter
# Tk - Janela/tela
janela = Tk()


# O método 'title' do Tkinter altera o título da tela.
janela.title("Calculadora")
# O método 'geometry' altera o tamanho inicial da janela.
janela.geometry("338x325")

texto_de_entrada = StringVar()

# Caixa de texto que exibe o resultado e as operações
texto_exibe_operacoes_resultado = Entry (janela,
                                         font=("Arial 20 bold"),
                                         textvariable=texto_de_entrada, # Variável
                                         border=5, # Borda
                                         background="#BBB", # Cor do fundo
                                         foreground="black", # Cor da letra
                                         )
texto_exibe_operacoes_resultado.grid(row=1,columnspan=5,padx=10, pady=15)

calculo_operacoes = " "
def enviar_numero_para(char):

    global calculo_operacoes
    # Com o 'char' que só permite um item, vou adicionando
    # o mesmo ao final de cada ação/operação
    calculo_operacoes += str(char)
    # Usando 'set', estamos colocando todo o texto na variável
    # que está lincado com o campo 'Entry'.
    texto_de_entrada.set(calculo_operacoes)


def deletar_numero():
    global calculo_operacoes

    # Pego o texto do 'Entry' e excluo apenas o último item
    texto_sem_o_ultimo_digito = calculo_operacoes[:-1]

    #Colocando na variáverl o texto da operação sem o último dígito
    calculo_operacoes = texto_sem_o_ultimo_digito
    # Usando 'set', estamos colocando todo o texto na variável
    # que está lincado com o campo 'Entry'.
    texto_de_entrada.set(calculo_operacoes)

def limpar_tudo():

    global calculo_operacoes

    # Apagando o texto da variável integralmente.
    calculo_operacoes = " "

    # Usando 'set', estamos colocando todo o texto na variável
    # que está lincado com o campo 'Entry'.
    texto_de_entrada.set(calculo_operacoes)


def funcao_igual():

    global calculo_operacoes

    # O método 'eval' avalia é um calculo válido e
    # efetua o mesmo.
    resultado_calculo = str(eval(calculo_operacoes))
    # Usando 'set', estamos colocando todo o texto na variável
    # que está lincado com o campo 'Entry'.
    texto_de_entrada.set(resultado_calculo)

    # Mudamos a variável que tinha a operação e colocamos
    # apenas o resultado do cálculo na variável global
    calculo_operacoes = resultado_calculo
    


botao_numero_7 = Button(janela,
                        text="7", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("7"))
# O 'lambda' permite enviar vários dados em uma função.

botao_numero_7.grid(row=2, column=0, sticky="NSEW")

botao_numero_8 = Button(janela,
                        text="8", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("8"))

botao_numero_8.grid(row=2, column=1, sticky="NSEW")

botao_numero_9 = Button(janela,
                        text="9", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("9"))

botao_numero_9.grid(row=2, column=2, sticky="NSEW")

botao_deletar = Button(janela,
                        text="DEL", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#DB701F", # Cor do  Fundo
                        font=("Arial 12 bold"), # Fonte, Tamanho e Estilo
                        command=deletar_numero)
# A função deletar_numero não deve ser chamada diretamente ao configurar
# o comando do botão. Em vez disso, você deve passar a referência da função
# sem os parênteses.

botao_deletar.grid(row=2, column=3, sticky="NSEW")

botao_deletar_tudo = Button(janela,
                        text="AC", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#DB701F", # Cor do  Fundo
                        font=("Arial 12 bold"), # Fonte, Tamanho e Estilo
                        command=limpar_tudo)

botao_deletar_tudo.grid(row=2, column=4, sticky="NSEW")

botao_numero_4 = Button(janela,
                        text="4", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("4"))

botao_numero_4.grid(row=3, column=0, sticky="NSEW")

botao_numero_5 = Button(janela,
                        text="5", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("5"))

botao_numero_5.grid(row=3, column=1, sticky="NSEW")

botao_numero_6 = Button(janela,
                        text="6", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("6"))

botao_numero_6.grid(row=3, column=2, sticky="NSEW")


botao_multiplicacao = Button(janela,
                        text="*", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("*"))

botao_multiplicacao.grid(row=3, column=3, sticky="NSEW")


botao_divisao = Button(janela,
                        text="/", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("/"))

botao_divisao.grid(row=3, column=4, sticky="NSEW")

botao_numero_1 = Button(janela,
                        text="1", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("1"))

botao_numero_1.grid(row=4, column=0, sticky="NSEW")


botao_numero_2 = Button(janela,
                        text="2", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("2"))

botao_numero_2.grid(row=4, column=1, sticky="NSEW")

botao_numero_3 = Button(janela,
                        text="3", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("3"))

botao_numero_3.grid(row=4, column=2, sticky="NSEW")

botao_adicao = Button(janela,
                        text="+", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("+"))

botao_adicao.grid(row=4, column=3, sticky="NSEW")


botao_subtracao = Button(janela,
                        text="-", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("-"))

botao_subtracao.grid(row=4, column=4, sticky="NSEW")


botao_numero_0 = Button(janela,
                        text="0", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("0"))

botao_numero_0.grid(row=5, column=0, sticky="NSEW")

botao_ponto = Button(janela,
                        text=".", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("."))

botao_ponto.grid(row=5, column=1, sticky="NSEW")


botao_exponenciacao= Button(janela,
                        text="y ͯ", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("**"))

# columnspan - indica quantas colunas do grid o item irá ocupar
botao_exponenciacao.grid(row=5, column=1, sticky="NSEW")

botao_mod= Button(janela,
                        text="MOD", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#BBB", # Cor do  Fundo
                        font=("Arial 12 bold"), # Fonte, Tamanho e Estilo
                        command=lambda: enviar_numero_para("%"))

# columnspan - indica quantas colunas do grid o item irá ocupar
botao_mod.grid(row=5, column=2, sticky="NSEW")



botao_igual = Button(janela,
                        text="=", # Texto do Botão
                        border=5, # Borda
                        foreground="black", # Cor da Letra
                        background="#03BB85", # Cor do  Fundo
                        font=("Arial 20 bold"), # Fonte, Tamanho e Estilo
                        command=funcao_igual)

# columnspan - indica quantas colunas do grid o item irá ocupar
botao_igual.grid(row=5, column=3, columnspan=2, sticky="NSEW")





# Stick - Ele estica/preencher as laterais, evitando espaços em branco.
# Stick - NSEW - Norte, Sul, Leste e Oeste
# Grid - Divide a tela em partes.


# mainloop - No Tkinter, uma janela funciona como # um loop infinito.
# A janela que o Python mostra é, na verdade, um programa ,em
# funcionamento.
janela.mainloop()

