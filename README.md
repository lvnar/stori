# Stori Challenge
##### By César Pérez Canseco [perez.canseco@gmail.com]
___
Django project design to complish with the Stori Card challenge to:
- Get a CVS file
- Process bank transactions
- Email summary info

___
## Configuration
There are some fields that can be set in .env file
according to environment:
- ENV - False on Production environment
- API_URL - 'localhost' by default. Escalability oriented.
- SMTP_URL - SMTP relay address.
- SMTP_API_KEY - SMTP security access key
- DJANGO_SECRET_KEY - Project secret key

- T_EMAIL,T_NAME,T_ACCOUNT - Testing driven values

___
## Deployment
Project requires Python3 installed. Run the net commands:

1. Install pipenv
    ```
    pip3 install pipenv --upgrade
    ```
2. Set virtual environment up 
    ```
    pipenv --python 3.10
    pipenv install -r requirements.txt
    pipenv run python manage.py migrate
    ```
3. Run server
    ```
    pipenv run python manage.py runserver
    ```

___
## Run a test
Running this script you create the minimal requirements in DB to run
a successful test and get a summary of loaded info in the inbox. There
are a few fields which can be set to get email in personal inbox.
```
bash setup/test.py
````
