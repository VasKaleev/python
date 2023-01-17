countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
city = input()
flag = False
for key, value in countries.items():
    if city in value:
        print(f'INFO: {city} is a city in {key}')
        flag = True
if flag == False:
    print(f'ERROR: Country for {city} not found')

