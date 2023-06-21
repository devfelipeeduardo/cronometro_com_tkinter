from tkinter import *
from time import sleep

#CORES
cor1 = "#0a0a0a"  # black
cor2 = "#fafcff"  # white
cor3 = "#21c25c"  # green
cor4 = "#eb463b"  # red
cor5 = "#dedcdc"  # gray
cor6 = "#3080f0"  # blue


#PADRÃO TKINTER
janela = Tk()
janela.title()
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)


#FUNÇÕES

global tempo
global rodar
global contador
global limitador
global rodando

tempo = '00:00:00'
rodar = False
contador = -5
limitador = 59
rodando = False

def iniciar():

    global tempo
    global contador
    global limitador

    if rodar == True:
        
        #Aviso de quando o cronômetro inicia
        if contador <= -1:
            inicio = 'Começando em: ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = ('Arial 10')

        #Rodando o cronômetro
        else:

            label_tempo['font'] = ('Times 50 bold')           
            temporaria = tempo
            hora, minuto, segundo = map(int, temporaria.split(':'))
            segundo = contador

            if (segundo >= limitador):
                contador = 0
                minuto += 1
            
            segundo = str(0)+str(segundo)
            minuto = str(0)+str(minuto)
            hora = str(0)+str(hora)
        
            #Atualizador de valores
            temporaria = str(hora[-2:])+ ':' + str(minuto[-2:])+ ':' + str(segundo[-2:])
            label_tempo['text'] = temporaria
            tempo = temporaria

        
        label_tempo.after(1000, iniciar)
        contador += 1

#DESABILITA E HABILITA INICIAR
def habilitar_iniciar():
    botao_iniciar.config(state=NORMAL)
    sleep(1)
def desabilitar_iniciar():
    botao_iniciar.config(state=DISABLED)

#DESABILITA E HABILITA PAUSAR
def habilitar_pausar():
    botao_pausar.config(state=NORMAL)
    sleep(1)
def desabilitar_pausar():
    botao_pausar.config(state=DISABLED)


def alterar_estado_iniciar():
    global rodar
    desabilitar_iniciar()
    habilitar_pausar()
    rodar = True
    iniciar()


def pausar():
    global rodar
    rodar = False
    habilitar_iniciar()
    desabilitar_pausar()

def reiniciar():
    global contador
    global tempo
    contador = -5 
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    label_tempo['font'] = ('Times 50 bold') 
    desabilitar_pausar()
    sleep(1)
    habilitar_iniciar()

#CRONÔMETRO E TEMPO

#Cronômetro
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

#Tempo
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)


#BOTÕES

#Iniciar
botao_iniciar = Button(janela, command=alterar_estado_iniciar, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

#Pausar
botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

#Reiniciar  
botao_reiniciar = Button(janela, command=reiniciar,text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)



janela.mainloop()