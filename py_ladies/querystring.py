# Query string zabawa:
#
# /query_string
# GET
# proper response:
#     200: {
#     "parsed": bool,
#     "args": dict,
#     "url": dict,
#     "query_string": dict
# }

import requests
zad = requests.get("http://py.net/query_string")
print(zad.json())