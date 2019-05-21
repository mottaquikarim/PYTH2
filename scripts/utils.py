import json
import os

from datetime import datetime


# TODO: refactor the filename_parts bits...
def does_dir_path_exist(filename, dirname="Notes"):
    filename_parts = filename.split('/')
    newdir = "/".join(filename_parts[0:-1]+[dirname])
    filename_name = filename_parts.pop().split('.')[0]
    newfilepath = newdir + "/" + filename_name + ".ipynb"
    if os.path.isfile(newfilepath):
        return newfilepath
    else:
        return None
    

def get_ipynb_path(filename, dirname="nb"):
    filename_parts = filename.split('/')
    newdir = "/".join(filename_parts[0:-1]+[dirname])
    filename_name = filename_parts.pop().split('.')[0]
    os.makedirs(newdir, exist_ok=True)
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

def get_status_icon_by_date(data):
    str_month, str_day = data.split('/')
    month = int(str_month)
    day = int(str_day)

    today = datetime.today()
    if month == today.month and day == today.day:
        return "➡️  "
    elif month < today.month or month == today.month and day < today.day:
        return "✅  "
    else:
        return ""
