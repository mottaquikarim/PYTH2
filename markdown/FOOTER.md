## Practice Problems

The PSETS associated with this course exist on a separate github repo. Please find **[PYTH2 PSETS here](https://github.com/mottaquikarim/pydev-psets)**

## Building and Deploying

The `scripts` folder contains a few py scripts that help transform the content from markdown to jupyter notebooks and regenerate the README. On deploy, travis CI runs these tasks and generates output content.

### Build Env and Install Reqs 

Create a virtual env:

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Converting Markdown to Jupyter Notebooks

In `scripts/conf.py`, set the `IPYTHON_DIRS` to include whichever directories that must be converted. Then:

```python
python scripts/convert_to_nb.py
```

The dirs in `IPYTHON_DIRS` will now have a `nb` folder with jupyter notebooks.

### Regenerating README

Each `.md` file has something like:

```
<!---
{"next":"Lectures_class2/Lecture2.md","title":"Intro to GA & Python - 5/21"}
-->
```

This is parsed by the `scripts/build_summary.py` script and a list is created where each subsequent file is denoted in `next`. Files that are part of `IPYTHON_DIRS` automatically link to the jupyter notebook vs the markdown. To run:

```python
python scripts/build_summary.py
```

## Instructional Team

Some info about your instructors.

### Taq Karim

<img src="https://github.com/mottaquikarim/JavascriptBootcamp/blob/master/assets/taq.jpg?raw=true" style="width: 100px; height: auto;" width="100" align="left"> 

[Hello, Wrold!](https://medium.com/@the_taqquikarim/console-log-hello-wrold-3e3abeb44396) I'm Taq, Tech Lead of the Demand Side (DSP) team at Place Exchange, a programmatic advertising exchange platform for Out of Home media. I'm also a lecturer, leading workshops and courses on a wide variety of topics (frontend / backend) in institutions such as Coalition 4 Queens (now Pursuit), The Startup Institute, NYCDA, OneMonth, The King's College and Columbia Splash. [I've taught Front-end Web Development at GA 14x](https://medium.com/@the_taqquikarim/10-lessons-learned-from-100-weeks-of-teaching-fewd-12c43db14f6b) (so far). When I'm not working I am usually [thinking about math](https://medium.com/math-musings/why-does-25-25-2-2-1-100-25-an-explanation-6c7e7b283d41), [building](https://medium.com/@the_taqquikarim/a-technique-for-saving-content-from-a-data-text-html-uri-10f045a8876d) [software](https://medium.com/@the_taqquikarim/introducing-bonfire-2c0e437895e2), [working](https://photos.app.goo.gl/w1crzgI7DqCgGR373) [on](https://photos.app.goo.gl/EaFkp5SmyO0opkg32) [hardware](https://photos.app.goo.gl/tvxPl2zbIMl7FEnK2) [hacks](https://www.instagram.com/p/8rARZNND_t/?taken-by=taqqui.karim) or hanging out with my cat, Layla Karim.

### Julianna Garreffa

*bio here*
