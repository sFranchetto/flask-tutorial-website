from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Vancouver, Canada',
  'salary': '$50,000'
}, {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Remote',
  'salary': '$100,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Montreal, Canada'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Toronto, Canada',
  'salary': '$150,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
