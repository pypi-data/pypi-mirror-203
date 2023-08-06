# dbm-database-service
Package can be used by in early stages of development to manage MySQL Database by adding and modifying tables and columns.
The idea is that once we have .env file created, we can use it's mysqlpool credentials to connect into database.
We are able to do it in automatic mode where .env file has to be store in same location where connector will be called,
or we can use absolute path to a file.

## Installation
[PyPI](https://pypi.org/project/dbm-database-service/)

Using pip:
```bash
  pip install dbm-database-service
```
Using poetry:
```bash
  poetry add dbm-database-service
```
Using pipenv:
```bash
  pipenv install dbm-database-service
```

## TESTS
Tests are automated, that means that you don't need to prepare .env files in desired places. They will be downloaded from
Google Drive - [feel free to inspect them](https://drive.google.com/drive/folders/1Ed1gQlnVKnk7hLUMWTGJ0W4l5b-yZPjs?usp=sharing).
MySQL container also will be created, so no further set up is needed.

### 1. Make sure your docker is running and port 3306 is empty
### 2. Clone repository and enter main directory:
```angular2html
    git clone https://github.com/DSmolke/DBM_DataBase_Service.git
    cd DBM_DataBase_Service
```
### 3. Run tests using:
####Poetry:
```angular2html
    poetry update
    poetry shell    
    cd tests
    poetry run pytest -vv
```
* update protects from decoding errors
* tests take around 15s because of database and .env files

####Pipenv:
```angular2html
    pipenv shell 
    cd tests
    pipenv run pytest -vv
```

####Pip:
```angular2html
    pip install mysql-connector-python
    pip install python-dotenv
    pip install easyvalid-data-validator
    pip install gdown
    pip install pytest
    cd tests
    pytest -vv
```

## Basic usage
Having existing database server, or mysql container, we want to create new table, add columns to existing table or
do any operation on database.

###1. Step - prepare .env file
Please download .env file template - > [link](https://drive.google.com/drive/folders/1Ed1gQlnVKnk7hLUMWTGJ0W4l5b-yZPjs?usp=sharing)

Edit file according to your needs.
```angular2html
POOL_NAME=TEST
POOL_SIZE=5
POOL_RESET_SESSION=True
HOST=localhost
DATABASE=test_db
USER=user
PASSWORD=user
PORT=3306
```

Copy its absolute path and keep it for later use.

###2. Step - Import all necessary objects
```angular2html
from dbm_database_service.models.column import Column
from dbm_database_service.models.table import Table
from dbm_database_service.models.datatype import DataType
from dbm_database_service.connectors import MySQLConnectionPoolBuilder
from dbm_database_service.managers import MySQLDatabaseManager
```

###3. Step - Create new MySQLConnectionPoolBuilder with prepared .env path
```angular2html
dbm1 = MySQLConnectionPoolBuilder(r'C:\Users\Omen i5\Desktop\PROJEKTY\dbm_database_service\tests\.env')
```

###4. Step - Create new MySQLDatabaseManager using object prepared in previous step
```angular2html
database_manager = MySQLDatabaseManager(dbm1.build())
```

5. Step - Add new table into database:
```angular2html
database_manager.create_table(
    Table('jeans', if_not_exists=True, columns=[
        Column(name='id', datatype=DataType('int'), primary_key=True, autoincrement=True),
        Column(name='brand', datatype=DataType('varchar', 255), unique=True),
        Column(name='price', datatype=DataType('decimal', (6, 2)), unique=True),
])
```