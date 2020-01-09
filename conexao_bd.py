import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    passwd='senha',
    database='usuario'
)
cursor = con.cursor()
'''
Criar tabela
cursor.execute("create table st_user(cpf int(11),"
               "nome varchar(255),"
               "sobrenome varchar(255),"
               "idade int(3),"
               "primary key(cpf))")
'''


def insert(cpf, nome, sobrenome, idade):
    sql = "INSERT INTO st_user (cpf, nome, sobrenome, idade) VALUES (%s, %s, %s, %s)"
    val = (cpf, nome, sobrenome, idade)
    cursor.execute(sql, val)
    con.commit()
    return cursor.rowcount


def update(option, new_value, cpf_old):
    field = ''
    if option == 1 or option == 4:
        new = int(new_value)
    if option == 1:
        field = 'cpf'
    elif option == 2:
        field = 'nome'
    elif option == 3:
        field = 'sobrenome'
    elif option == 4:
        field = 'idade'
    else:
        return 0
    sql = "UPDATE st_user SET " + field + "= %s WHERE cpf = %s"
    val = (new_value, cpf_old)
    cursor.execute(sql, val)
    con.commit()
    return cursor.rowcount


def delete(cpf_old):
    sql = "DELETE FROM st_user WHERE cpf = %s"
    val = (cpf_old)
    cursor.execute(sql, val)
    con.commit()
    return cursor.rowcount


control = input("Para comecar, digite 'sim' para finalizar digite 'sair'")
while control != 'sair':
    cpf = ''
    nome = ''
    sobrenome = ''
    idade = ''
    print("Crud")
    option = int(input('Escolha entre as opçoes:\n '
                       '1 - Inserir dados\n '
                       '2 - Alterar dados\n '
                       '3 - Excluir dados\n '
                       '4 - Listar dados :\n'))

    if option == 1:
        cpf = input('Insira o cpf (apenas numeros): ')
        nome = input('Insira o nome: ')
        sobrenome = input('Insira o sobrenome: ')
        idade = input('Insira a idade: ')
        var = insert(cpf, nome, sobrenome, idade)
        if var == 1:
            print("inserido com sucesso")
    elif option == 2:
        option2 = int(input("Insira a opç~ao que deseja alterar: 1 - Cpf, 2 - Nome, 3 - Sobrenome, 4 - Idade"))
        new_value = input('Insirar o valor a ser alterado')
        cpf_old = input("Insira Cpf cadastrado")
        var = update(option2, new_value, cpf_old)
        if var == 1:
            print("alterado com sucesso")

    elif option == 3:
        cpf_old = input("Insira o cpf a ser exluido")
        var = delete(cpf_old)
        if var == 1:
            print("excluido com sucesso")

    elif option == 4:
        query = "SELECT * FROM st_user"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print("cpf = ", row[0], )
            print("nome = ", row[1])
            print("sobrenome  = ", row[2])
            print("idade  = ", row[3], "\n")

    else:
        print("Opç~ao invalida")

    control = input("Para continuar, digite 'sim' para finalizar digite 'sair'")


