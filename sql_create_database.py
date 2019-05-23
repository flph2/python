# importamos a biblioteca de conexao com banco de dados do tipo mysql
import mysql.connector

# cria um objeto que permite a conexao com a instancia do mySQL
conexao = mysql.connector.connect(user='root', password='pass', host='127.0.0.1')

# cursor é um objeto que permite executar queries SQL no banco
cursor = conexao.cursor()


# query SQL que iremos executar no banco para criar um banco de dados
query = """ CREATE DATABASE lendas """

# objeto cursor armazena em memoria (staging) a query a ser executada
cursor.execute(query)

# o objeto conexao pega todas as queries armazenadas em memoria 
# e executam as alterações permanentemente no banco de dados
conexao.commit()

# mata o cursor, reseta todos resultados, apaga todas queries 
# e garante que o objeto cursor nao possui mais nenhuma referencia ao objeto conexao
cursor.close()

# mata a conexao com o banco de dados
conexao.close()