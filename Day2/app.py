from flask import Flask
app=Flask(__name__)
#now we will start def the routs
@app.route("/")
def home():
    """Default homre page"""
    return "welcome all this is home"
@app.route("/loki")
def details():
    """Details about loki"""
    return "loki is from visakhapatnam"
@app.route("/profile")
def profile():
    """loki profile"""
    return "loki was a python full stack trinee at codegnan"
if __name__=="__main__":
    app.run(host='0.0.0.0', 
            port=5500,debug=True)
