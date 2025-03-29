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

@app.route('/userhome')
def userhome():
  return render_template("user-home.html")

@app.route('/myaccounts')
def myaccounts():
  return render_template("myAccounts.html")

@app.route('/mytransaction')
def mytransaction():
  return render_template("myTrasaction.html")

@app.route('/mobile')
def mobile():
  return render_template("mobileRecharge.html")

@app.route('/mysetting')
def mysetting():
  return render_template("mySetting.html")

@app.route('/mypayments')
def mypayments():
  return render_template("myPayments.html")

@app.route('/transfermoney')
def transfermoney():
  return render_template("transferMoney.html")

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
        return render_template("index.html")
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
        return render_template("user-home.html")
    else:
        msg = "plese signUp first"  
    return render_template("message.html",msg=msg)



if __name__ == '__main__':
  app.run(debug=True)