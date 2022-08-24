# Stori Challenge
##### By César Pérez Canseco [perez.canseco@gmail.com]
___
Django project design to complish with the Stori Card challenge to:
- Get a CVS file
- Process bank transactions
- Email summary info

___
## Configuration
There are some fields that can be set in ./stori/settings.py
according to environment:
- DEBUG - False on Production environment
- API_URL - 'localhost' by default but configurable
- SMTP_URL - SMTP relay address
- SMTP_API_KEY - SMTP security access key

___
## Deployment
Project requires Python3 installed. Run the net commands:

1. Install pipenv
    ```
    pip3 install pipenv --upgrade
    ```
2. Set virtual environment up 
    ```
    pipenv shell
    pipenv install
    python manage.py migrate
    ```
3. Run server
    ```
    python manage.py runserver
    ```

___
## Run a test
Running this script you create the minimal requirements in DB to run
a successful test and get a summary of loaded info in the inbox. There
are a few fields which can be set to get email in personal inbox.
```
bash setup/setup.sh
````
