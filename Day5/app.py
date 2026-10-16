from flask import Flask,render_template,url_for,request,redirect
import uuid
app=Flask(__name__)
#we will generate UUID using python module
@app.route('/')
def home():
    return render_template('index.html')
#name=loki,email=loki@gmail.com
@app.route('/getData',methods=['GET'])
def getData():
    name=request.args.get('name')
    email=request.args.get('email')
    return f'the name is {name} and email is {email}'

@app.route('/getDatafromPost',methods=['POST'])
def getDatafromPost():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'the name was {name}, email is {email}'
    
@app.route('/postData/',methods=['POST'])
def postData():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    if name is None or len(name)<5:
        return render_template('index.html',err="Invalid name")
    if email is None:
        return render_template('index.html',err='Invalid email')
    if password is None or len(password)<4:
        return render_template('index.html',err='Password is wrong')
    return render_template('index.html',msg='Successfull')
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)