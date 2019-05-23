# importamos a biblioteca de conexao com banco de dados do tipo mysql
import mysql.connector

# cria um objeto que permite a conexao com o banco de dados
conexao = mysql.connector.connect(user='root', password='pass', host='127.0.0.1', database='lendas')

# cursor é um objeto que permite executar queries SQL no banco
cursor = conexao.cursor()


# modelo de carro do registro que iremos apagar no banco
modelo =  ['UNINHO CHAVOSO COM ESCADA NO TETO']

# query SQL que iremos executar no banco para deletar o registro de um modelo especifico
# repare na variavel '%s', ela ira receber o valor da variavel 'modelo'
query = """ DELETE FROM carros WHERE modelo = %s """

# objeto cursor armazena em memoria (staging) a query junto com o dado da variavel 'modelo' 
cursor.execute(query, modelo)

# o objeto conexao pega todas as queries armazenadas em memoria 
# e executam as alterações permanentemente no banco de dados
conexao.commit()

# mata o cursor, reseta todos resultados, apaga todas queries 
# e garante que o objeto cursor nao possui mais nenhuma referencia ao objeto conexao
cursor.close()

# mata a conexao com o banco de dados
conexao.close()