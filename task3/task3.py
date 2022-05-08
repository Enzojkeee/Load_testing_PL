import json


def open_json(file):
    with open(f"{file}", 'r') as f:
        result = f.read()

    return json.loads(result)


def save_json(dict):
    with open('report.json', 'w') as f:
        a = json.dumps(dict)
        return f.write(a)



def update_json(a: dict, b: dict):
    for k, v in a.items():
        if isinstance(v, list):
            for i in v:
                update_json(i, b)
        else:
            update_value(a, b)


def update_value(a, b):
    for i in b.get('values'):
        if 'id' in i and i.get('id') == a.get('id'):
            a.update({'value': i.get('value')})


if __name__ == '__main__':
    tests = open_json('tests.json')
    value = open_json('values.json')
    update_json(tests, value)
    save_json(tests)