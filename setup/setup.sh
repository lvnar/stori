#!/bin/bash

# Create a new user on DB
# 'email' and 'name' fields may be set as prefered. You can
# use yours to get the email on your own inbox
curl --location --request POST 'localhost:8000/api/user' \
    --header 'Content-Type: application/json' \
    --form 'email="lvnar.dev@gmail.com"' \
    --form 'name="César Pérez Canseco"'

# Create a new acccount on DB
# 'number' field may be changed but should match with the number
# used in the next commands. 'userId' should be the same as given
# in the previous answer.
curl --location --request POST 'localhost:8000/api/account' \
    --header 'Content-Type: application/json' \
    --form 'userId="1"' \
    --form 'number="A123456780"'

# Create a new random input file with script
# Two params 'accountNumber'.csv and 'nTransactions'
python setup/csvGenerator.py A123456780.csv 5

# Send file to /input endpoint and wait for the email 
# in your inbox.
curl --location --request POST 'localhost:8000/input' \
    --form 'file=@"./A123456780.csv"'

