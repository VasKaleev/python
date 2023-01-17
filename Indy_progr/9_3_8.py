import json
str_json = """
{
  "name": "Jonny",
  "have_driver_license": false
}
"""

data = json.loads(str_json)
print(data)