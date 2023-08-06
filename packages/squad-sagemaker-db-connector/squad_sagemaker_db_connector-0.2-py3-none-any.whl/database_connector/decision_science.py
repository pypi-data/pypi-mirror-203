"""
This module provides a database engine connection for the decision_science database. It reads the from host
from AWS Parameter Store for better security. And reads username and password for a user from their home
directory in the JupyterHub server.
This connection provides WRITE access to resources inside a user's own schema in the decision_science database.
And provides READ access to the whole database.
"""
import csv
import getpass

from sqlalchemy import create_engine
from .utils import get_parameter


HOST_PARAMETER = 'db-connector-decision-science-host'

host = get_parameter(HOST_PARAMETER)

# read username and password from the credentials file from user's directory
ubuntu_user = getpass.getuser()

with open(f'/home/{ubuntu_user}/decision_science_creds.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        username = row['username']
        password = row['password']

engine = create_engine(
    f"postgresql://{username}:{password}@{host}/decision_science",
    connect_args={"options": "-c statement_timeout=60000"},
)
