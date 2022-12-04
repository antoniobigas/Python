from PySimpleGUI import PySimpleGUI as sg
#para funcionar, tem que instalar com o comando a seguir no terminal: pip install pysimplegui
#layout

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

#Janela/window

janela = sg.Window('Tela de Login', layout)

#Ler os eventos  (unpacking python)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos =='Entrar':
        if valores['usuario']=='bigas' and valores['senha'] =='123456':
            print('Bem vindo ao curso de Python!')
        else:
            print ('Credenciais inválidas, verifique!')  
