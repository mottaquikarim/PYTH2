<!---
{"next": "Topics/course_review.md","title": "Data Visualization"}
-->

# Data Visualization with Pandas & Matplotlib

In this section, we'll go over example code for different types of common visualizations.

## Objectives

* Describe why data visualization is important for communicating results.
* Identify how to select the correct visualization to use based on the data being presented.
* Identify characteristics to clearly communicate through data visualizations.


## How Do we Make Sense of a Data Set?

We're only looking at 1/3 of this data set! While all the data we need is here, it is difficult to make sense of and draw any meaning from.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-data-set.png)


## So What Is Data Visualization?

- A quick, easy way to convey concepts that from from large data sets.
- We can use these charts, graphs, or illustrations to visualize large amounts of complex data.


## Criteria for Crafting a Good Visualization

Visualizations should follow three (plus one) rules. They should be:

1. Simplified
2. Easy to Interpret
3. Clearly Labeled
4. (Bonus) Interactive


## How Do you Choose the Right Chart Type?

With so many chart types, it can be difficult to know how best to display your data.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/chart_types.png)

When creating a visualization first think about the variables you are showing (words, categories, numbers, etc., the volume of data, and the central point you are hoping to communicate through your visualization.


## When to Use a Bar Chart
Bar charts are one of the most simple and frequently used chart types. They are useful for illustrating either one string or one numeric variable, quickly comparing information, or for show exact values.

When thinking about using a bar chart consider:
- Will you use vertical or horizontal bars?
- How will you number your axis (it is always best to start at zero)?
- How will you order your bars?



## The Pie Chart in Action

As you can see from this example pie charts can be effective for proportions or percentages.

![](https://www.csisun.com/wp-content/uploads/2012/07/solarhotwaterpiechart.jpg)


## When to Use the Pie Chart Type

Pie charts are commonly misused. They show a part-to-whole relationship when the total amount is one of your variable and you'd like to show the subdivision of variables.

When thinking about using a pie chart consider:
- The more variables you have, as in the more slices of your pie you'll have, the harder it is to read.
- Area is _very_ difficult for the eye to read, so if any of your wedges are similarly sized think about a different chart type.
- If you want to compare data, leave it to bars or stacked bars. If your viewer has to work to translate pie wedges into relevant data or compare pie charts to one another, the key points you're trying to convey might go unnoticed.


## The Scatter Plot in Action

This scatter plot uses a combination of text, coloring, and labelling to describe the data. What is clear or unclear from this chart about the data set?

<img src="http://kbroman.files.wordpress.com/2013/02/science_scores.png" style="width: 70%; height: auto" />


## When to Use a Scatter Plot

Scatterplots are great for data dense visualizations and clusters. They are most effective for trends, concentrations, and outliers. They can be especially useful to see what you want to investigate further.


When thinking about using a scatter plot consider:
- This chart type is not as common so can me more difficult for an audience to read.
- If dots are covering up each other, consider a different chart type.
- A bubble chart is one variation on the scatter plot.
- Scatter plots are a great way to give you a sense of trends, concentrations, and outliers, and are great to use while exploring your data. This will provide a clear idea of what you may want to investigate further.

## Knowledge Check: Choosing a Chart


Annual sales in each state for a grocery store chain?

- Bar chart.
- Pie chart.
- Scatterplot.


## When to Use a Histogram


- Effective for distribution across groups.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/histogram.png)

- Histograms are useful when you want to see how your data are distributed across groups. Important: histograms are not the same thing as a bar chart! Histograms look similar to bar charts, but with bar charts, each column represents a group defined by a categorical variable; and with histograms, each column represents a group defined by a continuous, quantitative variable.
- One implication of this distinction: with a histogram, it can be appropriate to talk about the the tendency of the observations to fall more on the low end or the high end of the X axis.
- With bar charts, however, the X axis does not have a low end or a high end; because the labels on the X axis are categorical - not quantitative.

## Bar Chart vs Histogram

The main difference between a bar chart and histogram is that histograms are used to show distributions of variables while bar charts are used to _compare_ variables.

![](https://qph.fs.quoracdn.net/main-qimg-237e649130e7ae0245e003a6a1949b91.webp)


## Which type of chart?

Relationship of average income to education level?


- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.


## A Line Chart in Action

Line graphs are an excellent way to show change over time. While bar charts can also show time, they don't show it in a continuous way like a line chart.

![](https://static.guim.co.uk/sys-images/Guardian/Pix/maps_and_graphs/2012/4/25/1335374489202/Recession-and-recovery-ch-001.gif)


## When to Use a Line Chart

Line charts are particularly good at showing how a variable change over time. They work best if you have one date variable and one number variable.

When thinking about using a line chart consider:
- How many lines you'll need on your graph, the more overlapping lines there are, the harder your chart will be to read.
- Consider how many colors you need to use for your lines. Giving each line its own color forces the viewer to scan back and forth from the key to the graph.
- Individual data points can be hard to read, but line charts are good for showing overall trends.
- Similar to bar charts, try and start at 0 on your x axis.

## Knowledge Check: Which type of chart?

Change in average income since 1960 for American adults?

- Bar chart.
- Pie chart.
- Scatterplot.
- Line chart.
- Histogram.


## Returning to How to Choose the Right Chart


Check out [this series of charts](https://i.redd.it/e7alp8yrnb711.png): `https://i.redd.it/e7alp8yrnb711.png`

- Which is easiest to view the data?


It's subjective! There are pros and cons to each. Choosing a chart type depends firstly on the data you have. Secondly, it depends on the clearest way to convey your message. The alignment of these two aspects will help you decide what type of visualization to use.

## Charts & Code

There is an increasing array of libraries and tools to allow us to use code to create visualize data in compelling and approachable ways.

Check out this complex chart that was made using Python!

<img src="https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-chart.jpg" style="width: 70%; height: auto;"  />

*Source: u/dx034 on Reddit*


## Group Activity: Exploring Good Visualizations

Get in small groups of 2-3.

Go to [https://www.reddit.com/r/dataisbeautiful/top/](https://www.reddit.com/r/dataisbeautiful/top/). These are all data visualizations created by people like you!

Pick one that you think is particularly good and one that is particular bad. Why? What are the characteristics?


## Visual Attributes of Good Data Visualization

Some attributes affect our brain more strongly.

In order of focus:

- Position
- Color
- Size


## Summary

- The chart type you select should accurately represent the variables you are pulling from data in a way that is clearly readable for your audience.
- Visual considerations include: position, color, order, size. What else?
- With data visualizations becoming increasingly popular, a clean and clear chart goes a long way in conveying a message from a data set.


<div style="overflow: auto; width: 100%;">
	<iframe src="../Notebooks/data_viz.html" style="min-height: 800px; width: 100%; border: none;"></iframe>
</div>

## Lab

<div style="overflow: auto; width: 100%;">
	<iframe src="../Notebooks/omdb_viz_starter.html" style="min-height: 800px; width: 100%; border: none;"></iframe>
</div>


## [Solution](https://colab.research.google.com/github/mottaquikarim/PythonProgramming/blob/master/app/src/Notebooks/omdb_viz_solution.ipynb)

## Resources

* [44 Types of Graphs](https://visme.co/blog/types-of-graphs/)
* [8 Tips for Great Data Viz](https://www.gooddata.com/blog/8-ways-turn-good-data-great-visualizations)
* [Python Graph Gallery](https://python-graph-gallery.com/)
* [Data to Viz Interactive Diagram](https://www.data-to-viz.com/#explore)
* [How to Set a Color w. Matplotlib](https://python-graph-gallery.com/196-select-one-color-with-matplotlib/)
* [Python Colors & Color Palettes](https://python-graph-gallery.com/python-colors/)
* [Data to Viz Visualization Style Tips](https://www.data-to-viz.com/caveats.html)
