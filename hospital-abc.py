# Dicionários para armazenar dados dos pacientes e médicos
pacientes = {}  
medicos = {}

# Função para adicionar um novo paciente
def adicionar_paciente():
    while True: #loop infinito só vai parar quando tiver return ou break (condição True nunca será falsa)
        
        cpf = input("CPF: ")
        if cpf.isalpha(): #verifica se o cpf contém apenas letras
            print("O CPF deve ser representado em números.\nInsira os dados novamente:")
            continue #reiniciar o loop quando uma entrada inválida é detectada

        if cpf in pacientes and pacientes[cpf]: #cpf (in) pacientes verifica se o CPF está presente como uma chave no dicionário pacientes.
            print("Paciente já cadastrado.")
            return #interromper  a execução
#A expressão cpf in pacientes verifica se o CPF está presente no dicionário de pacientes.
#A expressão pacientes[cpf] verifica se há algum valor associado a esse CPF.
        nome = input("Nome: ")

        idade = input("Idade: ")
        if idade.isalpha():
            print("A idade deve ser representada em números.\nInsira os dados novamente:")
            continue  #reiniciar o loop quando uma entrada inválida é detectada


        endereco = input("Endereço: ")

        telefone = input("Telefone: ")
        if telefone.isalpha():
            print("O telefone deve ser representado em números.\nInsira os dados novamente:")
            continue #reiniciar o loop quando uma entrada inválida é detectada


        if not cpf or not nome or not idade or not endereco or not telefone: #Verifica se a variável cpf está vazia ou não foi preenchida.
            print("Por favor, preencha todos os campos.")
            continue #reiniciar o loop quando uma entrada inválida é detectada


        pacientes[cpf] = {"Nome": nome, "Idade" : idade, "Endereco" : endereco, "Telefone" : telefone,}

        print("Novo paciente cadastrado com sucesso!")
        break #é usada para sair de um loop imediatamente, interrompendo sua execução

# Função para adicionar um novo médico
def adicionar_medico():
    while True: #loop infinito só vai parar quando tiver return ou break (condição True nunca será falsa)

        crm = input("CRM: ")

        if crm in medicos and medicos[crm]:
            print("Médico já cadastrado.")
            return  #interromper  a execução

        nome = input("Nome: ")

        especialidade = input("Especialidade: ")

        telefone = input("Telefone: ")
        if telefone.isalpha():
            print("O telefone deve ser representado em números.\nInsira os dados novamente:")
            continue #reiniciar o loop quando uma entrada inválida é detectada

        if not crm or not nome or not especialidade or not telefone: # #Verifica se a variável cpf está vazia ou não foi preenchida.
            print("Por favor, preencha todos os campos.")
            continue #reiniciar o loop quando uma entrada inválida é detectada

        medicos[crm] = {"Nome": nome, "Especialidade": especialidade, "Telefone": telefone,}

        print("Novo médico cadastrado com sucesso!")
        break #é usada para sair de um loop imediatamente, interrompendo sua execução

# Função para pesquisar um paciente por CPF
def pesquisar_paciente():

    while True: #loop infinito só vai parar quando tiver return ou break (condição True nunca será falsa)

        cpf = input("CPF: ")
        if cpf.isalpha():
            print("O CPF deve ser representado em números.\nInsira novamente:")
            continue ##reiniciar o loop quando uma entrada inválida é detectada


        paciente = pacientes.get(cpf) #é usado para acessar o valor associado a uma determinada chave em um dicionário.
                                      #Se a chave estiver presente no dicionário, get() retornará o valor associado a essa chave.

        if paciente and paciente:
            print(f"Paciente encontrado: {paciente}")
            break #é usada para sair de um loop imediatamente, interrompendo sua execução

        else:

            print("O paciente não foi encontrado.")
            break #é usada para sair de um loop imediatamente, interrompendo sua execução

# Função para pesquisar um médico por CRM
def pesquisar_medico():

    while True:

        crm = input("CRM: ")
        medico = medicos.get(crm) #para acessar o valor associado à chave crm no dicionário medicos.
                                  #Se crm estiver presente como uma chave em medicos, get() retornará o valor associado a essa chave.
        if medico and medico:
            print(f"Médico encontrado: {medico}")
            break #é usada para sair de um loop imediatamente, interrompendo sua execução

        else:

            print("O médico não foi encontrado.")
            break #é usada para sair de um loop imediatamente, interrompendo sua execução

# Função para excluir um paciente pelo CPF
def excluir_paciente():

    while True:


        cpf = input("Digite o CPF do paciente a ser removido: ")

        if cpf in pacientes and pacientes[cpf]:
            pacientes[cpf] = False
            print("Paciente excluído com sucesso!")
            break  #é usada para sair de um loop imediatamente, interrompendo sua execução

        else:

            print("O paciente não foi encontrado.")
            break  #é usada para sair de um loop imediatamente, interrompendo sua execução

# Função para excluir um médico pelo CRM
def excluir_medico():

    while True:

        crm = input("Digite o CRM do médico a ser removido: ")

        if crm in medicos and medicos[crm]:
            medicos[crm] = False
            print("Médico excluído com sucesso!")
            break ##é usada para sair de um loop imediatamente, interrompendo sua execução


        else:

            print("O médico não foi encontrado.")
            break #é usada para sair de um loop imediatamente, interrompendo sua execução


# Função principal para executar o menu
def executar_sistema():

    while True:

        print("\nMenu do Sistema")

        print("1. Adicionar Novo Paciente")

        print("2. Adicionar Novo Médico")

        print("3. Pesquisar Paciente pelo CPF")

        print("4. Pesquisar Médico pelo CRM")

        print("5. Excluir Paciente pelo CPF")

        print("6. Excluir Médico pelo CRM")

        print("7. Sair do Sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_paciente()

        elif opcao == '2':
            adicionar_medico()

        elif opcao == '3':
            pesquisar_paciente()

        elif opcao == '4':
            pesquisar_medico()

        elif opcao == '5':
            excluir_paciente()

        elif opcao == '6':
            excluir_medico()

        elif opcao == '7':
            print("Obrigado por usar o sistema!")
            break

        else:

            print("Opção inválida!")

if __name__ == "__main__":
    executar_sistema()