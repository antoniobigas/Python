import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos:')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartao?')],
            [sg.Radio('Sim', 'Cartoes', key='aceitaCartao'),sg.Radio('Nao', 'Cartoes',key='naoAceitaCartao')],
            #[sg.Slider(range=(0,255),default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)
    
    #Extrair dados da Tela    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            #velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita_gmail : {aceita_gmail}' )
            print(f'aceita_outlook : {aceita_outlook}')
            print(f'aceita_yahoo : {aceita_yahoo}')
            print(f'aceita_cartao: {aceita_cartao}')
            print(f'nao_aceita_cartao: {nao_aceita_cartao}')
            #print(f'velocidade_script: {velocidade_script}') #não achei util utilizar isso. serve pra limitar o tempo de envio de dados

tela = TelaPython()
tela.Iniciar()

