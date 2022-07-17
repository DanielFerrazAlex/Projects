from tkinter import *
from tkinter import ttk

cor1 = '#3b3b3b'
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#eceff1'
cor5 = '#fa6a02'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

all_valor = ''
valor_texto = StringVar()

def entrar_valor(event):
    global all_valor
    all_valor = all_valor + str(event)
    valor_texto.set(all_valor)
    
def operacao():
    global all_valor
    resultado = eval(all_valor)
    valor_texto = str (resultado)

def deletar_tela():
    global all_valor
    all_valor = ''
    valor_texto.set('')

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

tecla_1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=deletar_tela)
tecla_1.place(x=0, y=0)

tecla_2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('%'))
tecla_2.place(x=120, y=0)

tecla_3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('/'))
tecla_3.place(x=180, y=0)

tecla_4 = Button(frame_corpo, text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('7'))
tecla_4.place(x=0, y=52)

tecla_5 = Button(frame_corpo, text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('8'))
tecla_5.place(x=60, y=52)

tecla_6 = Button(frame_corpo, text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('9'))
tecla_6.place(x=120, y=52)

tecla_7 = Button(frame_corpo, text='*', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('*'))
tecla_7.place(x=180, y=52)

tecla_8 = Button(frame_corpo, text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('4'))
tecla_8.place(x=0, y=104)

tecla_9 = Button(frame_corpo, text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('5'))
tecla_9.place(x=60, y=104)

tecla_10 = Button(frame_corpo, text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('6'))
tecla_10.place(x=120, y=104)

tecla_11 = Button(frame_corpo, text='-', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('-'))
tecla_11.place(x=180, y=104)

tecla_12 = Button(frame_corpo, text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('1'))
tecla_12.place(x=0, y=156)

tecla_13 = Button(frame_corpo, text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('2'))
tecla_13.place(x=60, y=156)

tecla_14 = Button(frame_corpo, text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('3'))
tecla_14.place(x=120, y=156)

tecla_15 = Button(frame_corpo, text='+', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('+'))
tecla_15.place(x=180, y=156)

tecla_16 = Button(frame_corpo, text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('0'))
tecla_16.place(x=0, y=208)

tecla_17 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('.'))
tecla_17.place(x=120, y=208)

tecla_18 = Button(frame_corpo, text='7', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=operacao)
tecla_18.place(x=180, y=208)

janela.mainloop()