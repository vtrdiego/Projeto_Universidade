#IMPORTANDO MYSQL E BIBLIOTECAS========
import mysql.connector as mysql
import tkinter.messagebox as Messagebox
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#==================================================== TELA DE LOGIN =================================================

#FUNÇÃO DE VERIFICAR LOGIN==============

def acessar():
    usuario=caixa_usuario.get()
    senha=caixa_senha.get()

    if usuario=='' or senha=='':
        avisoLogin.place(x=10000)
        avisoVazio.place(x=165,y=275)
    else:
        conexaoUm=mysql.connect(host='localhost',user='root',password='',database='sga')
        cursorUm=conexaoUm.cursor()
        cursorUm.execute("select * from acesso where usuario=('"+usuario+"')")
        colunaUm=cursorUm.fetchall()

        conexaoDois=mysql.connect(host='localhost',user='root',password='',database='sga')
        cursorDois=conexaoDois.cursor()
        cursorDois.execute("select * from acesso where senha=('"+senha+"')")
        colunaDois=cursorDois.fetchall()

        if colunaUm==[] or colunaDois==[]:
            avisoVazio.place(x=10000)
            avisoLogin.place(x=145,y=275)
        else:
            tela_opcoes()
            conexaoUm.close()
            conexaoDois.close()

#JANELA===============
janela=Tk()
janela.title("ACESSO ADMINISTRATIVO (SGA)")
janela.geometry('500x400')
janela['bg']='#e6b800'
janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
janela.iconbitmap(default='logos/icone.ico')

#Widgets===============
LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
LabelTopo.place(x=False,y=False)

LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
LabelEsquerdo.place(x=False,y=69)

#LOGOS========================

logo=PhotoImage(file='logos/logo.png')
logoLabel=Label(janela, image=logo, bg='#2B59BD')
logoLabel.place(x=155,y=2)

#TEXTOS=====================

texto_sistema=Label(
    LabelEsquerdo,
    text='SISTEMA DE GERENCIAMENTO ACADÊMICO',
    bg='#cce6ff',
    font=('times news roman',10)
)
texto_sistema.place(x=110,y=10)

texto_usuario=Label(
    LabelEsquerdo,
    text='USUÁRIO:',
    bg='#cce6ff',
    font=('times news roman',15)
    )
texto_usuario.place(x=200,y=65)

caixa_usuario=ttk.Entry(LabelEsquerdo, width=50)
caixa_usuario.place(x=100,y=100)

texto_senha=Label(
    LabelEsquerdo,
    text='SENHA:',
    bg='#cce6ff',
    font=('times news roman',15)
    )
texto_senha.place(x=210,y=150)

avisoVazio=Label(LabelEsquerdo,text='Preencha os campos!',fg='RED',font=('times news roman',12),bg='#cce6ff')
avisoLogin=Label(LabelEsquerdo,text='Usuário ou senha incorreto!',fg='RED',font=('times news roman',12),bg='#cce6ff')

caixa_senha=ttk.Entry(LabelEsquerdo,width=50,show='*')
caixa_senha.place(x=100,y=185)

#BOTÃO ENTRAR=========

botao_login=Button(LabelEsquerdo,text='ACESSAR', width=20,command=acessar)
botao_login.place(x=170,y=230)

botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
botao_sair.place(x=410,y=285)

#///////////////////////////////////////////// FIM DA TELA DE LOGIN ///////////////////////////////////////////////


#=============================================== TELA DE OPÇÕES ==================================================
        
def tela_opcoes():
    
    #JANELA ==============
    global janela
    janela.destroy()
    janela=Tk()
    janela.title("ACESSO ADMINISTRATIVO (SGA)")
    janela.geometry('500x400')
    janela['bg']='#e6b800'
    janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
    janela.iconbitmap(default='logos/icone.ico')

    #WIDGETS===============
    LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
    LabelTopo.place(x=False,y=False)

    LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
    LabelEsquerdo.place(x=False,y=69)

    #LOGO========================

    global logo
    logo=PhotoImage(file='logos/logo.png')
    logoLabel=Label(janela, image=logo, bg='#2B59BD')
    logoLabel.place(x=155,y=2)

    #TEXTOS E BOTÕES =================

    texto_sistema=Label(
    LabelEsquerdo,
    text='SISTEMA DE GERENCIAMENTO ACADÊMICO',
    bg='#cce6ff',
    font=('times news roman',10)
    )
    texto_sistema.place(x=110,y=10)

    texto_registrar=Label(
    LabelEsquerdo,
    text='REGISTRAR NOVO ALUNO:',
    bg='#cce6ff',
    font=('times news roman',11)
    )
    texto_registrar.place(x=150,y=60)

    botao_registrar=Button(LabelEsquerdo,text='REGISTRAR',width=15,command=tela_registrar)
    botao_registrar.place(x=185,y=93)

    texto_consultar=Label(
    LabelEsquerdo,
    text='CONSULTAR REGISTRO:',
    bg='#cce6ff',
    font=('times news roman',11)
    )
    texto_consultar.place(x=155,y=140)

    botao_consultar=Button(LabelEsquerdo,text='CONSULTAR',width=15,command=tela_consulta)
    botao_consultar.place(x=185,y=173)

    texto_alterar=Label(
    LabelEsquerdo,
    text='CONFIGURAÇÃO DE ACESSO:',
    bg='#cce6ff',
    font=('times news roman',11)
    )
    texto_alterar.place(x=135,y=220)

    botao_alterar=Button(LabelEsquerdo,text='CONFIGURAR',width=15,command=tela_configurar)
    botao_alterar.place(x=185,y=253)

    botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
    botao_sair.place(x=410,y=285)

#////////////////////////////////////////// FIM TELA DE OPÇÕES //////////////////////////////////////////////


#========================================== TELA DE MATRÍCULA ================================================

def tela_registrar():

    #======= SUB-FUNÇÃO MYSQL REGISTRAR ======

    def rigistrar_NovoAluno():
        nome=caixa_nome.get()
        data=caixa_data.get()
        rg=caixa_rg.get()
        cpf=caixa_cpf.get()
        endereco=caixa_endereco.get()
        estado_civil=ver_civil.get()
        sexo=ver_sexo.get()
        telefone=caixa_telefone.get()
        email=caixa_email.get()
        curso=caixa_curso.get()
        data_matricula=caixa_dataMatricula.get()
        ra=caixa_ra.get()
        turno=ver_turno.get()

        if nome=='' or data=='' or rg=='' or cpf=='' or endereco=='' or estado_civil=='------------' or sexo=='-' or telefone=='' or email=='' or curso=='' or data_matricula=='' or ra=='' or turno=='------------':
            Messagebox.showinfo('AVISO','Preencha todos os campos!')
        else:
            conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
            cursor=conexao.cursor()
            cursor.execute("select * from aluno where ra=('"+ra+"')")
            colunas=cursor.fetchall()
            if colunas==[]:
                conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
                cursor=conexao.cursor()
                cursor.execute("insert into aluno values('"+nome+"','"+data+"','"+rg+"','"+cpf+"','"+endereco+"','"+estado_civil+"','"+sexo+"','"+telefone+"','"+email+"','"+curso+"','"+data_matricula+"','"+ra+"','"+turno+"')")
                cursor.execute('commit')
                Messagebox.showinfo('AVISO!','Aluno registrado com sucesso!')
                tela_registrar()
                conexao.close
            else:
                Messagebox.showinfo('AVISO','RA já cadastrada, informe outra!')

    #JANELA REGISTRAR============
    global janela
    janela.destroy()
    janela=Tk()
    janela.title("ACESSO ADMINISTRATIVO (SGA)")
    janela.geometry('500x400')
    janela['bg']='#e6b800'
    janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
    janela.iconbitmap(default='logos/icone.ico')

    #WIDGETS===============
    LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
    LabelTopo.place(x=False,y=False)

    LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
    LabelEsquerdo.place(x=False,y=69)

    #LOGO========================

    global logo
    logo=PhotoImage(file='logos/logo.png')
    logoLabel=Label(janela, image=logo, bg='#2B59BD')
    logoLabel.place(x=155,y=2)

    #TEXTOS, CAIXAS E BOTÕES=====================

    texto_matricula=Label(
        LabelEsquerdo,
        text='MATRICULAR NOVO ALUNO',
        bg='#cce6ff',
        font=('times news roman',10)
    )
    texto_matricula.place(x=160,y=10)

    texto_nome=Label(
        LabelEsquerdo,
        text='NOME:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_nome.place(x=10,y=45)
    caixa_nome=ttk.Entry(LabelEsquerdo,width=70)
    caixa_nome.place(x=50,y=45)

    texto_data=Label(
        LabelEsquerdo,
        text='DATA DE NASCIMENTO:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_data.place(x=10,y=75)
    caixa_data=ttk.Entry(LabelEsquerdo,width=10)
    caixa_data.place(x=135,y=75)

    texto_rg=Label(
        LabelEsquerdo,
        text='RG:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_rg.place(x=229,y=75)
    caixa_rg=ttk.Entry(LabelEsquerdo,width=13)
    caixa_rg.place(x=254,y=75)

    texto_cpf=Label(
        LabelEsquerdo,
        text='CPF:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_cpf.place(x=362,y=75)
    caixa_cpf=ttk.Entry(LabelEsquerdo,width=13)
    caixa_cpf.place(x=392,y=75)

    texto_endereco=Label(
        LabelEsquerdo,
        text='ENDEREÇO:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_endereco.place(x=10,y=105)
    caixa_endereco=ttk.Entry(LabelEsquerdo,width=66)
    caixa_endereco.place(x=75,y=105)

    texto_civil=Label(
        LabelEsquerdo,
        text='ESTADO CIVIL:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_civil.place(x=10,y=135)

    lista_civil=["------------","Solteiro(a)","Casado(a)","Divorciado(a)","Viúvo(a)"]
    ver_civil=StringVar()
    ver_civil.set(lista_civil[0])
    opcao_civil=ttk.OptionMenu(LabelEsquerdo,ver_civil,*lista_civil)
    opcao_civil.place(x=90,y=133)

    texto_sexo=Label(
        LabelEsquerdo,
        text='SEXO:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_sexo.place(x=210,y=135)
    lista_sexo=["-","M","F"]
    ver_sexo=StringVar()
    ver_sexo.set(lista_sexo[0])
    opcao_sexo=ttk.OptionMenu(LabelEsquerdo,ver_sexo,*lista_sexo)
    opcao_sexo.place(x=250,y=133)

    texto_telefone=Label(
        LabelEsquerdo,
        text='TELEFONE:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_telefone.place(x=315,y=135)
    caixa_telefone=ttk.Entry(LabelEsquerdo,width=15)
    caixa_telefone.place(x=380,y=135)

    texto_email=Label(
        LabelEsquerdo,
        text='EMAIL:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_email.place(x=10,y=165)
    caixa_email=ttk.Entry(LabelEsquerdo,width=70)
    caixa_email.place(x=50,y=165)

    texto_curso=Label(
        LabelEsquerdo,
        text='CURSO:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_curso.place(x=10,y=197)
    caixa_curso=ttk.Entry(LabelEsquerdo,width=35)
    caixa_curso.place(x=55,y=197)

    texto_dataMatricula=Label(
        LabelEsquerdo,
        text='DATA DE MATRÍCULA:',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_dataMatricula.place(x=290,y=197)
    caixa_dataMatricula=ttk.Entry(LabelEsquerdo,width=10)
    caixa_dataMatricula.place(x=410,y=197)

    texto_ra=Label(
        LabelEsquerdo,
        text='REGISTRO ACADÊMICO (RA):',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_ra.place(x=10,y=231)
    caixa_ra=ttk.Entry(LabelEsquerdo,width=17)
    caixa_ra.place(x=162,y=231)

    texto_turno=Label(
        LabelEsquerdo,
        text='TURNO:',
        bg='#cce6ff',
        font=('times news roman',8)  
    )
    texto_turno.place(x=335,y=231)
    lista_turno=["------------","Manhã","Tarde","Noite","Integral"]
    ver_turno=StringVar()
    ver_turno.set(lista_turno[0])
    opcao_turno=ttk.OptionMenu(LabelEsquerdo,ver_turno,*lista_turno)
    opcao_turno.place(x=380,y=231)

    botao_voltar=Button(LabelEsquerdo,text='VOLTAR',width=10,command=tela_opcoes)
    botao_voltar.place(x=10,y=285)

    botao_matricular=Button(LabelEsquerdo,text='CADASTRAR',width=10,bg='#ccffe6',command=rigistrar_NovoAluno)
    botao_matricular.place(x=155,y=285)

    botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
    botao_sair.place(x=410,y=285)

    botao_limpar=Button(LabelEsquerdo,text='LIMPAR',width=10,bg='#ffffcc',command=tela_registrar)
    botao_limpar.place(x=265,y=285)

#////////////////////////////////////// FIM DA TELA DE MATRÍCULA /////////////////////////////////////////////


#========================================= TELA DE CONSULTA ====================================================

def tela_consulta():

    #==== SUB-FUNÇÃO DELETAR ALUNO ====
    
    def deletar_aluno():
        con=mysql.connect(host='localhost',user='root',password='',database='SGA')
        cursor=con.cursor()
        cursor.execute("delete from aluno where ra=('"+ra+"')")                                  
        cursor.execute('commit')
        Messagebox.showinfo('AVISO!','Registro deletado com sucesso!')
        tela_consulta()
        con.close

    #==== SUB-FUNÇÃO DELETAR TODOS OS ALUNOS ====
        
    def deletar_todos_alunos():
        con=mysql.connect(host='localhost',user='root',password='',database='SGA')
        cursor=con.cursor()
        cursor.execute('delete from aluno where ra >= 0')                                  
        cursor.execute('commit')
        Messagebox.showinfo('AVISO!','Todos os registros foram deletados!')
        tela_consulta()
        con.close

    #==== SUB-FUNÇÃO MYSQL CONSULTA RA ====

    def consultar_ra():
        global ra
        ra=caixa_consulta_registro.get()

        if ra=='':
          Messagebox.showinfo('AVISO!','Preencha o campo!')
        else:
            conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
            cursor=conexao.cursor()
            cursor.execute("select * from aluno where ra=('"+ra+"')")
            colunas=cursor.fetchall()
            if colunas==[]:
                Messagebox.showinfo('AVISO!','RA não encontrado!')
            else:
                for c in colunas: 
                    insertData='NOME:  '+str(c[0])+'    -    DATA DE NASCIMENTO:  '+str(c[1])+'   -     RG:  '+str(c[2])+'    -    CPF:  '+str(c[3])+'    -    ENDEREÇO:  '+str(c[4])+'    -    ESTADO CIVIL:  '+str(c[5])+'    -    SEXO:  '+str(c[6])+'    -    TELEFONE:  '+str(c[7])+'    -    EMAIL:  '+str(c[8])+'    -    CURSO:  '+str(c[9])+'    -    DATA DE MATRÍCULA:  '+str(c[10])+'    -    RA:  '+str(c[11])+'    -    TURNO:  '+str(c[12]+'         ')
                    caixa_lista.insert(caixa_lista.size(),insertData)
                conexao.close()

                botao_deletar_todos.place(x=10000)
                botao_limpar_todos.place(x=10000)

                botao_alterarCurso.place(x=120,y=285)
                botao_deletar_aluno.place(x=210,y=285)
                botao_limpar_aluno.place(x=300,y=285)


    #====== SUB-FUNÇÃO DE CONSULTAR TODOS OS REGISTROS ======

    def consultar_todosRegistros():
        
        conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
        cursor=conexao.cursor()
        cursor.execute("select * from aluno")                            
        linhas=cursor.fetchall()
        
        if linhas==[]:
            Messagebox.showinfo('AVISO!','Não há alunos matriculados!')
        else:
            for c in linhas:
                insertData='NOME:  '+str(c[0])+'    -    DATA DE NASCIMENTO:  '+str(c[1])+'   -     RG:  '+str(c[2])+'    -    CPF:  '+str(c[3])+'    -    ENDEREÇO:  '+str(c[4])+'    -    ESTADO CIVIL:  '+str(c[5])+'    -    SEXO:  '+str(c[6])+'    -    TELEFONE:  '+str(c[7])+'    -    EMAIL:  '+str(c[8])+'    -    CURSO:  '+str(c[9])+'    -    DATA DE MATRÍCULA:  '+str(c[10])+'    -    RA:  '+str(c[11])+'    -    TURNO:  '+str(c[12]+'         ')
                caixa_lista.insert(caixa_lista.size()+1, insertData)
            conexao.close()

            botao_alterarCurso.place(x=10000)
            botao_deletar_aluno.place(x=10000)
            botao_limpar_aluno.place(x=10000)
        
            botao_deletar_todos.place(x=150,y=285)
            botao_limpar_todos.place(x=260,y=285)

    #JANELA ===============
            
    global janela
    janela.destroy()
    janela=Tk()
    janela.title("ACESSO ADMINISTRATIVO (SGA)")
    janela.geometry('500x400')
    janela['bg']='#e6b800'
    janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
    janela.iconbitmap(default='logos/icone.ico')

    #WIDGETS===============
    LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
    LabelTopo.place(x=False,y=False)

    LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
    LabelEsquerdo.place(x=False,y=69)

    #LOGO========================

    global logo
    logo=PhotoImage(file='logos/logo.png')
    logoLabel=Label(janela, image=logo, bg='#2B59BD')
    logoLabel.place(x=155,y=2)

    texto_sistema=Label(
    LabelEsquerdo,
    text='CONSULTA DE REGISTRO',
    bg='#cce6ff',
    font=('times news roman',10)
    )
    texto_sistema.place(x=165,y=10)

    #==== TEXTOS,BOTÕES E LISTA ====
    
    botao_alterarCurso=Button(LabelEsquerdo,text='ALTERAR',width=10,bg='#ccffe6',command=tela_novoCurso)
    botao_deletar_aluno=Button(LabelEsquerdo,text='DELETAR',width=10,bg='#ffcccc',command=deletar_aluno)
    botao_limpar_aluno=Button(LabelEsquerdo,text='LIMPAR',width=10,bg='#ffffcc',command=tela_consulta)
    botao_deletar_todos=Button(LabelEsquerdo,text='DELETAR',width=12,bg='#ffcccc',command=deletar_todos_alunos)
    botao_limpar_todos=Button(LabelEsquerdo,text='LIMPAR',width=12,bg='#ffffcc',command=tela_consulta)

    texto_consulta_registro=Label(
        LabelEsquerdo,
        text='RA DO ALUNO(A):',
        bg='#cce6ff',
        font=('times news roman',8)
    )
    texto_consulta_registro.place(x=35,y=40)
    caixa_consulta_registro=ttk.Entry(LabelEsquerdo,width=20)
    caixa_consulta_registro.place(x=20,y=60)

    botao_consultar=Button(LabelEsquerdo,width=12,text='CONSULTAR',command=consultar_ra)
    botao_consultar.place(x=150,y=57)

    botao_todos=Button(LabelEsquerdo,width=25,text='EXIBIR TODOS OS REGISTROS',command=consultar_todosRegistros)
    botao_todos.place(x=280,y=57)

    caixa_lista=Listbox(LabelEsquerdo,width=79,height=10,relief=RIDGE,borderwidth=2)
    caixa_lista.place(x=10,y=95)

    barraUm=ttk.Scrollbar(LabelEsquerdo, orient='vertical')
    caixa_lista.configure(yscroll=barraUm.set)
    barraUm.place(x=469.5,y=98,relheight=0.45)

    barraDois=ttk.Scrollbar(LabelEsquerdo, orient='horizontal')
    caixa_lista.configure(xscroll=barraDois.set)
    barraDois.place(x=13,y=241,relwidth=0.95)

    botao_voltar=Button(LabelEsquerdo,text='VOLTAR',width=10,command=tela_opcoes)
    botao_voltar.place(x=10,y=285)

    botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
    botao_sair.place(x=410,y=285)

#///////////////////////////////////////////// FIM DA TELA DE CONSULTA ////////////////////////////////////////////


#=============================================== TELA ALTERAR CURSO =============================================

def tela_novoCurso():
   
    #=== SUB-FUNÇÃO ALTERAR CURSO =====

    def alterar_curso():
        curso=caixa_curso.get()
        data_matricula=caixa_data.get()
        turno=ver_turno.get()

        if curso=='' or data_matricula=='' or turno=='------------':
            Messagebox.showinfo('AVISO!','Preencha todos os campos!')
        else:
            conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
            cursor=conexao.cursor()
            cursor.execute("update aluno set curso=('"+curso+"')where ra=('"+ra+"')")
            cursor.execute("update aluno set data_matricula=('"+data_matricula+"')where ra=('"+ra+"')")
            cursor.execute("update aluno set turno=('"+turno+"')where ra=('"+ra+"')")
            cursor.execute('commit')
            Messagebox.showinfo('AVISO!','Curso alterado com sucesso!')
            tela_consulta()
            conexao.close
        
    #JANELA ===============
            
    global janela
    janela.destroy()
    janela=Tk()
    janela.title("ACESSO ADMINISTRATIVO (SGA)")
    janela.geometry('500x400')
    janela['bg']='#e6b800'
    janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
    janela.iconbitmap(default='logos/icone.ico')

    #WIDGETS===============
    LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
    LabelTopo.place(x=False,y=False)

    LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
    LabelEsquerdo.place(x=False,y=69)

    #LOGO========================

    global logo
    logo=PhotoImage(file='logos/logo.png')
    logoLabel=Label(janela, image=logo, bg='#2B59BD')
    logoLabel.place(x=155,y=2)

    #TEXTOS, CAIXAS E BOTÕES =================

    texto_sistema=Label(
        LabelEsquerdo,
        text='ALTERAR CURSO',
        bg='#cce6ff',
        font=('times news roman',11)
    )
    texto_sistema.place(x=175,y=20)


    texto_curso=Label(
        LabelEsquerdo,
        text='INFORME O NOVO CURSO DO ALUNO(A):',
        bg='#cce6ff',
        font=('times news roman',11)
    )
    texto_curso.place(x=95,y=80)
    caixa_curso=ttk.Entry(LabelEsquerdo,width=35)
    caixa_curso.place(x=130,y=115)

    texto_data=Label(
        LabelEsquerdo,
        text='DATA DE MATRÍCULA:',
        bg='#cce6ff',
        font=('times news roman',11)
    )
    texto_data.place(x=70,y=168)
    caixa_data=ttk.Entry(LabelEsquerdo,width=10)
    caixa_data.place(x=110,y=200)
            
    texto_turno=Label(
        LabelEsquerdo,
        text='TURNO:',
        bg='#cce6ff',
        font=('times news roman',10)  
    )
    texto_turno.place(x=340,y=170)
    lista_turno=["------------","Manhã","Tarde","Noite","Integral"]
    ver_turno=StringVar()
    ver_turno.set(lista_turno[0])
    opcao_turno=ttk.OptionMenu(LabelEsquerdo,ver_turno,*lista_turno)
    opcao_turno.place(x=320,y=200)

    botao_voltar=Button(LabelEsquerdo,text='VOLTAR',width=10,command=tela_consulta)
    botao_voltar.place(x=10,y=285)

    botao_alterar=Button(LabelEsquerdo,text='ALTERAR',width=10,bg='#ccffe6',command=alterar_curso)
    botao_alterar.place(x=155,y=285)

    botao_limpar=Button(LabelEsquerdo,text='LIMPAR',width=10,bg='#ffffcc',command=tela_novoCurso)
    botao_limpar.place(x=265,y=285)

    botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
    botao_sair.place(x=410,y=285)


#////////////////////////////////////////////////// FIM DA TELA NOVO CURSO /////////////////////////////////////////////


#================================================ TELA DE CONFIGURAR ACESSO =============================================

def tela_configurar():

    #==== FUNÇÃO PARA ALTERAR USUÁRIO E SENHA ====
    def alterar_usuario_senha():
        global ra
        usuario=caixa_novoUsuario.get()
        senha=caixa_novaSenha.get()
        cod='1'

        if usuario=='' and senha=='':
                Messagebox.showinfo('AVISO','Preencha um dos campos, ou ambos!')
        else:
            if usuario!='' and senha=='':
                conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
                cursor=conexao.cursor()
                cursor.execute("update acesso set usuario=('"+usuario+"')where cod_usuario=('"+cod+"')")
                cursor.execute('commit')
                Messagebox.showinfo('AVISO!','Usuário alterado com sucesso!')
                conexao.close
                tela_configurar()
            elif usuario=='' and senha!='':
                conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
                cursor=conexao.cursor()
                cursor.execute("update acesso set senha=('"+senha+"')where cod_usuario=('"+cod+"')")
                cursor.execute('commit')
                Messagebox.showinfo('AVISO!','Senha alterada com sucesso!')
                conexao.close
                tela_configurar()
            elif usuario!='' and senha!='':
                conexao=mysql.connect(host='localhost',user='root',password='',database='SGA')
                cursor=conexao.cursor()
                cursor.execute("update acesso set usuario=('"+usuario+"')where cod_usuario=('"+cod+"')")
                cursor.execute("update acesso set senha=('"+senha+"')where cod_usuario=('"+cod+"')")
                cursor.execute('commit')
                Messagebox.showinfo('AVISO!','Usuário e senha alterados com sucesso!')
                conexao.close
                tela_configurar()
                

    #JANELA DE NOVO USUÁRIO E SENHA=======
    global janela
    janela.destroy()
    janela=Tk()
    janela.title("ACESSO ADMINISTRATIVO (SGA)")
    janela.geometry('500x400')
    janela['bg']='#e6b800'
    janela.resizable(width=False, height=False) #Para fixar o tamanho da janela
    janela.iconbitmap(default='logos/icone.ico')

    #WIDGETS===============
    LabelTopo=Frame(janela, width=500, height=62, bg='#2B59BD',relief='raise')
    LabelTopo.place(x=False,y=False)

    LabelEsquerdo=Frame(janela, width=500, height=325, bg='#cce6ff',relief='raise')
    LabelEsquerdo.place(x=False,y=69)

    #LOGO========================

    global logo
    logo=PhotoImage(file='logos/logo.png')
    logoLabel=Label(janela, image=logo, bg='#2B59BD')
    logoLabel.place(x=155,y=2)

    #TEXTOS, CAIXAS E BOTÕES =================

    texto_sistema=Label(
        LabelEsquerdo,
        text='SISTEMA DE GERENCIAMENTO ACADÊMICO',
        bg='#cce6ff',
        font=('times news roman',10)
    )
    texto_sistema.place(x=110,y=10)

    texto_registrar=Label(
        LabelEsquerdo,
        text='ALTERAÇÃO DE ACESSO',
        bg='#cce6ff',
        font=('times news roman',11)
    )
    texto_registrar.place(x=155,y=60)

    texto_informar=Label(
        LabelEsquerdo,
        text='Informe o novo usuário e/ou senha para alteração:',
        bg='#cce6ff',
        font=('times news roman',12),
        fg='BLUE'
    )
    texto_informar.place(x=75,y=100)

    texto_usuario=Label(
        LabelEsquerdo,
        text='NOVO USUÁRIO:',
        bg='#cce6ff',
        font=('times news roman',11),
    )
    texto_usuario.place(x=73,y=160)
    caixa_novoUsuario=ttk.Entry(LabelEsquerdo,width=25)
    caixa_novoUsuario.place(x=53,y=190)

    texto_senha=Label(
        LabelEsquerdo,
        text='NOVA SENHA:',
        bg='#cce6ff',
        font=('times news roman',11),
    )
    texto_senha.place(x=320,y=160)
    caixa_novaSenha=ttk.Entry(LabelEsquerdo,width=25,show='*')
    caixa_novaSenha.place(x=290,y=190)

    botao_voltar=Button(LabelEsquerdo,text='VOLTAR',width=10,command=tela_opcoes)
    botao_voltar.place(x=10,y=285)

    botao_alterar=Button(LabelEsquerdo,text='ALTERAR',width=20,bg='#ccffe6',command=alterar_usuario_senha)
    botao_alterar.place(x=173,y=285)

    botao_sair=Button(LabelEsquerdo,text='SAIR',width=10,command=exit)
    botao_sair.place(x=410,y=285)

#//////////////////////////////////////////////// FIM DA TELA DE CONFIGURAR ACESSO ///////////////////////////////////////////


janela.mainloop()

#FIM//////
