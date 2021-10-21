import tkinter as tk
from tkinter import *

#CORES
c1 = '#ffffff' #branco
c2 = '#000000' #preto
c3 = '#4deb60' #lima


#CRIA A TELA E SEU TÍTULO DE JANELA
window = tk.Tk()
window.title('Calculadora de Viagens')
window.geometry('300x285')
window.configure(bg=c1)

#DIVIDINDO A TELA EM DUAS WIDE FRAMES
up_frame_window = Frame(window, width=300, height=50, bg=c1, pady=0, padx=0, relief='flat')
up_frame_window.grid(row=0, column=0, sticky=NSEW)

down_frame_window = Frame(window, width=300, height=235, bg=c1, pady=0, padx=0, relief='flat')
down_frame_window.grid(row=1, column=0, sticky=NSEW)

# FRAME DE CIMA
#TITULO DENTRO DA JANELA
app_name = Label(up_frame_window, text='Calculadora de Viagem', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 16 bold'), bg=c1, fg=c2)
app_name.place(x=0, y=0)

app_line = Label(up_frame_window, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 1'), bg=c3, fg=c2)
app_line.place(x=0, y=35)

# FUNÇÃO PARA CALCULAR VALOR GASTO TOTAL E QUANTOS LITROS
def kmCalculator():
    km = float(km_input.get())
    auto = float(auto_input.get())
    price = float(price_input.get())

    litros = km/auto
    total_price = litros*price
    
    result_km_line['text'] = 'Você gastará R${:.2f}'.format(total_price)
    
    result_line['text'] = "{:.{}f}".format(litros, 2)


# FRAME DE BAIXO
#QUILOMETRAGEM TEXT
km_line = Label(down_frame_window, text='KM da viagem', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=c1, fg=c2)
km_line.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

km_input = Entry(down_frame_window, width=5, relief='solid', font=('Raleway 10 bold'), justify='center')
km_input.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)



#PREÇO DA GASOLINA
price_line = Label(down_frame_window, text='Preço da gasolina', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=c1, fg=c2)
price_line.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

price_input = Entry(down_frame_window, width=5, relief='solid', font=('Raleway 10 bold'), justify='center')
price_input.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


#AUTONOMIA DO VEÍCULO
auto_line = Label(down_frame_window, text='KM por Litro', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=c1, fg=c2)
auto_line.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)

auto_input = Entry(down_frame_window, width=5, relief='solid', font=('Raleway 10 bold'), justify='center')
auto_input.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

#QUANTOS LITROS SERÁ NECESSÁRIO
result_line = Label(down_frame_window, text='Litros', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Raleway 20 bold'), bg=c3, fg=c1)
result_line.place(x=184, y=35)

#VALOR À SER PAGO
result_km_line = Label(down_frame_window, text='Valor gasto', width=37, height=0, padx=0, pady=0, relief='flat', anchor='center', font=('Raleway 10 bold'),bg=c1, fg=c2)
result_km_line.place(x=0, y=140)


#BOTÃO DE CALCULO
result_button = Button(down_frame_window, command=kmCalculator, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Raleway 10 bold'), bg=c3, fg=c1)
result_button.grid(row=4, column=0, sticky=NSEW, pady=60, padx=10, columnspan=60)



window.mainloop()