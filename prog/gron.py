import json
import argparse


def flatten_json(obj, base, current_path=''):
    flattened = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            path = f"{current_path}.{k}" if current_path else f"{base}.{k}"
            flattened.extend(flatten_json(v, base, path))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            path = f"{current_path}[{i}]"
            flattened.extend(flatten_json(v, base, path))
    else:
        flattened.append(f"{current_path} = {json.dumps(obj)}")

    return flattened


def gron(file_name, base_object='json'):
    with open(file_name, 'r') as file:
        data = json.load(file)

    flattened_data = flatten_json(data, base_object)
    return '\n'.join(flattened_data)


parser = argparse.ArgumentParser(description="Gron JSON Tool")
parser.add_argument('filename', help="JSON file to process")
parser.add_argument('--obj', default='json', help="Base object name")

args = parser.parse_args()

result = gron(args.filename, args.obj)
print(result)