"""
This module provides a database engine connection for the SquadIQ database. It reads the username, password, and host
from AWS Parameter Store for better security.
This connection provides READ ONLY access to the SquadIQ database.
"""
from sqlalchemy import create_engine
from .utils import get_parameters

AWS_REGION = "ap-south-1"

JUPYTERHUB_PG_DB_NAME_PARAMETER = "squadiq-jupyterhub-pg-db-name"
JUPYTERHUB_PG_USERNAME_PARAMETER = "squadiq-jupyterhub-pg-username"
JUPYTERHUB_PG_PASSWORD_PARAMETER = "squadiq-jupyterhub-pg-password"
JUPYTERHUB_PG_HOST_PARAMETER = "squadiq-replica-pg-host"

parameter_to_value_map = get_parameters([
    JUPYTERHUB_PG_USERNAME_PARAMETER,
    JUPYTERHUB_PG_PASSWORD_PARAMETER,
    JUPYTERHUB_PG_HOST_PARAMETER,
    JUPYTERHUB_PG_DB_NAME_PARAMETER,
], AWS_REGION)

user = parameter_to_value_map[JUPYTERHUB_PG_USERNAME_PARAMETER]
password = parameter_to_value_map[JUPYTERHUB_PG_PASSWORD_PARAMETER]
host = parameter_to_value_map[JUPYTERHUB_PG_HOST_PARAMETER]
db_name = parameter_to_value_map[JUPYTERHUB_PG_DB_NAME_PARAMETER]

engine = create_engine(
    "postgresql://{user}:{password}@{host}/{db_name}".format(user=user, password=password, host=host, db_name=db_name),
    connect_args={"options": "-c statement_timeout=60000"},
)
