from flask import Flask,render_template,request
import  mysql.connector

app= Flask(__name__)
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense"
    )
mycursor=mydb.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Register')
def about():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/reg_validation',methods=['POST'])
def reg_validation():
    if request.method=='POST':

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("INSERT INTO users (name,email,password) VALUES(%s,%s,%s)",(name,email,password))
        mydb.commit()
        mycursor.close()
        return "sucessss!!"

@app.route('/login_validation',methods=['POST'])
def login_validation():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """
                         .format(email, password))
        users = mycursor.fetchall()
        if(len(users)>0):
            return render_template('main.html')
        else:
            return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')




@app.route('/create')
def createques():
    return render_template('Create.html')








if __name__=="__main__":
    app.run(debug=True)