#importamos a biblioteca de conexao com banco de dados do tipo mysql
import mysql.connector

# cria um objeto que permite a conexao com o banco de dados
conexao = mysql.connector.connect(user='root', password='pass', host='127.0.0.1', database='lendas')

# cursor é um objeto que permite executar queries SQL no banco
cursor = conexao.cursor()


# modelo de carro que iremos buscar no banco
modelo =  ['911 Twin Turbo']

# query SQL que iremos executar no banco para retornar um modelo especifico
# repare na variavel '%s', ela ira receber o valor da variavel 'modelo'
query = """ SELECT * FROM carros WHERE modelo = %s """

# objeto cursor armazena em memoria (staging) a query junto com o dado da variavel 'modelo'
cursor.execute(query, modelo)

# o objeto conexao retorna todos os resultados da query executada anteriormente
# e armazena na variavel resultado
resultado = cursor.fetchall()

#imprimindo resultado
print(resultado)

# mata o cursor, reseta todos resultados, apaga todas queries
# e garante que o objeto cursor nao possui mais nenhuma referencia ao objeto conexao
cursor.close()

# mata a conexao com o banco de dados
conexao.close()