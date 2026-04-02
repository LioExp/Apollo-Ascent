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
    except IndexError:
        print('voce n colocou o comando completo, verifique o comando digitado')