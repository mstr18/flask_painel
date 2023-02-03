import pyodbc
import bcrypt
import re

class Conexoes:
    
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=Abc,1234")
    def __init__(self):
        try:
            self.conn = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=Abc,1234")
        except pyodbc.Error as err:
            return print(f"Erro na conexao com o banco de dados: {err}")
        
    def getConn(self):

        return self.conn
    
    def insertUser(u,p,e, self)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if(re.search(regex,e)):  
                    
                    password = p.encode() 
                    salt = bcrypt.gensalt()
                    password_hash = bcrypt.hashpw(password, salt)
                    #Validar senha!!!! terminar código
                    self.conn.cursor().execute(f"insert into dbo.users values ('{u}', '{password_hash}', '{e}');")
                    self.conn.commit() 
                    return True
        else:  
                    print("Invalid Email")  
                    return False
    
    def validUser(self, u, p):
        cursor = self.conn.cursor().execute(f"select usuario, senha from dbo.users where usuario like '{u}' and senha like '{p}'")
        if cursor.rowcount == 0: 
            return False
        else: 
            cursor.close()
            return True
        
    

   