from flask import Flask,render_template,url_for,request,redirect
import uuid
app=Flask(__name__)
@app.route('/')
@app.route('/home/')
def resume():
    return render_template('Resume.html')

@app.route('/subject/<subject>/<float:marks>/')
def subject(subject,marks):
    return f"subject:{subject} and marks:{marks}"

@app.route('/uuid/<subject>')
def id(subject):
    id=uuid.uuid4().hex
    return f'the unique id of the {subject} is {id}'

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)