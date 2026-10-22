from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    data=[{"id":1,"name":"loki","marks":90},
          {"id":2,"name":"sailu","marks":92},
          {"id":3,"name":"roxx","marks":100},
          {"id":4,"name":"arjun","marks":88},
          {"id":5,"name":"akhil","marks":68},
          {"id":6,"name":"deepti","marks":77},
          {"id":7,"name":"naveen","marks":65},
          {"id":8,"name":"satya","marks":70},
          {"id":9,"name":"vinay","marks":80},
          {"id":10,"name":"yamini","marks":90}]
    return render_template('index.html',d=data)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5858,debug=True)
