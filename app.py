#Importem la classe Flask dins de la llibreria flask
from flask import Flask, render_template, send_from_directory, jsonify
from database import load_jobs_from_db, load_job_from_db
app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Definem la pagina d'inici (sense ruta extra) 
@app.route("/")
def hellow_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name="holaquetal")

#Intentem afegir icona favicon.ico pero no va
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path,'static'), 'image/pepsi.ico', mimetype = 'image/vnd.microsoft.icon')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)