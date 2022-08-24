import sys
import time
from random import random

FILE_NAME = sys.argv[1] if len(sys.argv) > 1 else "input.csv"

DATE_FORMAT = '%Y-%m-%d'
END_DATE = time.time()
LIMIT_TRANSACTION = 10000

init_date = time.mktime(time.strptime('2020-1-1',DATE_FORMAT))

with open(FILE_NAME, "w") as out:
    n = 100 if len(sys.argv) <= 2 else int(sys.argv[2])
    for i in range(n):
        randtime = init_date + random() * 2000000.0
        randtime = END_DATE if randtime > END_DATE else randtime
        randdate = time.strftime(DATE_FORMAT, time.localtime(randtime))
        
        transaction = random() * LIMIT_TRANSACTION
        transaction *= -1 if random() > 0.5 else transaction

        out.write('{},{},{:.2f}\n'.format(i + 1, randdate, transaction))

        init_date = randtime