import json
import os


def get_ipynb_path(filename, dirname="nb"):
    filename_parts = filename.split('/')
    newdir = "/".join(filename_parts[0:-1]+[dirname])
    os.makedirs(newdir, exist_ok=True)
    filename_name = filename_parts.pop().split('.')[0]
    return f"{newdir}/{filename_name}.ipynb" 

def mrkdown_details(code, with_header_dict=False):
    lines = code.split('\n')

    header = lines[0:3]
    rest = lines[4:]

    header_dict = json.loads(header[1])
    next_file = header_dict.get("next", None)

    returnable = [next_file, rest]
    if with_header_dict:
        returnable.append(header_dict)

    return returnable

