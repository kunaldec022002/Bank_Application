# main file of the preject

from flask import Flask, render_template,request
from database import Database

app = Flask(__name__)
db = Database()

# routing html pages

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/signup')
def signup():
  return render_template("signup.html")

# action routes pages (storeUser)
@app.route('/storeUser',methods=['POST','GET'])
def storeUser():
  if request.method == 'POST':
    email1 = request.form['email1']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']

    if pass1 != pass2:
      msg="password not matched, please try again !!"
    else:
      if db.storeUser(email1,pass1) == True:
        msg= "signup successful"
      else:
        msg = "Signup Failed"   
    return render_template("message.html",msg=msg)

# action routes pages (checkUser)
@app.route('/checkUser',methods=['POST','GET'])
def checkUser():
  if request.method == 'POST':
    email1 = request.form['email1']
    pass1 = request.form['pass1']
  
    if db.checkUser(email1,pass1) == True:
        msg= "Login successful"
    else:
        msg = "Login Failed"   
    return render_template("message.html",msg=msg)



if __name__ == '__main__':
  app.run(debug=True)