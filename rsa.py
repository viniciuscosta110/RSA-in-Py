import random

def criptografar(texto, e, n):
    encriptado = (texto ** e) % n
    return encriptado

def achar_d(e, totiente):
    i = 1
    while(True):
        if(e * i % totiente == 1):
            return i
        i += 1

def primos_entre_si(n):
    resultado = []

    for i in range(1, n):
        if(MDC(n, i) == 1):
            resultado.append(i)
    return random.choice(resultado)

def qntd_totiente(p, q):
    return (p - 1) * (q - 1)
    
def MDC(p, q):
    if(p < q):
        aux = p
        p = q
        q = aux
    if(q == 0):
        return p
    else:
        return MDC(q, p%q)

def main():
    print("  ####################################################")
    print("  ##        ENCRIPTAÇÃO E DESENCRIPTAÇÃO RSA        ##")
    print("  ####################################################")
    print("  ##        Escolha uma das opções á seguir:        ##")
    print("  ##------------------------------------------------##")
    print("  ## 1: GERAR CHAVE PUBLICA                         ##")
    print("  ## 2: ENCRIPTAR                                   ##")
    print("  ## 3: DESENCRIPTAR                                ##")
    print("  ## 4: SAIR                                        ##")
    print("  ####################################################")
    
    escolha = int(input())

    if(escolha == 1):
        print("Deseja escolher os numeros primos?")
        print("1: SIM                       2:NÃO")
        escolha_primos = int(input())

        if(escolha_primos == 1):
            p = int(input("Primeiro número primo(p): "))
            q = int(input("Segundo número primo(q): "))
            texto = 9#################

            n = p * q

        totiente = qntd_totiente(p, q)

        e = primos_entre_si(n)
        d = achar_d(e, totiente)

        print(criptografar(texto, e, n))
        print("cahve publica: {}".format(e))
        print("chave privada: {}".format(d))
main()
\\Gabriel é gay
