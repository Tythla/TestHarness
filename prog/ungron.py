import json
import argparse


def set_value(dct, keys, value):
    """Set a value in a nested dictionary based on a list of keys."""
    for key in keys[:-1]:
        if key.isdigit(): 
            key = int(key)
            if not isinstance(dct, list):
                dct = [dct]
            while len(dct) <= key:
                dct.append({})
            dct = dct[key]
        else:
            dct = dct.setdefault(key, {})
    last_key = keys[-1]
    if last_key.isdigit():
        last_key = int(last_key)
        if not isinstance(dct, list):
            dct[last_key] = value
        else:
            while len(dct) <= last_key:
                dct.append(None)
            dct[last_key] = value
    else:
        dct[last_key] = value


def ungron(lines):
    result = {}
    for line in lines:
        path, value = line.split(' = ')
        keys = path.split('.')
        value = json.loads(value)
        set_value(result, keys, value)
    return result


parser = argparse.ArgumentParser(
    description="Ungron: Convert flattened JSON back to structured JSON")
parser.add_argument('filename', help="File containing flattened JSON")

args = parser.parse_args()

with open(args.filename, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

ungroned_data = ungron(lines)
print(json.dumps(ungroned_data, indent=4))
