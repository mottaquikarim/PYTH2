[![Build Status](https://travis-ci.org/mottaquikarim/PYTH2.svg?branch=master)](https://travis-ci.org/mottaquikarim/PYTH2) ![GitHub](https://img.shields.io/github/license/mottaquikarim/PYTH2.svg)

![icon](assets/pycon.png?raw=true)
# PYTH2: Python Programming

*🎉🎈🎂🍾🎊🍻💃*

*A hands on and practical introduction
 to programming and python development.*

## [Online Classroom](https://pyth826.slack.com)

Slack is our online classroom - we will share class notes, videos, lectures, etc here.

## Table of Contents

Here are all the lectures for this course. This section will be updated with notes as we make our way through the curriculum.


### [WELCOME](src/README.md)
### [GETTING STARTED](src/Intro/README.md)
1. **[Tools and Resources](src/Intro/tools.md)**
2. **[Setting Up Our Environment](src/Intro/environment.md)**
3. **[Running Python Locally](src/Intro/installing_py_locally.md)**
4. **[FAQ](src/Intro/FAQ.md)**
### [LECTURES](src/Lectures_class2/README.md)
1. ✅  **[Intro to GA & Python - 8/26](src/Lectures_class2/Lecture1.md)**
2. ✅  **[Conditionals - 8/28](src/Lectures_class2/Lecture2.md)**
3. ✅  **[Conditionals & Lists - 9/4](src/Lectures_class2/Lecture3.md)**
4. ✅  **[Tuples, Sets, & Dicts - 9/9](src/Lectures_class2/Lecture4.md)**
5. ✅  **[Loops & Iterators - 9/11](src/Lectures_class2/Lecture5.md)**
6. ➡️  **[Modules & Functions Intro - 9/16](src/Lectures_class2/Lecture6.md)**
7. **[Functions - 9/18](src/Lectures_class2/Lecture7.md)**
8. **[Intro to OOP & Classes - 9/23](src/Lectures_class2/Lecture8.md)**
9. **[Classes - 9/25](src/Lectures_class2/Lecture9.md)**
10. **[Intro to Data Science - 9/30](src/Lectures_class2/Lecture10.md)**
11. **[Intro to Pandas Objects - 10/2](src/Lectures_class2/Lecture11.md)**
12. **[Pandas Data Processing I - 10/7](src/Lectures_class2/Lecture12.md)**
13. **[Pandas Data Processing II - 10/9](src/Lectures_class2/Lecture13.md)**
14. **[Pandas EDA I - 10/14](src/Lectures_class2/Lecture14.md)**
15. **[Pandas EDA II - 10/16](src/Lectures_class2/Lecture15.md)**
16. **[Pandas Data Analysis Lab - 10/21](src/Lectures_class2/Lecture16.md)**
17. **[Data Visualization - 10/23](src/Lectures_class2/Lecture17.md)**
18. **[Data Visualization Lab - 10/28](src/Lectures_class2/Lecture18.md)**
19. **[In-Class Project Work - 10/30](src/Lectures_class2/Lecture19.md)**
20. **[Project Presentations! - 11/4](src/Lectures_class2/Lecture20.md)**
### [TOPICS](src/Topics/README.md)
1. **[Essential Terminology](src/Topics/nb/essential_terminology.ipynb)** | **[Notes](src/Topics/Notes/essential_terminology.ipynb)**
2. **[Basic Data Types](src/Topics/nb/basic_data_types.ipynb)** | **[Notes](src/Topics/Notes/basic_data_types.ipynb)**
3. **[Conditionals](src/Topics/nb/conditionals.ipynb)** | **[Notes](src/Topics/Notes/conditionals.ipynb)**
4. **[Lists](src/Topics/nb/lists.ipynb)** | **[Notes](src/Topics/Notes/lists.ipynb)**
5. **[Dicts](src/Topics/nb/dicts.ipynb)** | **[Notes](src/Topics/Notes/dicts.ipynb)**
6. **[Loops](src/Topics/nb/loops.ipynb)** | **[Notes](src/Topics/Notes/loops.ipynb)**
7. **[Modules & Packages](src/Topics/nb/modules.ipynb)** | **[Notes](src/Topics/Notes/modules.ipynb)**
8. **[Functions](src/Topics/nb/functions.ipynb)** | **[Notes](src/Topics/Notes/functions.ipynb)**
9. **[List Comprehensions](src/Topics/nb/list_comprehensions.ipynb)**
10. **[Classes](src/Topics/nb/classes.ipynb)**
11. **[Data Science](src/Topics/nb/data_science.ipynb)**
12. **[Intro to Pandas Objects](src/Topics/nb/intro_pandas.ipynb)**
13. **[Exploratory Data Analysis w. 🐼](src/Topics/nb/preprocessing.ipynb)**
14. **[Pandas Analysis II](src/Topics/nb/eda.ipynb)**
15. **[Data Visualization](src/Topics/nb/data_viz.ipynb)**
16. **[Course Review](src/Topics/nb/course_review.ipynb)**
17. **[Python Project Ideas](src/Topics/nb/project_ideas.ipynb)**
### [HOMEWORK](src/Homework/README.md)
1. ✅  **[Homework 0 DUE - 9/4](src/Homework/hwk0.md)**
2. ✅  **[Homework 1 DUE - 9/9](src/Homework/hwk1.md)**
3. ➡️  **[Homework 2 DUE - 9/16](src/Homework/hwk2.md)**
4. **[Homework 3](src/Homework/hwk3.md)**
5. **[Homework 4](src/Homework/hwk4.md)**
6. **[Homework 5](src/Homework/hwk5.md)**
7. **[Final Project Reqs](src/Homework/final.md)**
### [RESOURCES](src/Resources/README.md)
1. **[Python Glossary](src/Resources/python_glossary.md)**
2. **[Basic Statistics](src/Resources/basic_stats.md)**
3. **[Pandas Glossary](src/Resources/pandas_glossary.md)**
4. **[General Reference Guides](src/Resources/genref.md)**
5. **[Libraries, Packages, & Other Tools](src/Resources/tools_libs.md)**
6. **[Cheat Sheets](src/Resources/cheat_sheets.md)**
7. **[Helpful Articles/Tutorials](src/Resources/articles.md)**
8. **[Open Source Datasets](src/Resources/datasets.md)**
### [ABOUT](src/About/README.md)
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

This also parses any `Lectures` folder and automatically swaps jupyter notebook links to it. Same for `Topics` folder in main README file.

## Instructional Team

Some info about your instructors.

### Taq Karim

<img src="https://github.com/mottaquikarim/JavascriptBootcamp/blob/master/assets/taq.jpg?raw=true" width="200" align="left"> 

[Hello, Wrold!](https://medium.com/@the_taqquikarim/console-log-hello-wrold-3e3abeb44396) I'm Taq, Tech Lead of the Demand Side (DSP) team at Place Exchange, a programmatic advertising exchange platform for Out of Home media. I'm also a lecturer, leading workshops and courses on a wide variety of topics (frontend / backend) in institutions such as Coalition 4 Queens (now Pursuit), The Startup Institute, NYCDA, OneMonth, The King's College and Columbia Splash. [I've taught Front-end Web Development at GA 14x](https://medium.com/@the_taqquikarim/10-lessons-learned-from-100-weeks-of-teaching-fewd-12c43db14f6b) (so far). When I'm not working I am usually [thinking about math](https://medium.com/math-musings/why-does-25-25-2-2-1-100-25-an-explanation-6c7e7b283d41), [building](https://medium.com/@the_taqquikarim/a-technique-for-saving-content-from-a-data-text-html-uri-10f045a8876d) [software](https://medium.com/@the_taqquikarim/introducing-bonfire-2c0e437895e2), [working](https://photos.app.goo.gl/w1crzgI7DqCgGR373) [on](https://photos.app.goo.gl/EaFkp5SmyO0opkg32) [hardware](https://photos.app.goo.gl/tvxPl2zbIMl7FEnK2) [hacks](https://www.instagram.com/p/8rARZNND_t/?taken-by=taqqui.karim) or hanging out with my cat, Layla Karim.

<!-- ### Julianna Garreffa

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/julianna.jpeg?raw=true" width="150" align="left">

Hi, I'm Julianna! I'm an experienced product manager and budding entrepreneur. I have experience in strategic roadmap planning, launching research-backed product features, orchestrating agile projects, directing technical client onboarding, analyzing data in R, and coding with HTML, CSS and Python. In my free time, I love traveling, volunteering with animals, cooking, and hearing live music. At home though, I'm probably reading or watching movies/TV, snuggled up with my cat, Layla Karim!

<br><br> -->

### Layla Karim

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/layla1.jpg?raw=true" width="200" align="left"> 

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/layla4.jpeg?raw=true" width="200" align="left"> 

<br>

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/layla2.jpg?raw=true" width="200" align="left"> 

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/layla3.jpg?raw=true" width="200" align="left"> 
