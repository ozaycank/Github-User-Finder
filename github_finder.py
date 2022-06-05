from flask import Flask,render_template,request
import requests

app = Flask(__name__)
base_url = "https://api.github.com/users/"


@app.route("/",methods = ["POST","GET"])
def index():
    if request.method == "POST":
        githubName  = request.form.get("githubname")
        responseUser = requests.get(base_url+githubName)
        responseRepository = requests.get(base_url + githubName + "/repos")

        userInfo = responseUser.json()
        repositories = responseRepository.json()

        if "message" in userInfo:
            return render_template("index.html",error = "User Not Found !!")
        else:    
            return render_template("index.html", profile = userInfo, repositories = repositories)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 