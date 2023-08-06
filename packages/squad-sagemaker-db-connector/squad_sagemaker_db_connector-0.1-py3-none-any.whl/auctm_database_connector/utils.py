import boto3

from collections import namedtuple


ssm_client = boto3.client('ssm', region_name='us-east-1')


def get_parameter(parameter_name: str) -> str:
    """
    Fetches the value of the given parameter from AWS SSM Parameter Store.
    :param parameter_name: String
    :return: String
    """
    return ssm_client.get_parameter(
        Name=parameter_name, WithDecryption=True
    )['Parameter']['Value']


def get_parameters(parameter_names: [str], region='us-east-1') -> {str: str}:
    """
    Fetches the given parameters from SSM Parameter store.
    :param parameter_names: List of strings
    :param region: String
    :return: dictionary containing key-value pairs
    """
    ssm_client = boto3.client('ssm', region_name=region)

    parameters = ssm_client.get_parameters(
        Names=parameter_names, WithDecryption=True
    )['Parameters']

    parameter_to_value_map = {
        parameter['Name']: parameter['Value']
        for parameter in parameters
    }

    return parameter_to_value_map


def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a dict.
    By default, the Python DB API will return results without their field names, which means you end up with a
    list of values, rather than a dict. At a small performance and memory cost, we can return results as a
    dict.

    Using Normal Cursor -
    >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
    >>> cursor.fetchall()
    ((54360982, None), (54360880, None))

    Using dict_fetch_all method -
    >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
    >>> dictfetchall(cursor)
    [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def namedtuple_fetch_all(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    A namedtuple is a tuple-like object that has fields accessible by attribute lookup;
    it’s also indexable and iterable. Results are immutable and accessible by field names or indices,
    which might be useful.

    Using Normal Cursor -
    >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
    >>> cursor.fetchall()
    ((54360982, None), (54360880, None))

    Using namedtuple_fetch_all method -
    >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
    >>> results = namedtuplefetchall(cursor)
    >>> results
    [Result(id=54360982, parent_id=None), Result(id=54360880, parent_id=None)]
    >>> results[0].id
    54360982
    >>> results[0][0]
    54360982
    """

    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
