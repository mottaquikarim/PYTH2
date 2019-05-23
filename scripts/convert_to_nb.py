import nbformat

from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from os import listdir
from os.path import isfile, join

from conf import DEFAULT_FIRST_FILE_NB, IPYTHON_DIRS
from utils import get_ipynb_path, mrkdown_details


def get_cell(line, block):
    if "python" in line:
        return new_markdown_cell(block)

    return new_code_cell(block)

def mrkdown_to_nb(body, filename):
    nb = new_notebook()
    nb.cells.append(new_markdown_cell(f"""<a href="https://colab.research.google.com/github/mottaquikarim/PYTH2/blob/master/{get_ipynb_path(filename)}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>"""))
    current_block = []
    for line in body:
        if line.startswith('```'):
            block = "\n".join(current_block)
            nb.cells.append(get_cell(line, block))
            current_block = []
        else:
            current_block.append(line)

    if len(current_block):
        nb.cells.append(new_markdown_cell("\n".join(current_block)))

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


def convert_psets(dirname):
    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    for f in onlyfiles:
        fh = open(f'{dirname}/{f}')
        mrkdown_to_nb(fh.read().split('\n'), f'{dirname}/{f}')

    print(onlyfiles)

if __name__ == "__main__":
    for filter_ in IPYTHON_DIRS:
        convert_to_nb('src', filter_=filter_)

    convert_psets('src/PSETS')
