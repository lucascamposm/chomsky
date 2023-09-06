
import os
import csv
import platform 


estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'}
alfabeto = {'i', 'c', 'v', 'r', 'p', 's', 't', 'j', 'o', 'x', 'z', 'l', 'f', 'n', 'm', 'y', 'u', 'k', 'b', 'a', 'q', 'd', 'e', 'g', 'h'}
estado_inicial = 'q0'
estado_final = {'q0'}


#=============================================
# Passos 
#=============================================
passos = { # AÇÕES/OPERAÇÕES RELACIONADAS A CADA SÍMBOLO
'i' : {"realiza login em conta"},
'c' : {"abre o menu de compra de créditos"},
'v' : {"insere valor a ser adquirido"},
'r' : {"realiza o pedido do valor"},
'p' : {"realiza o pagamento do pedido"},
's' : {"abre o menu de consulta do saldo em conta"},
't' : {"seleciona para qual cartão realizar a operação"},
'j' : {"mostra saldo"},
'o' : {"abre o menu de pedidos realizado"},
'x' : {"cancela o pedido"},
'z' : {"verifica se há cartão válido"},
'l' : {"abre menu de cancelar cartão"},
'f' : {"faz o cancelamento de cartão"},
'n' : {"abre menu de dados pessoais"},
'm' : {"atualiza o email/telefone"},
'y' : {"insere email/telefone"},
'u' : {"atualiza o endereço"},
'k' : {"insere endereço"},
'b' : {"volta ao menu principal"},
'a' : {"refaz o último pedido"},
'q' : {"realiza logoff da conta"},
'd' : {"verifica se há pedido pendente"},
'e' : {"verifica se o usuário é válido"},
'g' : {"verifica se o menu é válido para tal operação"},
'h' : {"verifica se o valor mínimo foi atingido"}}

#=============================================
# Transicoes
#=============================================

transicoes = { # DESCRIÇÃO TEXTUAL DO AUTÔMATO, NO FORMATO -> estado_atual : {simbolo_lido 1: estado_destino 1}, ... , {simbolo_lido n: estado_destino n}
    'q0':  {'i': 'q1'},
    'q1':  {'o': 'q2', 'c': 'q3', 's': 'q4', 'l': 'q5', 'n': 'q6', 'q': 'q0'},
    'q2':  {'a': 'q12', 'd': 'q7', 'b': 'q1'},
    'q3':  {'z': 'q10'},
    'q4':  {'z': 'q22'},
    'q5':  {'z': 'q19', 'b': 'q1'},
    'q6':  {'b': 'q1', 'u': 'q16', 'm': 'q15'},
    'q7':  {'p': 'q9', 'x': 'q8'},
    'q8':  {'b': 'q1'},
    'q9':  {'b': 'q1'},
    'q10': {'b': 'q1', 't': 'q11'},
    'q11': {'v': 'q24'},
    'q12': {'r': 'q13'},
    'q13': {'d': 'q14'},
    'q14': {'r': 'q13', 'b': 'q1'},
    'q15': {'y': 'q17'},
    'q16': {'k': 'q18'},
    'q17': {'u': 'q16', 'b': 'q1'},
    'q18': {'m': 'q15', 'b': 'q1'},
    'q19': {'t': 'q20'},
    'q20': {'f': 'q21'},
    'q21': {'z': 'q19', 'b': 'q1'},
    'q22': {'t': 'q23', 'b': 'q1'},
    'q23': {'j': 'q22'},
    'q24': {'h': 'q25'},
    'q25': {'v': 'q24', 'r': 'q26'},
    'q26': {'d': 'q27'},
    'q27': {'p': 'q28', 't': 'q11', 'b': 'q1'},
    'q28': {'t': 'q11', 'b': 'q1'}
}

#=============================================
# Funcoes Auxiliares
#=============================================
def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def enter_input():
    entrada = input('\n[input]: ')
    return entrada

def print_menu():
    print("\t=========================================================")
    print("\t|        Bem vindo ao simulador em autômato TRI!        |")
    print("\t|  O sistema de transporte integrado de Porto Alegre    |")
    print("\t=========================================================")
    print("DIGITE: ")
    print("[0] para sair")
    print("[1] para inserir uma palavra de entrada")
    print("[2] para inserir um nome de arquivo de entradas")
    print("[3] para visualizar as operações disponiveis")

def insira_tecla_continuar():
    print("\nInsira uma tecla para continuar...",end="")
    enter_input()

def print_msg(mensagem):
    frase = (f"|                 {mensagem}                 |")
    aux_print_linha(len(frase))  #linha com "========"
    print(frase) #print da msg 
    aux_print_linha(len(frase))
    insira_tecla_continuar()

def aux_print_linha(tamanho_linha):
    for i in range(tamanho_linha): 
        print("=",end="")
    print()


def handle_arquivo(arquivo):
    try:
        with open(arquivo, "r") as handle:
            leitor = csv.reader(handle)
            for row in leitor:
                for i in range(len(row)):
                    processa_automato(row[i])
                    insira_tecla_continuar()
                    limpar_tela()
    except:
        print_msg("Erro ao Abrir o arquivo!")
#=============================================
# funcao Simulate 
#=============================================
def simulate(input):
    estado_atual = estado_inicial # processamento começa no estado inicial

    for simbolo in input: # para cada símbolo da palavra de entrada
        if simbolo not in alfabeto: # retorna erro caso símbolo não pertence ao alfabeto
            raise ValueError(f"Simbolo lido '{simbolo}' -> não pertence ao alfabeto.")
        
        if simbolo in transicoes[estado_atual]: # caso o simbolo seja válido para o estado atual (!= indefinição)
            print(f'{passos[simbolo]} -> OK')
            estado_atual = transicoes[estado_atual][simbolo]
        else:
            print("\nErro, era esperado: ", end='')
            for i in transicoes[estado_atual]:
                print(i + ' | ', end='')
            print()
            return None

    return estado_atual in estado_final

#=============================================
# Proessa Automato 
#=============================================

def processa_automato(palavra):
    saida = simulate(palavra)
    msg_sucesso = (f"A entrada '{palavra}' PERTENCE a linguagem.")
    msg_erro = (f"A entrada '{palavra}' NAO PERTENCE a linguagem.")
    if saida:
        print_msg(msg_sucesso)
    else:
        print_msg(msg_erro)

#=============================================
# Funcao Terminal
#=============================================
def terminal():
    global passos
    resposta = '10'
    arquivo = None
    palavra = None

    while (resposta != None):
        limpar_tela()
        print_menu()

        resposta = enter_input()

        if(resposta == '1'):
            limpar_tela()
            print("Digite uma palavra")
            palavra = enter_input()
            processa_automato(palavra)
            print("\nInsira uma tecla para continuar...")
            enter_input()

        elif(resposta == '2'):
            limpar_tela()
            print("Insira o nome do arquivo:")
            arquivo = enter_input()
            handle_arquivo(arquivo)

        elif(resposta == '3'):
            for chave, valor in passos.items():
                print(f" {chave}: {valor}")
            insira_tecla_continuar()

        elif(resposta == '0'):
            resposta = None
        
        else:
            limpar_tela()
            print_msg("Operação inválida!")

#=============================================
# Main
#=============================================

def main():
    terminal()

if __name__ == "__main__":
    main()
