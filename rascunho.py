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
def ler_documento(documento_id):
    documento = collection.find_one({'_id': documento_id})
    return documento

# Atualizar um documento (Update)
def atualizar_documento(documento_id, novos_dados):
    result = collection.update_one({'_id': documento_id}, {'$set': novos_dados})
    return result.modified_count

# Deletar um documento (Delete)
def deletar_documento(documento_id):
    result = collection.delete_one({'_id': documento_id})
    return result.deleted_count

# Exemplo de uso
documento = {'nome': 'Exemplo', 'idade': 25}

# Criar um novo documento
documento_id = criar_documento(documento)
print('Documento criado com o ID:', documento_id)

# Ler o documento criado
documento_recuperado = ler_documento(documento_id)
print('Documento recuperado:', documento_recuperado)

# Atualizar o documento
novos_dados = {'idade': 30}
atualizar_documento(documento_id, novos_dados)
documento_atualizado = ler_documento(documento_id)
print('Documento atualizado:', documento_atualizado)

# Deletar o documento
deletar_documento(documento_id)
documento_deletado = ler_documento(documento_id)
print('Documento deletado:', documento_deletado)
