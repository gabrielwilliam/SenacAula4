#nova versão
from flask import Flask, render_template, request

app = Flask(__name__)

#rota para a pagina principal da aplicação
@app.route('/')
def start():
    return "Página Inicial"

#rota para pagina de produtod
@app.route("/produtos")
def produto():
    return "<h1>Minha pagina de produtos</h1>"

@app.route('/sobre')
def sobre():
    return "<h2>PAGINA DE SOBRE</h2>"

    
#enviando informações para o arquivo html (Templates)
@app.route('/cadastro')
def cadastro():
    titulo = 'Cadastro de usuário'
    descricao = 'Formulário que permite o cadastro de usuários do sistema'
    return render_template('app.html',titulo=titulo,descricao=descricao)



#Login de usuário
@app.route('/login', methods=["GET","POST"])
def login():
    
    if request.method == "GET":
        return render_template('app.html')
    else:
        usuario = request.form.get("user")

        if(usuario == 'gabriel.william@webba.com.br'):
            result = "<h1>Usuário Logado com sucesso!<h1>"
        else:
            result = "<h1>Ocorreu um erro no login</h1>"
    
    return result