from conf import DEFAULT_FIRST_FILE, IPYTHON_DIRS
from utils import get_ipynb_path, mrkdown_details


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
                summary_md.append(f"{i}. **[{title}]({dirname}/{file_})**")
            else:
                summary_md.append(f"{i}. **[{title}]({get_ipynb_path(dirname + '/' + file_)})**")

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

