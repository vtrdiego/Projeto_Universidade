#==== CONEXÃO COM BD ====

import mysql.connector

conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='SGA'
)

x=conexao.cursor()
print(conexao)

#===== CRIAÇÃO DA TABELA SGA =====

#x.execute('create database SGA')

#===== CRIAÇÃO DA TABELA ACESSO E ALUNO =====

'''x.execute('create table acesso(cod_usuario int(50) primary key,\
usuario varchar(50),senha varchar(30))')'''

x.execute('insert into acesso(cod_usuario,usuario,senha)values("1","admin","123")')
conexao.commit()

'''x.execute('create table aluno(nome varchar(100),data_nascimento varchar(11),\
rg varchar(20),cpf varchar(20),endereco varchar(100),estado_civil varchar(15),\
sexo varchar(2),telefone varchar(13),email varchar(100),curso varchar(50),\
data_matricula varchar(11),ra int(15) primary key, turno varchar(10))')'''


