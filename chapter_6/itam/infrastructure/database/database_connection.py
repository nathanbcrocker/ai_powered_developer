# Create a Python class called DatabaseConnection that uses the Singleton pattern to manage a single database connection to a PostgreSQL database using SQLAlchemy. 
# The class should read the database username, password, and connection string from environment variables
# The environment variables should be named: DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, and DB_NAME

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DatabaseConnection:
    __instance = None
    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance == None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self):
        if DatabaseConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseConnection.__instance = self
            self.engine = create_engine(f"postgresql://itam_user:itam_user@localhost:5432/postgres", connect_args={'options': '-csearch_path=itam'})
            #self.engine = create_engine(f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}", connect_args={'options': '-csearch_path={}'.format(os.environ['DB_SCHEMA'])})
            self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()