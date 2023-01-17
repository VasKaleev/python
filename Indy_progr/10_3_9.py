persons = [
    {
        'birthday': '1983-10-25',
        'job': 'Field seismologist',
        'name': 'Andrew Hernandez',
        'phone': '680-436-8521x3468'
    },
    {
        'birthday': '1993-10-03',
        'job': 'Pathologist',
        'name': 'Paul Harmon',
        'phone': '602.518.4130'
    },
    {
        'birthday': '2002-06-11',
        'job': 'Designer, multimedia',
        'name': 'Gregory Flores',
        'phone': '691-498-5303x079'
    },
    {
        'birthday': '2006-11-28',
        'job': 'Print production planner',
        'name': 'Jodi Garcia',
        'phone': '(471)195-7189'},
    {
        'birthday': '2019-12-05',
        'job': 'Warehouse manager',
        'name': 'Elizabeth Cannon',
        'phone': '001-098-434-5950x276'
    },
    {
        'birthday': '1984-06-12',
        'job': 'Visual merchandiser',
        'name': 'Troy Lucas',
        'phone': '+1-018-070-2288x18433'
    },
    {
        'birthday': '1993-09-14',
        'job': 'International aid/development worker',
        'name': 'Laurie Sandoval',
        'phone': '2930693269'
    },
    {
        'birthday': '1999-05-25',
        'job': 'Editor, film/video',
        'name': 'Jack Clark',
        'phone': '8643048473'
    },
    {
        'birthday': '1985-09-11',
        'job': 'Magazine journalist',
        'name': 'Kimberly Johnson',
        'phone': '+1-583-428-7663'
    },
    {
        'birthday': '1990-10-07',
        'job': 'Museum/gallery curator',
        'name': 'Austin Liu PhD',
        'phone': '714-879-5250'
    }
]
phones = list(map(lambda x: x['phone'], persons))
print(phones)
