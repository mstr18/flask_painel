import pyodbc

class Conexoes:
    
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=Abc,1234")
    def __init__(self):
        try:
            self.conn = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=master;UID=sa;PWD=Abc,1234")
        except pyodbc.Error:
            return print("Erro na conexao com o banco de dados")
        
    def getConn(self):
        return self.conn
    
    def validUser(self, u, p):
        cursor = self.conn.cursor().execute(f"select usuario, senha from dbo.users where usuario like '{u}' and senha like '{p}'")
        if cursor.rowcount == 0: return False
        else: return True
        
    

   