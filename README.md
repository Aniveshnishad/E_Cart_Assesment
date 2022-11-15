# E-commerce analytics module
This is e-commerce website its stor multiple products and manage by vendors. 


## Pre-requisites
1. Python 3.10.0
2. postgres


## Project Setup Environment

1. First Set virtual environment.  

``` shell
pip install -r requirenment.txt
```

## Setup Database  ( Required )
* Create a new database -> e-cart-module or any 
* After creating database change the .env file with you configuration like database username , password , host etc
* After this you need to run this command to properly create tables in your database 
```shell
python3 manage.py makemigrations
```

```shell
python3 manage.py migrate
```


## Creating a superuser 
```shell
python3 manage.py createsuperuser
```

Enter Few details and super admin will get created 


## Postmen Collection :

1. There is postmen collection provided in the project you can directly import it.
2. If you face any issue in postmen collection with env variable please add this variable 
3. server-url = 
4. token can be dynamically set after get token api 

## Api Document 
Api Document is provided in the docs formate in the project directory.