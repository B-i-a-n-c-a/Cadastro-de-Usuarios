from flask import Flask, render_template, request
from func import Funcoes
from flask_sqlalchemy import SQLAlchemy 
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastrados2.db'
db = SQLAlchemy(app)

app = Flask(__name__)

class ConfigRotas:

    def __init__(self, flask_app):
        self.app = flask_app

    class Usuario(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(80), nullable=False)
        sobrenome = db.Column(db.String(80), nullable=False)
        data_nasc = db.Column(db.Date, nullable=False)
        cpf = db.Column(db.String(11), nullable=False)
        email = db.Column(db.String(120), nullable=False)
        senha = db.Column(db.String(120), nullable=False)
        nome_usuario = db.Column(db.String(80), nullable=False)


    @app.route('/')
    def exibir_form():
        return render_template('formulario.htlm')

    @app.route('/cadastra', methods=['POST'])
    def rota_cad(self):
        dados ={ 
            'nome': request.form.get('nome'),
            'sobrenome': request.form.get('sobrenome'),
            'data_nascimento': request.form.get('data_nascimento'),
            'cpf': request.form.get('cpf'),
            'email': request.form.get('email'),
            'senha': request.form.get('senha'),
            'nome_usuario': request.form.get('nome_usuario')
        }    
    
        novo_cadastro = self.Usuario(**dados)
        db.session.add(novo_cadastro)
        db.session.commit()

    @app.route('/imprime_cadastros', methods=['GET'])
    def rota_impressao(self):
        usuario = self.Usuario.query.order_by(self.Usuario.nome, self.Usuario.cpf).all() #ordem de impressao
        if db: 
            return db.session.query(self.Usuario).all()
        for usuario in self.Usuario:
            nome_completo = f"{usuario.nome} {usuario.sobrenome}"
            print(f"Nome Completo: {nome_completo}, Data de Nascimento: {usuario.data_nasc}, "
              f"CPF: {usuario.cpf}, Email: {usuario.email}, Nome de usuário: {usuario.nome_usuario}")
    
    @app.route('/excluir_usuario', methods=['GET', 'POST'])
    def rota_excluir(self):
        valida_cpf = r'^\d{11}$'
        valida_email = r'^[\w-]+@[a-z\d]+\.[\w]{3}$'
        entrada_usuario = request.form.get('entrada_usuario')
        if re.match(valida_email, entrada_usuario):
            usuario = self.Usuario.query.filter_by(email=self.dados['email']).first()
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
        elif re.match(valida_cpf, entrada_usuario):
            usuario = self.Usuario.query.filter_by(email=self.dados['cpf']).first()
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
        else:
            return 'O dado informado nao é um CPF e nem email'