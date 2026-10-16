from flask import Flask
import uuid
app=Flask(__name__)
#we are generating student routing app
@app.route("/")
def student_app():
    return "welcome to student routing app"
@app.route("/student_page")
def student_page():
    return "student details are represented in this page"
@app.route("/student/<int:id>")
def student_id(id):
    return f"the id of the student was:{id}"
#Att,filepath,uuid,course
@app.route("/attedence/<float:attedence>")
def student_attedence(attedence):
    return f"the attedence of the studence was {attedence}"
@app.route("/skills/<s1>/<s2>/")
def skills(s1,s2):
    return f"student has the skills of {s1} and {s2}|"
@app.route("/path/path:<file_path>")
def path(file_path):
    return f"the file path was {file_path}"
@app.route("/search_student/")
def generate():
    id=uuid.uuid4()
    return f"the uuid of the student was {id}"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)