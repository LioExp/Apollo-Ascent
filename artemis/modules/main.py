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

        if verb in verbs:
            print(verbs[verb])
        else:
            print(f'parece que o {verb} não existe!')

        if noun in nouns:
            print(nouns[noun])
        else:
            print(f'parece que o {noun} não existe!')

    except IndexError:
        print('voce n colocou o comando completo, verifique o comando digitado')



