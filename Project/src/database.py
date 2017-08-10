# Standard library
import os
import sys

from sqlalchemy import create_engine

# Configuration
if (True):
    user = os.getenv('REDSHIFT_USER_PROD')
    password = os.getenv('REDSHIFT_PASSWORD_PROD')
    host = 'fleetremote-prd.csnqydpupptn.eu-west-1.redshift.amazonaws.com'  
    database = database = 'fleetremote_prd'
else:
    user = os.getenv('REDSHIFT_USER_DEV')
    password = os.getenv('REDSHIFT_PASSWORD_DEV')    
    host = 'fr.cjebzpwqeiev.eu-west-1.redshift.amazonaws.com'   
    database = 'events2'

port = 5439

connection = "postgresql://{user}:{password}@{host}:{port}/{database}".format(user=user, password=password, host=host, database=database, port=port)

engine = create_engine(connection)