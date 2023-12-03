import sqlite3

banco = sqlite3.connect('cadastrados2.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE cadastrados(nome text, sobrenome text, data_nasc date,                                  cpf text, email text, senha text, nome_usuario text)")

#cursor.execute("INSERT INTO cadastrados VALUES('Jao', 'Silva', 03-12-90, '198.097.643-94', 'jao123@gmail.com', '123456', 'jao234')")

#banco.commit()
cursor.execute("SELECT * FROM cadastrados")
print(cursor.fetchall())