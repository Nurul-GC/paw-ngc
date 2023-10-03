import pprint

import requests

with open("questions&answers.txt", "w+") as qa:
    response = requests.get('https://opentdb.com/api.php?amount=50')
    qa.write(f"{pprint.pformat(response.json())}")
print("done succesfully..")
