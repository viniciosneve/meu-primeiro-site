from flask import redirect, render_template, request, session, Blueprint, Response
from App.model import tables
from App import app, db
import random



app.secret_key= 'asadd'
User= tables.User
Publi= tables.Publi
#registrando_blueprint_user= Blueprint('User', __name__)
#registrando_blueprint_publi= Blueprint('Publi', __name__)
email_usuario_logado= None  #Email do usuario.
nome_usuario_logado= None   #Nome do usuario.
preenchimento= False        #Caso o usuario não preencha todas as opções.
mostrar_lista= False        #Apreseta uma lista do nome de todos o usuarios.
logado= False               #Para verificar se ja tem um usuario logado.
aviso= False                #Para avisar ao usuario se tem algo de errado.

R= 250
G= 250
B= 250


#================== SE TA FUNCIONANDO NÃO MEXE


#pagina inicial do site, que aparece quando o ususario não está logado e apenas para os que não estão logado.
@app.route('/site/')
def primaira_pagina():
    global logado
    a= User.query.all()
    for c in a:
        db.session.delete(c)
        db.session.commit()
    db.update(User)
    a= Publi.query.all()
    for c in a:
        db.session.delete(c)
        db.session.commit()
    db.update(Publi)
    if logado == True:
        return redirect(f'/site/logado/{nome_usuario_logado}/')
    
    return render_template('inicio.html')


#==================


# Pagina feita para os usuario fazer o login no site.
@app.route('/site/login/')
def pagina_de_loguin():
    global logado, aviso

    aviso= False

    if logado == True:
        return redirect(f'/site/logado/{nome_usuario_logado}/')
    return render_template('login.html', aviso= aviso)


#==================


# pagina para o usuario fazer o cadastro para poder logar no site.
@app.route('/site/cadastro/')
def pagina_de_cadastro():
    global logado
    
    if logado == True:
        return redirect(f'/site/logado/{nome_usuario_logado}/')
    return render_template(

        'criando_login.html',
        aviso= aviso,
        preenchimento= preenchimento,

        )


#==================


# Esta função é para verificar se o login colocado para criar a conta existe ou não, combinando com a função de cima.
@app.route("/site/check_criate_login/", methods= ['POST'])
def verificando_novo_usuario():
    checando_usuario= User.query.all()
    global aviso, preenchimento, email_usuario_logado
    info_perfil= session.get(f'{db.session.query(User).filter(User.email == email_usuario_logado).all()}')
    preenchimento= False
    aviso= False

    password= request.form['senha']
    email=    request.form['login']
    name=     request.form['nome']
    

    if password == '' or name == '' or email == '':
        #Caso o usuario esqueça de preencher toda a parte do cadastro
        preenchimento= True
        return redirect('/site/cadastro/')
    
    for checando in checando_usuario:
        if checando.email == email:
            aviso= True
            return redirect('/site/cadastro/')
        
    usuario= User(
        password= password,
        email=    email,
        name=     name,
    )

    db.session.add(usuario)
    db.session.commit()
    session.update()

    

    preenchimento= False
    aviso= False

    return redirect('/site/cadastro/')


#===================


# Esta função é para verificar se o login e a senha do usuario existe.
@app.route('/site/chack_user/', methods= ['POST'])
def verificando_usuario():
    global aviso, logado, nome_usuario_logado, R, G, B, mostrar_lista, email_usuario_logado
    checando_usuario= User.query.all()
    aviso= False

    login= request.form["login"]
    senha= request.form["senha"]

    for usuario in checando_usuario:

        if usuario.email == login and usuario.password == senha:

            if logado == False:

                email_usuario_logado= usuario.email
                nome_usuario_logado= usuario.name

                aviso= False
                logado= True
                return redirect(f'/site/logado/{nome_usuario_logado}')
        
    aviso= True
    logado= False
    return redirect('/site/login/')


#===================


# Site acessado apenas pelas pessoas que tem um registro no site, combinando com a função de cima.
@app.route('/site/logado/<nome>/')
def Logado(nome= nome_usuario_logado):
    global logado, mostrar_lista, R, G, B
    lista_usuarios= User.query.all()
    lista_publicacao= Publi.query.all()

    if logado == False:
        return redirect('/site/')
    
    return render_template('logado.html',
        lista_usuarios= lista_usuarios,
        lista_publicacao= lista_publicacao,
        mostrar_lista= mostrar_lista,
        R= R, G= G, B= B
        )


#Funcionalida-des a cima feito para o site logado.


#Um botão feito para deslogar o usuario e impedir o acesso ao site de cima.
@app.route('/site/deslogando/conta/', methods=['GET'])
def Deslogando():
    global logado, nome_usuario_logado, email_usuario_logado
    session.update()
    logado= False
    nome_usuario_logado= None
    email_usuario_logado= None
    return redirect('/site/')

#===================


#Um botão feito para mostrar uma lista dos usuarios existentes.
@app.route('/site/lista/usuarios/', methods=["GET"])
def Lista_usuarios():
    global mostrar_lista
    if mostrar_lista == False:
        mostrar_lista= True
    elif mostrar_lista == True:
        mostrar_lista= False
    return redirect(f'/site/logado/{nome_usuario_logado}/')


#===================


#Botão para mudar a cor de fundo do site.
@app.route('/site/mudando/cor/', methods=['GET'])
def Mudando_cor():
    global R, G, B
    R= random.randint(0, 255)
    G= random.randint(0, 255)
    B= random.randint(0, 255)

    return redirect(f'/site/logado/{nome_usuario_logado}')


#===================


#Função que recebe a publicação do usuario.
@app.route('/site/pegando/publi/usuario/', methods= ['POST', 'GET'])
def Recolhendo_publicacao():
    post_usuario= request.form['publi']

    id_usuario_publi= db.session.query(User).filter(User.email == email_usuario_logado).first()
    id_usuario= id_usuario_publi.id

    publicacao= Publi(
        post= post_usuario,
        id_usuario= id_usuario
    )

    db.session.add(publicacao)
    db.session.commit()
    return redirect(f'/site/logado/{nome_usuario_logado}')
#Funcionalida-des a cima feito para o site logado.