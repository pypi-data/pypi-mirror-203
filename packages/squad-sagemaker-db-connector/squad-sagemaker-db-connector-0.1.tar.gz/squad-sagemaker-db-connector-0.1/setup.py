import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

install_requires = [
    'boto3==1.14.60', 'psycopg2-binary==2.8.6', 'SQLAlchemy==1.3.19'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="squad-sagemaker-db-connector",
    author="Ujjwal Gupta",
    author_email="ujjwal.gupta@squadstack.com",
    description=("A pluggable connector that allows users (admins) to execute SQL,"
                 " view, and export the results."),
    license="MIT",
    keywords="Db connector",
    url="https://github.com/squadrun/auctm-database-connector",
    packages=['auctm_database_connector'],
    long_description=read('README.rst'),
    long_description_content_type='text/plain',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)
