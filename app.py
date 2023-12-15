from flask import Flask,render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru',
    'salary':'10000'
  },
  {
    'id':'2',
    'title':'Data engineer',
    'location':'Mumbai',
    'salary':'20000'
  },
  {
    'id':'3',
    'title':'Front engineer',
    'location':'remote',

  },
  {
    'id':'4',
    'title':'backend engineer',
    'location':'USA',
    'salary':'$130000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html" ,jobs=JOBS,company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host= '0.0.0.0', debug=True)