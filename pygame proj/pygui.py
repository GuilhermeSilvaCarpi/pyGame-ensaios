from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme(sg.theme_list()[4])
layout = [[sg.Text('user'), sg.Input(key='usuario', size=(20, 1))],
          [sg.Text('senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
          [sg.Checkbox('hhtiy')],
          [sg.Button('button')]]

# janela
janela = sg.Window('janela', layout)

# ler eventos
loop = True
while loop:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        loop = False
        break
    if eventos == 'button':
        if valores['usuario'] == 'gui' and valores['senha'] == '123':
            print('somethinck')
        else:
            print('bh')
