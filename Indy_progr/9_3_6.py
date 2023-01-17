import json
str_json = """
{
  "name": "Jonny",
  "surname": null
}
"""

data = json.loads(str_json)
print(data)