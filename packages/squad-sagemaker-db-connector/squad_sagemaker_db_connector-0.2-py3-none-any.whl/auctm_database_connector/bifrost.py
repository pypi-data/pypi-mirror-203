"""
This module provides a database engine connection for the bifrost database. It reads the username, password, and host
from AWS Parameter Store for better security.
This connection provides READ ONLY access to the Bifrost database.
"""
from sqlalchemy import create_engine
from .utils import get_parameters


USER_PARAMETER = 'db-connector-bifrost-username'
PASSWORD_PARAMETER = 'db-connector-bifrost-password'
HOST_PARAMETER = 'db-connector-bifrost-host'

parameter_to_value_map = get_parameters([USER_PARAMETER, PASSWORD_PARAMETER, HOST_PARAMETER])

user = parameter_to_value_map[USER_PARAMETER]
password = parameter_to_value_map[PASSWORD_PARAMETER]
host = parameter_to_value_map[HOST_PARAMETER]

engine = create_engine(
    f"postgresql://{user}:{password}@{host}/bifrost",
    connect_args={"options": "-c statement_timeout=60000"},
)
