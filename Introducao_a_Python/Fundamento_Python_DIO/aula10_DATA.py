from datetime import date, datetime, time, timedelta
from time import strftime, strptime



# existe uma documentação do site oficial do python, com todas diretriezes do "datetime" , usando as diretrizes do python
# utilizar essta documentação... "%d = dia, %m = mes, %y mes, %Y= mes com 4 digitos"
# pode trocar a barra por espaco, traço, etc....

def trabalhando_com_datetime() :
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H: %M')) #data atual dia mes ano, hora e segundos H: e M
    print(data_atual.strftime('%c'))
    print(data_atual.year) #pode puxar a data, hora, dia, minuto, etc resultados separados.
    tupla = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo') #dados para poder trazer traduzido
    print(tupla[data_atual.weekday()]) #com o weekday, voce consegue puxar a data..
    data_criada = datetime(2018, 6, 20, 15, 30, 20) #cria uma data
    print(data_criada) #imprime a data criada
    print(data_criada.strftime('%c')) #imprime a data convertida em strf + time
    data_string = '01/01/2022 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=2) #para retirar/somar (basta trocar o simbolo) algo e chegar na data desejada, primeiro retira os dias, horas e minutos.
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today()
    # passou a date, para uma string, e apos isso pode ser manipulado, dentro do date nao tem como.
    data_atual_str = data_atual.strftime('%A %M %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))


def trabalhando_com_time() :
    horario = time(hour=15, minute=18, second=30)
    print(horario) #imprimiu em formato de horario a linha acima.
    horario_str = horario.strftime('%H: %M: %S')
    print(horario_str) #imprimiu em formato string a linha acima.
    print(type(horario_str)) #imprimiu o type de horario_str class string.


# esse caralho nao funcionava enquanto nao colocar : from datetime import date, datetime, time

if __name__ == '__main__':
    trabalhando_com_datetime()
   #trabalhando_com_date()
   # trabalhando_com_time()
