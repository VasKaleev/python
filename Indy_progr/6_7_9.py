data = {
    "my_friends": {
        "count": 10,
        "people": [{
            "first_name": "Kurt",
            "id": 621547005,
            "last_name": "Cobain",
            "bdate": "31.8.2005"
        }, {
            "first_name": "Виолетта",
            "id": 484200150,
            "last_name": "Кастилио",
        }, {
            "first_name": "Иринка",
            "id": 21886133,
            "last_name": "Бушуева",
            "bdate": "28.8.1942"
        }, {
            "first_name": "Данил",
            "id": 282456573,
            "last_name": "Греков",
            "bdate": "4.7.2002"
        }, {
            "first_name": "Валентин",
            "id": 184902932,
            "last_name": "Долматов",
            "bdate": "25.5"
        }, {
            "first_name": "Евгений",
            "id": 620469646,
            "last_name": "Шапорин",
            "bdate": "6.12.1982"
        }, {
            "first_name": "Ангелина",
            "id": 622328862,
            "last_name": "Краснова",
            "bdate": "4.11.1995"
        }, {
            "first_name": "Иван",
            "id": 576015198,
            "last_name": "Вирин",
            "bdate": "2.2.1915"
        }, {
            "first_name": "Паша",
            "id": 386922406,
            "last_name": "Воронов",
            "bdate": "27.9"
        }, {
            "first_name": "Ольга",
            "id": 622170942,
            "last_name": "Савченкова",
            "bdate": "20.12"
        }]
    }
}
a = []
for i in data['my_friends']['people']:
    a.append(i['first_name'])
print(*sorted(a),sep='\n')