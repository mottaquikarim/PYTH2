from conf import DEFAULT_FIRST_FILE, IPYTHON_DIRS
from utils import does_dir_path_exist, get_ipynb_path, get_status_icon_by_date, mrkdown_details

def scan_for_nb(filename):
    if "Lectures_" not in filename:
        return

    f = open(filename, 'r')
    content = f.read()
    body = content.split('\n')[4:]

    for ipyth in IPYTHON_DIRS:
        for idx, line in enumerate(body):
            if ipyth in line:
                body[idx] = line.replace(f'{ipyth}/(?!nb)', f'{ipyth}/nb/')
                body[idx] = line.replace('.md', '.ipynb')
        
    f.close()
    f = open(filename, 'w')
    f.write('\n'.join(content.split('\n')[0:3]) + '\n\n' + '\n'.join(body))
    f.close()


def build_summary(dirname, first_file=DEFAULT_FIRST_FILE):
    content_arr = []
    summary_md = []

    file_ = first_file
    i = 0
    while file_:
        content_arr.append(file_)

        try:
            f = open(f'{dirname}/{file_}')
        except Exception as e:
            pass

        nextfile_, body, header = mrkdown_details(f.read(), with_header_dict=True)
        scan_for_nb(f'{dirname}/{file_}')
        title = header.get('title', file_)
        if "README" in file_:
            summary_md.append(f"### [{title.upper()}]({dirname}/{file_})")
            i = 0
        else:
            ipyth_link = False
            for ipyth in IPYTHON_DIRS:
                if ipyth in file_:
                    ipyth_link = True
                    break

            if not ipyth_link:
                if " - " in title:
                    data = title.split(' - ').pop()
                    status = get_status_icon_by_date(data)
                    summary_md.append(f"{i}. {status}**[{title}]({dirname}/{file_})**")
                else:
                    summary_md.append(f"{i}. **[{title}]({dirname}/{file_})**")
            else:
                str_ = f"{i}. **[{title}]({get_ipynb_path(dirname + '/' + file_)})**"
                print("FILE: ", file_)
                path = does_dir_path_exist(dirname + "/" + file_)
                if path:
                    str_ += f" | **[Notes]({path})**"

                summary_md.append(str_)

        file_ = nextfile_
        i += 1


    return "\n".join(summary_md)

if __name__ == "__main__":
    content = build_summary('src')
    with open('markdown/HEADER.md', 'r') as f:
        header = f.read()

    with open('markdown/FOOTER.md', 'r') as f:
        footer = f.read()

    with open('README.md', 'w') as f:
        f.write(header + '\n' + content + '\n' + footer)

