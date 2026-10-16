from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return "welcome to day3 learning about static vs dynamic"
@app.route("/profile/")
def profile():
    return "i am loki from vizag"
#static route -->/name/loki/
#dynamic route -->/name/<name>
@app.route("/name/loki/")
def name():
    return f"i am loki"

@app.route("/name/<name>/")
def data(name):
    return f"hello {name}"

@app.route("/course/<course_name>/")
def course(course_name):
    return f"<b>you selected {course_name}</b>"

@app.route("/student/<int:student_id>/")
def student_id(student_id):
    return f"the id of the student is{student_id}"

@app.route("/percentage/<float:percentage>")
def percentage(percentage):
    return f"the percentage of student is {percentage}"

@app.route("/path/<path:file_name>/")
def filepath(file_name):
    return f"the path of the file is {file_name}"

@app.route("/student_id/<uuid:stu_id>")
def studentid(stu_id):
    return f"the uuid of the student was {stu_id}"
 
if __name__=="__main__":
    app.run(host='0.0.0.0',
            port=5006,debug=True)
           