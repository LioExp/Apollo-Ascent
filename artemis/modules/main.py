from time import sleep
import sys

verbs = {
    'v02':'mostrar dados',
    'v03':'iniciar contagem regressiva',
    'v04':'abortar missão',
    'v05':'iniciar decolagem'
    }
    
nouns = {
    'n01':'posição',
    'n02':'velocidade'
    }
nave = {'altitude': 0, 'velocidade': 0, 'combustivel': 99}

def contagem_regressiva():
    for i in range(10,-1, -1):
        print(i)
        sleep(1)

def abortar_missão():
    print('abortando a missão...')
    sys.exit()
        
def decolagem():
    for i in range(0, 101, 10):
        nave["altitude"]= i
        nave['velocidade'] = i*2
        nave['combustivel'] = nave['combustivel'] - i
        if nave['combustivel'] <= 0:
            print('Aviso!, combustivel insuficiênte.')
            break
        else:
            print(f'Altitude: {nave["altitude"]}Km\nVelocidade: {nave["velocidade"]}Km/s\nCombustivel: {nave["combustivel"]}')
        sleep(1)

    
while True:
    usuario = input("digite seu pedido: ").strip()
    if usuario == 'exit':
        usuario = input('voce tem a certeza que quer sair?(y/n)').strip()
        if usuario == 'y':
            break
        else:
            continue
    try :
        comando = usuario 
        partes = comando.split() 
        verb = partes[0]
        noun = partes[1]

        if verb in verbs and noun in nouns:
            print(verbs[verb])
            print(nouns[noun])

            if verb == 'v03':
                contagem_regressiva()

            elif verb == "v04":
                abortar_missão()
            elif verb == 'v05':
                decolagem()


        elif verb not in verbs:
            print(f'parece que o {verb} não existe!')

        elif noun not in nouns:
            print(f'parece que o {noun} não existe!')

        

    except IndexError:
        print('voce n colocou o comando completo, verifique o comando digitado')



