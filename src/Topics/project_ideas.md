<!---
{"next": "Homework/README.md","title": "Python Project Ideas"}
-->

# Python Project Ideas

## Overview

Your final project should address a data-related problem in a professional field that interests you. Pick any subject that you're passionate about! Your project should reflect significant original work inn applying data science techniques to an interesting problem. Although final projects are individual assignments, peer code review is strongly encouraged.

To help spark ideas, we put together a smorgasbord of cool [public data sources](../Resources/datasets.md). Using public data is the most common choice. If you have access to private data, that's also an option, though you'll have to be careful about what results you can release.

## Project Deliverables

You are responsible for creating a **project paper** and a **project presentation**. The paper should be written with a technical audience in mind, while the presentation should target a more general audience. You will deliver your presentation (including slides) during the final week of class.

Here are the components you should aim to cover in your **paper**:

* Problem statement and hypothesis
* Data dictionary
* Description of your data set and how it was obtained
* Description of any pre-processing steps you took (i.e. wrangling & cleaning)
* What you learned from exploring the data, including visualizations
* How you chose which features to use in your analysis
* Your challenges and successes
* Conclusions and key learnings
* Possible extensions or business applications of your project

Your **presentation** should cover summarize the above components and instead focus on creating an engaging, clear, and informative story about your project.

## Submission & Presentation

Deliver your project presentation and submit all required deliverables (paper, slides, code, data, and data dictionary).

Your project paper, presentation slides, and code should be included in a **GitHub repository**, along with all of your data and a data dictionary. If it's not possible or practical to include your data, you should link to your data source and provide a sample of the data (anonymized if necessary).

## Example Project Outline

### Question and Data Set(s)

What is the question you hope to answer? What data are you planning to use to answer that question? What do you know about the data so far? Why did you choose this topic?

Example:
* I'm planning to predict passenger survival on the Titanic.
* I have Kaggle's Titanic dataset with 10 passenger characteristics.
* I know that many of the fields have missing values, that some of the text fields are messy and will require cleaning, and that about 38% of the passengers in the training set survive.
* I chose this topic because I'm fascinated by the history of the Titanic.

### Data Exploration and Analysis Plan

What data have you gathered, and how did you gather it? What steps have you taken to explore the data? Which areas of the data have you cleaned, and which areas still need cleaning? What insights have you gained from your exploration? Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)? How might you use modeling to answer your question?

Example:
* I've created visualizations and numeric summaries to explore how survivability differs by passenger characteristic, and it appears that gender and class have a large role in determining survivability.
* I estimated missing values for age using the titles provided in the Name column.
* I created features to represent "spouse on board" and "child on board" by further analyzing names.
* I think that the fare and ticket columns might be useful for predicting survival, but I still need to clean those columns.
* I analyzed the differences between the training and testing sets, and found that the average fare was slightly higher in the testing set.
* Since I'm predicting a binary outcome, I plan to use a classification method such as logistic regression to make my predictions.