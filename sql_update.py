# importamos a biblioteca de conexao com banco de dados do tipo mysql
import mysql.connector

# cria um objeto que permite a conexao com o banco de dados
conexao = mysql.connector.connect(user='root', password='pass', host='127.0.0.1', database='lendas')

# cursor é um objeto que permite executar queries SQL no banco
cursor = conexao.cursor()


# lista contendo o modelo de carro que iremos atualizar no banco 
# e o novo modelo de carro que iremos atualizar
lista_modelo =  ['UNINHO CHAVOSO COM ESCADA NO TETO', '911 Twin Turbo']

# query SQL que iremos executar no banco para atualizar um modelo especifico
# repare nas variaveis '%s', elas irao receber os valores da lista 'lista_modelo' sequencialmente
query = """ UPDATE carros SET modelo = %s WHERE modelo = %s """

# objeto cursor armazena em memoria (staging) a query junto com os dados da lista 'lista_modelo' 
cursor.execute(query, lista_modelo)

# o objeto conexao pega todas as queries armazenadas em memoria 
# e executam as alterações permanentemente no banco de dados
conexao.commit()

# mata o cursor, reseta todos resultados, apaga todas queries 
# e garante que o objeto cursor nao possui mais nenhuma referencia ao objeto conexao
cursor.close()

# mata a conexao com o banco de dados
conexao.close()