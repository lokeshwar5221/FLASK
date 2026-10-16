from flask import Flask,render_template,url_for,request,redirect
import uuid
app=Flask(__name__)
@app.route('/')
@app.route('/home/')
def resume():
    return render_template('Resume.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)