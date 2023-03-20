import logging as lg
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_note():
    global diretorio

    try:
        if diretorio == '':
            diretorio = asksaveasfilename()
        arq = open(diretorio, 'w')
        arq.write(texto.get('1.0', END))
    except Exception as ex:
        lg.info(f'Error: [{ex}]')
        return None
        pass


def open_note():
    global diretorio
    try:
        diretorio = askopenfilename()
        conteudo = []
        arq = open(diretorio, 'r')
        for linha in arq:
            conteudo.append(linha)
        texto.delete('1.0', END)
        texto.insert('insert', '\n'.join(conteudo))
    except Exception as ex:
        lg.info(f'Error: [{ex}]')


def exit_app():
    tela.destroy()


def theme_app(style):
    if style == 1:
        texto['bg'] = 'black'
        texto['fg'] = 'white'
    elif style == 2:
        texto['bg'] = 'white'
        texto['fg'] = 'black'
    elif style == 3:
        texto['bg'] = 'orange'
        texto['fg'] = 'black'


diretorio = ''
tamanho = 12
fonte_estilo = 'arial'

tela = Tk()

tela['bg'] = 'white'
tela.title('Note Bloxk')
tela.geometry('700x350')

menu = Menu(tela)

arquivo = Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=arquivo)
arquivo.add_command(label='Novo')
arquivo.add_command(label='Nova Janela')
arquivo.add_command(label='Abrir', command=open_note,)
arquivo.add_command(label='Salvar', command=save_note)
arquivo.add_command(label='Salvar Como')
arquivo.add_command(label='Sair', command=exit_app)

tela.config(menu=menu)

texto = Text(tela, bg='white', fg='black', width=180, height=80, relief=RIDGE)

texto.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
texto.configure(font=(fonte_estilo, tamanho))

tela.mainloop()
