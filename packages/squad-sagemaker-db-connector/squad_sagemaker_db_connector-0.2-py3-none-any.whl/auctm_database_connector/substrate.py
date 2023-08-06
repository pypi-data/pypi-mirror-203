"""
This module provides a database engine connection for the substrate database. It reads the username, password, host,
and port from AWS Parameter Store for better security.
This connection provides READ ONLY access to the Substrate database.
"""
from sqlalchemy import create_engine
from .utils import get_parameters


USER_PARAMETER = 'db-connector-substrate-username'
PASSWORD_PARAMETER = 'db-connector-substrate-password'
HOST_PARAMETER = 'db-connector-substrate-host'
PORT_PARAMETER = 'db-connector-substrate-port'

DB_NAME = 'substrate'

parameter_to_value_map = get_parameters([USER_PARAMETER, PASSWORD_PARAMETER, HOST_PARAMETER, PORT_PARAMETER])

user = parameter_to_value_map[USER_PARAMETER]
password = parameter_to_value_map[PASSWORD_PARAMETER]
host = parameter_to_value_map[HOST_PARAMETER]
port = parameter_to_value_map[PORT_PARAMETER]

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{DB_NAME}",
    connect_args={"options": "-c statement_timeout=60000"},
)
