import nbformat

from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

from conf import DEFAULT_FIRST_FILE_NB, IPYTHON_DIRS
from utils import get_ipynb_path, mrkdown_details


def get_cell(line, block):
    if "python" in line:
        return new_markdown_cell(block)

    return new_code_cell(block)

def mrkdown_to_nb(body, filename):
    nb = new_notebook()
    current_block = []
    for line in body:
        if line.startswith('```'):
            block = "\n".join(current_block)
            nb.cells.append(get_cell(line, block))
            current_block = []
        else:
            current_block.append(line)

    nbformat.write(nb, get_ipynb_path(filename))


def convert_to_nb(dirname, filter_, first_file=DEFAULT_FIRST_FILE_NB):
    content_arr = []

    file_ = first_file
    while file_ and filter_ in file_:
        content_arr.append(f'{dirname}/{file_}')

        nb = new_notebook()
        try:
            f = open(f'{dirname}/{file_}')
        except:
            break

        nextfile_, body = mrkdown_details(f.read())
        mrkdown_to_nb(body, f'{dirname}/{file_}')
        file_ = nextfile_

    print(content_arr)
    pass


if __name__ == "__main__":
    for filter_ in IPYTHON_DIRS:
        convert_to_nb('src', filter_=filter_)
