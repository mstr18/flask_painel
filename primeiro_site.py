from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
from Classes.conexoes import Conexoes
import re

#import ipdb import para depuração

app = Flask(__name__)
app.secret_key = 'secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)


#Inicializando classe de validação de usuários. Senhas ainda em plaintext
bd = Conexoes()

@app.route("/")
def home():
    if 'username' in session:
        return redirect(url_for("index"))
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    
    if request.method == "POST":
        # Get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]
        

        # Check if the user exists and the password is correct
        if bd.validUser(username, password):
            session['username'] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html",invalido = "Senha inválida*" )
    else:
        return render_template("login.html")

@app.route("/index")
def index():
     if 'username' in session:
         return render_template("index.html")
     else:
         return render_template("login.html",invalido = "Sessão Expirada, favor logar novamente*" )
     
@app.route("/generic")
def generic():
     if 'username' in session:
         return render_template("generic.html")
     else:
         return render_template("login.html",invalido = "Sessão Expirada, favor logar novamente*" )
        
@app.route("/elements")
def elements():
     if 'username' in session:
         return render_template("elements.html")
     else:
         return render_template("login.html",invalido = "Sessão Expirada, favor logar novamente*" )

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("home"))

@app.route("/register", methods=["POST", "GET"])
def register():

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #if(re.search(regex,email)):  validação, se True, email OK
         
    if request.method == "POST":
            # Get the username and password from the form
            username = request.form["username"]
            password = request.form["password"]
            passwordconfirm = request.form["passwordconfirm"]
            email = request.form["email"]

     #adicionar regras#

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)



