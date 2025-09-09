from datetime import date, datetime
from tkinter import Label, Entry, Button, Tk, messagebox

def q12():
    def show_idade():
        idade = int(txt_idade.get())
        msg=''
        if idade <18:
            msg = 'Menor de Idade'
        elif idade >= 65:
            msg = 'Melhor idade'
        else:
            msg = 'Maior idade'
        messagebox.showinfo(
            title='Situação da Idade:',
            message=f'{msg}'
        )
        txt_idade.delete(0,len(txt_idade.get()))
        
    window = Tk()
    window.title('Questão 12')
    window.config(padx=10, pady=10)
    lbl_idade = Label(text='Idade:')
    lbl_idade.grid(row=0, column=0)
    global txt_idade
    txt_idade = Entry(width=4)
    txt_idade.grid(row=0,column=1)
    txt_idade.focus()
    btn_ok = Button(text='OK', width=5, command=show_idade)
    btn_ok.grid(row=1, column=0, columnspan=2)
    window.mainloop()

