from flask import Flask,url_for,request

app=Flask(__name__)
@app.route('/')
@app.route('/home/')
def home():
    #about_url=url_for('about')
    return f"""<h1>welcome to home page</h1>
                <a href="{url_for('about')}">About</a>"""

@app.route('/about/')
def about():
    return f"<h1>Welcome to about page</h1>"

@app.route('/getdata/',methods=['GET'])
def getdata():
    name=request.args.get('name')
    batchno=request.args.get('batchno')
    return f"name was {name} and batchno was{batchno}"
    
@app.route("/getdatafrompost/",methods=['POST'])
def getdatafrompost():
    data=request.get_json()
    name=data['name']
    skills=data['skills']
    return f"i am {name} and my skills are {skills}"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)