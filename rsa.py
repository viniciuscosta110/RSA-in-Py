import os
import math

def inverso(num1, num2):
    num3 = num2
    coeficientes = []
    array_aux = []
    indices = []

    tamanho=1
    aux2 = 1

    a = num1/num2
    a = int(a)
    coeficientes.append(a)
    b = num1%num2

    while(b!=0):
        num1 = num2
        num2 = b
        a = num1/num2
        a = int(a)
        b = num1%num2
        
        coeficientes.append(a)
        tamanho += 1
    aux4 = tamanho-1
    j=aux4-1

    for i in range(0,aux4):
        array_aux.append(coeficientes[j])
        j -= 1

    aux2 = 1
    anterior = 0
    x = anterior

    for i in range(0,aux4):
        indices.append(array_aux[i]*aux2 + anterior)
        anterior = aux2
        aux2 = array_aux[i]*aux2 + x
        x = anterior
  
    if(aux4 % 2 == 0):
        indices[aux4-2] = -indices[aux4-2]
        while(indices[aux4-2]<1):
            indices[aux4-2] = indices[aux4-2] + num3

    return indices[aux4-2]

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

def chave_pub_1(x):
    arquivo = open('chave_publica_1.txt' , 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close()

def chave_pub_2(y):
    arquivo = open('chave_publica_2.txt', 'w')
    arquivo.write("{}\n".format(y))
    arquivo.close()

def msg_criptografada(x):
    arquivo = open('msg_criptografada.txt', 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close
    
def msg_descriptografada(x):
    arquivo = open('msg_descriptografada.txt', 'w')
    arquivo.write("{}\n".format(x))
    arquivo.close

def ler_chave_pub_1():
    arquivo = open('chave_publica_1.txt', 'r')
    x = arquivo.read()
    x = int(x)
    arquivo.close
    return(x)

def ler_chave_pub_2():
    arquivo = open('chave_publica_2.txt', 'r')
    y = arquivo.read()
    y = int(y)
    arquivo.close
    return(y)

def ler_msg_criptografada():
    arquivo = open('msg_criptografada.txt', 'r')
    x = arquivo.read()
    arquivo.close
    return x

def ler_msg_descriptografada():
    arquivo = open('msg_descriptografada.txt', 'r')
    x = arquivo.read()
    arquivo.close
    return x

def criptografar(c,e,n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    aux = 0
    for i in range(0,29):
        if(c == array[i]):
            aux = i
    M = fastModularExponentiation(aux, e, n)
    M = M % n
    return M

def desencriptar(c, d, n):
    array = ['@','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

def main():
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
            n = p * q
            phi = calcular_phi(p, q)
            limpar_terminal()
            print("  <==================================================>")
            print("  <=    INSIRA O (e) PARA GERAR A CHAVE PÚBLICA     =>")
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
        elif(escolha == 2):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=          PRECISAMOS DA CHAVE PUBLICA!          =>")
            print("  <=              Digite o (n) e o (e)              =>")
            print("  <==================================================>")
            n = int(input("  == (n): "))
            e = int(input("  == (e): "))
            print("  <==================================================>")
            print("  <=     DIGITE A SUA MENSAGEM PARA ENCRIPTA-LA     =>")
            print("  <==================================================>")
            texto = input("    > ")
            texto = texto.upper()
            limpar_terminal()
            for i in range(len(texto)):
                print(" ", criptografar(texto[i], e, n), end="")
            print()
    
        elif(escolha == 3):
            limpar_terminal()
            print("  <==================================================>")
            print("  <=   DIGITE A SUA MENSAGEM PARA DESENCRIPTA-LA!   =>")
            print("  <==================================================>")
            texto = input("    > ")
            print("  <==================================================>")
            print("  <=     PARA DESENCRIPTAR INSIRA OS VALORES DE:    =>")
            print("  <=                    (n) e (d)                   =>")
            print("  <==================================================>")
            n = int(input("    (n): "))
            d = int(input("    (d): "))
    
        elif(escolha == 4):
            exit()
        else:
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
            print("  <!!               Escolha inválida               !!>")
            print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
main()
