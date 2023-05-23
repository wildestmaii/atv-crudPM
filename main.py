from pymongo import MongoClient

# Configurar a string de conexão do MongoDB Atlas
# Substitua <username>, <password> e <clustername> pelas suas credenciais e informações do cluster
connection_string = 'mongodb+srv://maiarameneses:teupai@cluster0.jpwytyh.mongodb.net/crudCAPI?retryWrites=true&w=majority'
##                   mongodb+srv://maiarameneses:<PASSWORD>@cluster0.jpwytyh.mongodb.net 
# Criar uma instância do cliente MongoDB
client = MongoClient(connection_string)

# Selecionar o banco de dados
db = client['crudCAPI']

# Selecionar a coleção
collection = db['teste']

# Criar um documento (Create)
def criar_documento(documento):
    result = collection.insert_one(documento)
    return result.inserted_id

# Ler um documento (Read)
def ler_documento(senha):
    documento = collection.find_one({'senha': senha})
    return documento

# Atualizar um documento (Update)
def atualizar_documento(senha, novos_dados):
    result = collection.update_one({'senha': senha}, {'$set': novos_dados})
    return result.modified_count

# Deletar um documento (Delete)
def deletar_documento(senha):
    result = collection.delete_one({'senha': senha})
    return result.deleted_count

def exibir_menu():
    print("---- CADASTRO DE CAPIVARAS ----")
    print("1. Cadastrar nova capivara")
    print("2. Visualizar capivara por senha")
    print("3. Atualizar capivara por senha")
    print("4. Deletar capivara por senha")
    print("0. Sair")


def cadastrar_capivara():
    nome = input("Digite o nome da capivara: ")
    idade = input("Digite a idade da capivara: ")
    senha = input("Digite a senha da capivara: ")
    documento = {"nome": nome, "idade": idade, "senha": senha}
    documento_id = criar_documento(documento)
    print("Capivara cadastrada com o ID:", documento_id)


def visualizar_capivara():
    senha = input("Digite a senha da capivara: ")
    capivara = ler_documento(senha)
    if capivara:
        print("Capivara encontrada:")
        print("ID:", capivara['_id'])
        print("Nome:", capivara['nome'])
        print("Idade:", capivara['idade'])
    else:
        print("Capivara não encontrada.")


def atualizar_capivara():
    senha = input("Digite a senha da capivara a ser atualizada: ")
    capivara = ler_documento(senha)
    if capivara:
        print("Capivara encontrada:")
        print("ID:", capivara['_id'])
        print("Nome:", capivara['nome'])
        print("Idade:", capivara['idade'])
        novo_nome = input("Digite o novo nome da capivara: ")
        nova_idade = input("Digite a nova idade da capivara: ")
        novos_dados = {"nome": novo_nome, "idade": nova_idade}
        atualizar_documento(senha, novos_dados)
        print("Capivara atualizada com sucesso.")
    else:
        print("Capivara não encontrada.")


def deletar_capivara():
    senha = input("Digite a senha da capivara a ser deletada: ")
    capivara = ler_documento(senha)
    if capivara:
        print("Capivara encontrada:")
        print("ID:", capivara['_id'])
        print("Nome:", capivara['nome'])
        print("Idade:", capivara['idade'])
        confirmacao = input("Tem certeza que deseja deletar esta capivara? (S/N): ")
        if confirmacao.lower() == 's':
            deletar_documento(senha)
            print("Capivara deletada com sucesso.")
        else:
            print("Operação cancelada.")
    else:
        print("Capivara não encontrada.")


def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            cadastrar_capivara()
        elif opcao == '2':
            visualizar_capivara()
        elif opcao == '3':
            atualizar_capivara()
        elif opcao == '4':
            deletar_capivara()
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Executar o programa
if __name__ == '__main__':
    main()
