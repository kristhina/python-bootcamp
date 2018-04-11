# Napisz program, który załaduje ten plik i skonwertuje każdą linię na obiekt JSON
#  w formacie {"date": string, "method": string, "uri": string, "status_code": int,
# "user_agent": string} jeśli zastosowana została metoda PUT, POST lub DELETE.

# metoda: group dict
# user agent to przeglądarka - do wrzucenia od Mozilla do końca ???

import re
import json

with open('access_log.txt', 'r', encoding="utf8") as file:
    logs = file.readlines()

for log in logs:
    try:
        m = re.match(r'.+\[(?P<date>.+)\].+(?P<method>POST|PUT|DELETE) (?P<uri>\S+) \S+ (?P<status_code>\d{3}).+\"-\" \"(?P<user_agent>.+)\"', log)
        result = m.groupdict()
        json_result = json.dumps(result)
        print(json_result)
    except AttributeError:
        pass





