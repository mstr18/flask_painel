from flask import Flask, render_template, request, redirect, url_for, session
#import pyodbc 

app = Flask(__name__)
app.secret_key = 'secret_key'


"""conexao = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=Abc,1234")

cur = conexao.cursor().execute("select usuario, senha from users")

for row in cur.fetchall():
    print(row.usuario)
    print(row.senha)"""

# Dummy user database
users = {
    'user1': 'p1',
    'user2': 'p2',
    'user3': 'p3'
}

@app.route("/")
def home():
    if 'username' in session:
        redirect(url_for("images"))
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]

        # Check if the user exists and the password is correct
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for("images"))
        else:
            return "senha inválida <a href='/login'> Voltar </a>"
    else:
        return render_template("login.html")

@app.route("/images")
def images():
     if 'username' in session:
         return render_template("images_match.html")
     else:
         return "sesssão expirada <a href='/login'> Voltar </a>"
        
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)



