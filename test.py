import json

schema_path = '1.json'

def load_schema():
    with open(schema_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        print(type(data))
        # # for i in data:
        # #     print(i)
        # lines = f.readlines()
        # for line in lines:
        #     print(type(line))
        #     print(line)
        #     data = json.loads(line)

load_schema()