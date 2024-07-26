# Importando tkinter
from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#3b3b3b"  # preta
cor2 = "#feffff"  # white/Branco
cor3 = "#38576b"  # Blue/azul
cor4 = "#ECEFF1"  # Gray/cinza
cor5 = "#FFAB40"  # Orange/laranja

# Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Frame
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável todos valores
todos_valores = ''

# Criando função para entrar valores
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

# Função para calcular
def calcular():
    global todos_valores
    try:
        # Substituir operações de porcentagem na expressão
        todos_valores = todos_valores.replace('%', '/100')
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ""

# Função para limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_2.place(x=119, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_4.place(x=0, y=51)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_5.place(x=60, y=51)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_6.place(x=120, y=51)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_7.place(x=177, y=51)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_8.place(x=0, y=103)

b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_9.place(x=60, y=103)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_10.place(x=120, y=103)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_11.place(x=177, y=103)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_12.place(x=0, y=155)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_13.place(x=60, y=155)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_14.place(x=120, y=155)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_15.place(x=177, y=155)

b_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_16.place(x=0, y=207)

b_17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_17.place(x=60, y=207)

b_18 = Button(frame_corpo, command=calcular, text="=", width=11, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RAISED)
b_18.place(x=120, y=207)

janela.mainloop()
