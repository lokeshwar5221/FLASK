from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/postdata/',methods=['POST'])
def postdata():
    username=request.form['username']
    email=request.form['email']
    address=request.form['address']
    password=request.form['password']
    if username is None or len(username)<5:
        return render_template('index.html',err="Invalid name")
    if email is None:
        return render_template('index.html',err='Invalid email')
    if address is None:
        return render_template('index.html',err='enter valid address')
    if password is None or len(password)<4:
        return render_template('index.html',err='Password is wrong')
    return render_template('index.html',msg='successfull')
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port="5001",debug=True)