import json

# Função para salvar as receitas em um arquivo JSON
def salvar_receitas(receitas):
    with open('receitas.json', 'w') as file:
        json.dump(receitas, file)

# Função para carregar as receitas de um arquivo JSON
def carregar_receitas():
    try:
        with open('receitas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Dicionário para armazenar as receitas
receitas = carregar_receitas()

# Função para adicionar uma nova receita
def adicionar_receita(receitas, nome, ingredientes, instrucoes):
    receitas[nome] = {'ingredientes': ingredientes, 'instrucoes': instrucoes}
    salvar_receitas(receitas)
    print(f'Receita "{nome}" adicionada com sucesso!\n')

# Função para visualizar detalhes de uma receita
def visualizar_receita(receitas, nome):
    if nome in receitas:
        print(f'Detalhes da Receita "{nome}":')
        print(f'Ingredientes: {", ".join(receitas[nome]["ingredientes"])}')
        print(f'Instruções: {receitas[nome]["instrucoes"]}\n')
    else:
        print(f'Receita "{nome}" não encontrada!\n')

# Função para atualizar informações de uma receita
def atualizar_receita(receitas, nome, novos_ingredientes, novas_instrucoes):
    if nome in receitas:
        receitas[nome]['ingredientes'] = novos_ingredientes
        receitas[nome]['instrucoes'] = novas_instrucoes
        salvar_receitas(receitas)
        print(f'Informações da Receita "{nome}" atualizadas com sucesso!\n')
    else:
        print(f'Receita "{nome}" não encontrada!\n')

# Função para remover uma receita
def remover_receita(receitas, nome):
    if nome in receitas:
        del receitas[nome]
        salvar_receitas(receitas)
        print(f'Receita "{nome}" removida com sucesso!\n')
    else:
        print(f'Receita "{nome}" não encontrada!\n')

# Função para exibir o menu
def exibir_menu():
    print('--- Cadastro de Receitas Culinárias ---')
    print('1. Adicionar Receita')
    print('2. Visualizar Receita')
    print('3. Atualizar Receita')
    print('4. Remover Receita')
    print('5. Sair')

# Loop principal do programa
while True:
    exibir_menu()

    escolha = input('Escolha uma opção (1-5): ')

    if escolha == '1':
        nome = input('Digite o nome da receita: ')
        ingredientes = input('Digite os ingredientes (separados por vírgula): ').split(', ')
        instrucoes = input('Digite as instruções: ')
        adicionar_receita(receitas, nome, ingredientes, instrucoes)

    elif escolha == '2':
        nome = input('Digite o nome da receita que deseja visualizar: ')
        visualizar_receita(receitas, nome)

    elif escolha == '3':
        nome = input('Digite o nome da receita que deseja atualizar: ')
        novos_ingredientes = input('Digite os novos ingredientes (separados por vírgula): ').split(', ')
        novas_instrucoes = input('Digite as novas instruções: ')
        atualizar_receita(receitas, nome, novos_ingredientes, novas_instrucoes)

    elif escolha == '4':
        nome = input('Digite o nome da receita que deseja remover: ')
        remover_receita(receitas, nome)

    elif escolha == '5':
        print('Saindo do programa. Até mais!')
        break

    else:
        print('Opção inválida. Tente novamente.\n')






















