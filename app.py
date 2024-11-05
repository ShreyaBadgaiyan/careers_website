# print("Hello World")

from flask import Flask, render_template,jsonify

app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,India',
        'salary':'Rs. 1000000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi,India',
        'salary':'Rs. 1500000'

    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'Rs. 1200000'
    },

    {
        'id':4,
        'title':'Backend Engineer',
        'location':'Remote',
        'salary':'$120,000'
    }

]

@app.route("/")
def home_page():
     return render_template('index.html',jobs=JOBS,company_name='Jovian')

@app.route("/profile")
def hello_world():
    return "Hello Shreya Badgaiyan!"



@app.route("/api/jobs")
def list_jobs():
     return jsonify(JOBS)
     



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)