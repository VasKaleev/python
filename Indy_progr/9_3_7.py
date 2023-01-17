import json
str_json = """
{
  "name": "Jonny",
  "have_driver_license": true
}
"""

data = json.loads(str_json)
print(data)