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
        
    def __getConn(self):

        return self.conn
    
    def verificaSenha(self, senha, confirmacao):
        
        if senha != confirmacao:
            return False        
        if len(senha) < 8:
            return False
        if not re.search("[a-z]", senha):
            return False
        if not re.search("[A-Z]", senha):
            return False
        if not re.search("[0-9]", senha):
            return False
        if not re.search("[!@#%&*]", senha):
            return False
        return True
    
    def verificaEmail(self, email):
         
         regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
         if re.search(regex,email):
             return True
         else: return False

    def insertUser(self,u,p,c,e):
        
        if self.verificaEmail(e):  

            if self.verificaSenha(p, c):        
                password = p.encode() 
                salt = bcrypt.gensalt()
                password_hash = bcrypt.hashpw(password, salt)
                hashed = password_hash.decode()
                sql = f"insert into dbo.users values ('{u}', '{hashed}', '{e}');"
                self.conn.cursor().execute(sql)
                self.conn.commit() 
            else:
                return False
            return True
        
        else:  
            return False
    
    def validUser(self, u, p):
        sql = f"select usuario, senha from dbo.users where usuario like '{u}'"
        cursor = self.conn.cursor().execute(sql)
        if cursor.rowcount == 0: 
            cursor.close()
            return False
        else: 
            for row in cursor:
                senha = row[1]
                if bcrypt.checkpw(p.encode('utf-8'), senha.encode('utf-8')): 
                    cursor.close()
                    return True  
            else:
                cursor.close() 
                return False  
            
        
    

   