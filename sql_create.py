# importamos a biblioteca de conexao com banco de dados do tipo mysql
import mysql.connector

# cria um objeto que permite a conexao com o banco de dados
conexao = mysql.connector.connect(user='root', password='pass', host='127.0.0.1', database='lendas')

# cursor é um objeto que permite executar queries SQL no banco
cursor = conexao.cursor()


# registro que iremos inserir no banco
carro =  ['Porsche', 
			  '911 Twin Turbo', 
			  '1997',
			  'Tanya']

# query SQL que recebera o registro 
# (repare nas variaveis em VALUES, elas irao receber sequencialmente a lista carro)
query = """ INSERT INTO carros (marca, modelo, ano, codinome) VALUES (%s, %s, %s, %s) """

# Objeto cursor armazenando em memoria (staging) a query junto com os dados da lista 'carro'
cursor.execute(query, carro)

# o objeto conexao pega todas as queries armazenadas em memoria 
# e executam as alterações permanentemente no banco de dados
conexao.commit()

# mata o cursor, reseta todos resultados, apaga todas queries 
# e garante que o objeto cursor nao possui mais nenhuma referencia ao objeto conexao
cursor.close()

# mata a conexao com o banco de dados
conexao.close()
