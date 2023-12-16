import sqlalchemy;
from sqlalchemy import create_engine,text
import os
db_connection_string=os.environ['SECRET_DB_CONNECTION']
engine = create_engine(db_connection_string,connect_args={
                "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                      }
                  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  jobs=[]
  
  for row in result.all():
    result_dict=row._mapping
    jobs.append(result_dict)
  
  return jobs