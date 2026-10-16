from flask import Flask,render_template,url_for,request,redirect
import uuid
app=Flask(__name__)
#we will generate UUID using python module
@app.route('/')
def home():
    return redirect(url_for('indexpage'))
    #return "welcome to day 4 of flask"
@app.route('/generate/')
def generate():
    id=uuid.uuid4().hex
    print(id)
    return f"The generated id is:{id}"
@app.route("/aboutpage/")
def aboutpage():
    return render_template('about.html')
@app.route("/indexpage/")
def indexpage():
    return render_template('index.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)