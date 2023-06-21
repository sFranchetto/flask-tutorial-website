from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :val").params(val=id))
    job = []
    for row in result.all():
      job.append(row._asdict())
    if len(job) == 0:
      return None
    else:
      return job


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    conn.execute(
      text(
        "INSERT INTO application (job_id, full_name, email, linkedin_url) VALUES (:job_id, :full_name, :email, :linkedin_url)"
      ).params(job_id=job_id,
               full_name=data['full_name'],
               email=data['email'],
               linkedin_url=data['linkedin_url']))
