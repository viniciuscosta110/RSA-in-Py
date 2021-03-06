import os
import math

def inverso(e, phi):

    phi2 = phi
    coeficientes = [] 
    coeficientes_invertidos = []
    indices = []

    tamanho=0
    tabela = 1

    a = e/phi
    a = int(a)
    coeficientes.append(a)
    b = e%phi

    while(b!=0):
        e = phi
        phi = b
        a = e/phi
        a = int(a)
        b = e%phi
        
        coeficientes.append(a)
        tamanho += 1
   
    j=tamanho-1

    for i in range(0,tamanho):
        coeficientes_invertidos.append(coeficientes[j])
        j -= 1

    tabela = 1
    anterior = 0

    for i in range(0,tamanho):
        indices.append(coeficientes_invertidos[i]*tabela + anterior)
        anterior = tabela
        tabela = indices[i]
  
    if(tamanho % 2 == 0):
        indices[tamanho-2] = -indices[tamanho-2]
        while(indices[tamanho-2]<1):
            indices[tamanho-2] = indices[tamanho-2] + phi2

    inv = indices[tamanho-2]
    return inv

def fastModularExponentiation(m, e, n):
    if(e == 0):
        return 1
    elif(e%2 == 0):
        aux = fastModularExponentiation(m, e/2, n)
        return (aux**2)%n
    else:
        return(m%n*fastModularExponentiation(m, e-1, n))%n

def limpar_terminal():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def limpar_arquivo(apagar):

    arquivo = open(apagar, 'w')
    arquivo.close()

def verificar_primos(x):
    if(x <= 1):
        return False
    aux = math.ceil(math.sqrt(x))
    for i in range(2,aux):
        if(x % i == 0):
            return False
    return True

def primos_entre_si(n,e):
    resultado = MDC(n, e)

    if(resultado == 1):
        return True
    else:
        return False
def MDC(p, q):
    if(q == 0):
        return p
    else:
        return MDC(q, p%q)

def calcular_phi(p, q):
    return (p - 1) * (q - 1)

def chave_pub(x):
    arquivo = open('chave_publica.txt' , 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close()

def msg_criptografada(x):
    arquivo = open('msg_criptografada.txt', 'a')
    arquivo.write("{} ".format(x))
    arquivo.close()
    
def msg_descriptografada(x): 
    arquivo = open('msg_descriptografada.txt', 'a')
    arquivo.write("{}\n".format(x))
    arquivo.close()

def criptografar(c,e,n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    aux = 0
    for i in range(0,29):
        if(c == array[i]):
            aux = i
    M = fastModularExponentiation(aux, e, n)
    return M

def desencriptar(nome_arquivo, d, n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

    arquivo = open(nome_arquivo, 'r')
    msg = arquivo.read().split(" ")
    palavras = ""
    tamanho = msg.__len__()
    tamanho -= 1
    
    for i in range (0, tamanho):
        if(msg[i] == " "):
            break
        c = msg[i]
        c = int(c)
        c = fastModularExponentiation(c, d, n)
        palavras += array[c]
        
    msg_descriptografada(palavras)
    arquivo.close()

def main():
    limpar_terminal()
    while(1):
        print("  <==================================================>")
        print("  <=        ENCRIPTAÇÃO E DESENCRIPTAÇÃO RSA        =>")
        print("  <==================================================>")
        print("  <=        Escolha uma das opções á seguir:        =>")
        print("  <=                                                =>")
        print("  <= 1: GERAR CHAVE PUBLICA                         =>")
        print("  <= 2: ENCRIPTAR                                   =>")
        print("  <= 3: DESENCRIPTAR                                =>")
        print("  <= 4: SAIR                                        =>")
        print("  <==================================================>")
        escolha = int(input("    >Digite sua escolha: " ))
        limpar_terminal()
    
        if(escolha == 1):
            print("  <==================================================>")
            print("  <=              GERANDO CHAVE PÚBLICA             =>")
            print("  <==================================================>")
            print("  <= Digite os números primos:                      =>")
            print("  <==================================================>")
            p = int(input("     (p):"))
            q = int(input("     (q):"))
            if(p * q < 28):
                while(p * q < 28):
                    print("  <==================================================>")
                    print("  <=          (p) e (q) são muito pequenos!         =>")
                    print("  <=              Digite-os novamente!              =>")
                    print("  <==================================================>")
                    p = int(input("      Digite (p):"))
                    q = int(input("      Digite (q):"))
            if(verificar_primos(p) == False or verificar_primos(q) == False):
                    while(verificar_primos(p) == False or verificar_primos(q) == False):
                        limpar_terminal()
                        print("  <==================================================>")
                        print("  <=  Um ou mais números digitados não são primos!  =>")
                        print("  <=              Digite-os novamente!              =>")
                        print("  <==================================================>")
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            if(p == q):
                    while(p == q):
                        limpar_terminal()
                        print("  <==================================================>")
                        print("  <=             (p) e (q) são iguais!              =>")
                        print("  <=              Digite-os novamente!              =>")
                        print("  <==================================================>")
                        p = int(input("      Digite (p):"))
                        q = int(input("      Digite (q):"))
            n = p * q
            phi = calcular_phi(p, q)
            limpar_terminal()
            print("  <==================================================>")
            print("  <=    Insira o (e) para gerar a chave pública:    =>")
            print("  <==================================================>")
            e = int(input("     (e): "))
            while(primos_entre_si(e,phi) == 0 or e >= phi or e <= 1):
                limpar_terminal()
                if(primos_entre_si(e, phi) == 0 and e < phi and e > 1):
                    print("  <==================================================>")
                    print("  <=     O NÚMERO DIGITADO NÃO É COPRIMO A PHI!     =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
                elif(e >= phi):
                    print("  <==================================================>")
                    print("  <=    O NÚMERO DIGITADO É MAIOR OU IGUAL A PHI!   =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
                elif(e <= 1):
                    print("  <==================================================>")
                    print("  <=     O NÚMERO DIGITADO É MENOR OU IGUAL A 1!    =>")
                    print("  <=              Digite (e) novamente:             =>")
                    print("  <==================================================>")
    
                e = int(input("     (e): "))
            limpar_terminal()
            print("  ####################################################")
            print("              CHAVE PÚBLICA: (n):{} (e):{}            ".format(n, e))
            print("  ####################################################")
            
            chave = str(n) +" "+ str(e)
            chave_pub(chave)

        elif(escolha == 2):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=          PRECISAMOS DA CHAVE PUBLICA!          =>")
            print("  <=              Digite o (n) e o (e)              =>")
            print("  <==================================================>")
            n = int(input("     (n): "))
            e = int(input("     (e): "))
            print("  <==================================================>")
            print("  <=    Digite a sua mensagem para encripta-la:     =>")
            print("  <==================================================>")

            texto = input("    > ")
            texto = texto.upper()

            limpar_terminal()

            print("  ####################################################")
            print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
            print("                  msg_criptografada.txt               ")
            print("  ####################################################")
    
            limpar_arquivo('msg_criptografada.txt')
            
            for i in range(0,len(texto)):
                msg_criptografada(criptografar(texto[i], e, n))
            print()
    
        elif(escolha == 3):
            limpar_terminal()
            while(1):
                print("  <==================================================>")
                print("  <=       Deseja utilizar um arquivo externo?      =>")
                print("  <=              (1)Sim      (2)Não                =>")
                print("  <==================================================>")
                escolha = int(input("    > "))
                if(escolha == 1):
                    print("  <==================================================>")
                    print("  <=       Digite o nome do arquivo que deseja      =>")
                    print("  <=                  desencriptar:                 =>")
                    print("  <==================================================>")
                    nome_arquivo = input("    Arquivo: ")
                    break
                elif(escolha == 2):
                    nome_arquivo = "msg_criptografada"
                    break
                else:
                    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
                    print("  <!!               Escolha inválida               !!>")
                    print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
                    
            print("  <==================================================>")
            print("  <=     Para desencriptar insira os valores de:    =>")
            print("  <=                 (p), (q) e (e)                 =>")
            print("  <==================================================>")
            p = int(input("    (p): "))
            q = int(input("    (q): "))
            e = int(input("    (e): "))
            limpar_terminal()

            print("  ####################################################")
            print("           SUA MENSAGEM SE ENCONTRA NO ARQUIVO        ")
            print("                msg_descriptografada.txt              ")
            print("  ####################################################")

            phi = calcular_phi(p, q)
            n = p * q
            d = inverso(e, phi)

            nome_arquivo += '.txt'
            
            limpar_arquivo('msg_descriptografada.txt')
            desencriptar(nome_arquivo, d, n)
            
            print()
            
        elif(escolha == 4):
            exit()
        else:
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
            print("  <!!               Escolha inválida               !!>")
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
main()
