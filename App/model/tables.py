from App import db
class User(db.Model):
    #Uma classe voltada para o usuario

    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)#id
    password= db.Column(db.String) #Senha
    name= db.Column(db.String) #Nome do usuario
    email= db.Column(db.String, unique= True) #login do usuario
    posts= db.relationship('Publi', backref= 'user', lazy= True)

    def __init__(self, password, name, email):
        self.password= password
        self.name= name
        self.email= email

    def __repr__(self):
        return f'Usuario: {self.name}'

    #publi = db.relationship('Publi', backref="users")

class Publi(db.Model):
    #Uma class voltada para a criação da publicação do usuario.

    __tablename__= "publis"
    #user= db.relationship(User)#Conectando o post com o usuario
    id= db.Column(db.Integer, primary_key= True, autoincrement= True)# O id do post.
    id_usuario= db.Column(db.Integer, db.ForeignKey(User.id), nullable= False)# Conectando o post com o id do usuario que o crou.
    post= db.Column(db.String)# O post.

    def __init__(self, post, id_usuario):
        self.post= post
        self.id_usuario= id_usuario
    
    def __repr__(self):
        return f'Esse post é do usuario que contem o ID {self.id_usuario}'
    
    #User.publis=db.Constraint(db.select(id).where(id_usuario == User.id).correlate(User))
