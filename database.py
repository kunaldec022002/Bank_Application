# database class to perform CRUD operation
import pymysql as pm

class Database:
    def __init__(self):
        # Correct the connection attribute name to self.com
        self.com = pm.connect(host='localhost', user='root', password='admin', database='mypythonbank')
        self.cursor = self.com.cursor()  # Use self.com instead of self.con

    def storeUser(self, email, pass1):
        try:
            # Using parameterized queries to avoid SQL injection
            self.cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, pass1))
            self.com.commit()  # Commit the transaction
            self.status = True
        except Exception as e:
            # Rollback in case of error
            self.com.rollback()
            self.status = False
           # print(f"Error: {e}")  # Print the error message for debugging
        return self.status
    
    def checkUser(self, email, pass1):
      
            # Using parameterized queries to avoid SQL injection
            self.cursor.execute("select * from users where email='%s' and password='%s'"%(email, pass1))
            if self.cursor.rowcount == 1:
                 self.status = True
            else:
                 self.status = False
            return self.status
