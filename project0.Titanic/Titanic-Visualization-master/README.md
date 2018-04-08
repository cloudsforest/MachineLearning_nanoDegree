# DataVisualization
Udacity Unit on d3.js &amp; dimple.js

## Summary 
This visualization shows the demographics of 891 of the 1317 passengers aboard the Titanic. Specifically, gender, class, port of embarkment, age, and number of family members aboard were explored. There were more men than women, more third class passengers than first class, and the most common age range was between 21 - 30.  Next, survivorhsip within each of these categories was explored.  Unsurprisingly, women, children, and first class passengers were more likely to survive.

## Design 

### Dataset information
This dataset is taken from [Kaggle]( https://www.kaggle.com/c/titanic/data?train.csv#) website.  I cleaned the data by removing categories I was uninterested in (passenger name, cabin number, fare) and creating a new one which combined the number of spouses/siblings and parents/children abroad and a new one which put passengers into age "bins".

### Version 1
My inital idea is to move progressively through the data from simple to more complex. The first set of visualizations will simply show the breakdown of theses passengers in terms of gender, age, ticket class (first, second, or third class), port of embarkment, and number of family members abroad.  Second, will focus on survivorship, first by showing the total number of survivors and non survivors and then breaking down the original visualization into these categories.  Finally, the visualization will show each of these categories as percentages rather than raw numbers.  In the future, I would like users to be able to select certain demographics (First class, single, female, in her 20s, embarked in Southampton) and see what the survival rate for that particular demographic is.

### Version 2 (based on feedback #1 and #2)
I clarified "unknown" categories in the description and also labeled the unknown category in the age graph. I fixed some typos (thanks Mom) and reordered one of the graphs so that it had the same survived/perished coloring as the others.  Additionally, I changed the position of the hover tooltip which had somehow migrated into the upper left hand corner. I personally liked the aesthetics of the old tooltip better, but could not find a way to customize only the position. I had to recreate the entire tooltip from scratch, so it looks more basic than the old one. I also added additional visualizations to the conclusion that explore why Southampton had such lower survival rates, since both of my reviewers were curious about this. I played around with making axes labels larger, since one reviewer complained about this, but ended up sticking with the 10px default font because it allowed all of the information to fit in. (Sorry mom.) 

### Version 3 (based on feedback #3 and own ideas)
I reverted back to the original tooltip after discovering that the issues with the old one were related to my version of dimple (2.1.6 rather than 2.2.0) and unncessary lines of code. The old tooltip is much prettier and now it's in the right position too! I also added labels inside of the bars for graphs with percentages, so that the absolute number of passengers was easily seen.  I reformatted the charts so that all axes labels could be seen (reviewer #3 was having problems). I did this by setting bounds on some of the charts and adding percentage margins.  I felt that the page was too long vertically and that the user might enjoy more interactivity so I added a navbar to transition from one part of the visualization to another.  

## Feedback 
### Feedback #1:
> What do you notice in the visualization?

Graphs are presented in a simple and straightforward manner that affords easy and quick interpretation. The two-color scheme of bar graphs offers simplicity and dissuades potential distraction in understanding and interpreting data.

The titles of each graph, e.g., Gender Breakdown, Class Breakdown, etc.  are clearly presented (large size font).  It would help in visualizing data if font size of Y and X axis labels are also enlarged. 

> What questions do you have about the data?

1.	In the Age/Survivor Breakdown graph, the last graph is not labeled. Is this for another age category – 81 -?
2.	Why is there a category “Unknown” in the graph on “Port Survivor %”?  If there’s a reason for including this category, it’s not clear to me .  
3.	The placement of the label “Port of Embarkment” is not on the same line as the titles of other categories, i.e., Gender and Ticket Class.
4.	 Due to large numbers of third class passengers and those who embarked from Southampton, could these categories potentially skew the relationships on survivorship drawn from the data? 
5.	There are no survivors among those with number of family members 7 and 10. Is there a possible explanation on why this is so?  
6.	Is there historic evidence that first class passengers were given priority? If so, would it explain this category’s high rate of survivorship?

> What relationships do you notice?

Percent of survivorship is greater among women (than men) and children (than older passengers). Writer noted that these trends are supported by historic evidence that women and children were given priority in being allowed to go to life boats.

> What do you think is the main takeaway from this visualization?

The main takeaway is that graphs are an excellent tool in presentation of data. When graphs are presented in a simple and straightforward design, data are more easily understood. 

> Is there something you don’t understand in the graphic?

No. Graphic is excellent and allowed easier understanding of data.

### Feedback #2:
> What do you notice in the visualization?

The visualization displays information about the Titanic passengers in a very clear format.  The progression from frequency, to survivorship and then to relative frequency helps illustrate arguments regarding likelihood of survival more clearly.  For example, looking at survivorship of children younger than 11 years old it is hard to tell that the majority of them survived.  I also have noticed that it is hard to pinpoint the exact value the bars represent, but there is a convenient tool that allows me to see which y-value it corresponds with.  I also noticed a few mistakes / inconsistencies in the graphs for Gender/Survivor breakdown and Age survivor breakdown and %.
 
> What questions do you have about the data?

I would be interested in knowing the greatest determinant of survival on the Titanic and why Southhampton had a much larger relative frequency of deaths (did they have the most 3rd class passengers maybe?).

> What relationships do you notice?

I notice that a greater percentage of women and children survived as compared to men.  I noticed that a greater percentage of first and second class passengers survived as compared to third class passengers.  I noticed that there were a lot more men on the ship than women (why is this true?).  I also noticed that, outside of being younger than 11, there was no distinct advantage for any particular age group in terms of survival.  I agree with the author's claim that the data shows that women and children were given priority for fleeing the ship.

> What do you think is the main takeaway from this visualization?

The main take away for me is that third class passengers were much less likely to have survived the accident than first class passengers.  
 
> Is there something you don’t understand in the graphic?

The graphics are very clear and easy to read.  There are just some small errors:  
1. the Gender/Survivor breakdown graph, why are the colors switched for perished and survived as compared to the others? 
2. the Age survivor breakdown and % there is a category missing, is this the category for unknown age?

### Feedback #3

> What do you notice in the visualization?

I  notice that…
There was a gender imbalance on the ship – close to double!       (I like the way the curser will make the line to do an accurate reading). I imagine there were probably more men than women although this is not stated. I also notice that the graph is more complex than the ones I am used to  - although it starts at zero the area between 0-200 is disproportionate to the rest of the graph. This initially made me read the graph inaccurately; I had initially thought that there were more than double the difference in the gender population. This is the same in the adjacent class breakdown.  

> What questions do you have about the data?

Which gender was more represented on the ship
In the class breakdown, does the largest bar graph represent the people who were migrating? Were there mostly men in the longest bar of class breakdown – the bar which I imagine represent the class immigrating. 
Does your data include people working on the ship? 

> What relationships do you notice?

I imagine the longest bar on the gender breakdown is male and the population on the class breakdown were probably male. 
The longest bar on both graph is the same amount. 

> What do you think is the main takeaway from this visualization?

That there is a connection between the class breakdown and the gender breakdown. 

> Is there something you don’t understand in the graphic?

- Is there a reason that the graph a smaller measurement? For me, it makes it more difficult to read.
- Is there a reason why no labels were added under the bars? Was it to encourage the inference of data? 

## Resources 
(Listed in order of usage)

- Titanic Wikipedia Entry https://en.wikipedia.org/wiki/RMS_Titanic
- Titanic Facts http://www.titanicfacts.net/titanic-passengers.html
- Dimple.js documentation http://dimplejs.org/examples_index.html
- Udacity Forum Discussion https://discussions.udacity.com/t/beginner-help-with-dimple-js-and-javascript-in-general/203196
- Udacity Forum Discussion https://discussions.udacity.com/t/project-6-feedback-and-help-request-titanic-data/198669
- Vverde's repository https://github.com/vverde/Udacity-Data-Analyst-Nanodegree-P6
- Stack Overflow Exchange http://stackoverflow.com/questions/17791926/how-to-rotate-x-axis-text-in-dimple-js
- Stack Overflow Exchange http://stackoverflow.com/questions/33179439/d3-js-dimple-getting-a-title-on-a-graph
- Dimple Wiki on Github https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.series#addOrderRule
- DailyMail Article http://www.dailymail.co.uk/debate/article-2087585/Cruise-ship-Costa-Concordia-sinking-Whatever-happened-women-children-first
- Udacity Forum Discussion https://discussions.udacity.com/t/custom-tooltip-legend-order/189042/6
- Anna Pawlicka's tooltip tutorial http://annapawlicka.com/pretty-charts-with-dimple-js/
- Stack Overflow Exchange http://stackoverflow.com/questions/30434627/how-to-change-the-position-and-size-of-the-tooltip-in-dimple-js
- Dimple.js Storyboard Control http://dimplejs.org/advanced_examples_viewer.html?id=advanced_storyboard_control
- Udacity Forum Discussion https://discussions.udacity.com/t/dynamic-buttons-between-cabin-class-and-sex/177482/4
- Stack Overflow Exchange http://stackoverflow.com/questions/4247067/jquery-menus-appear-disappear-on-click-v2/4247689#4247689
- w3 Schools CSS http://www.w3schools.com/css/css_navbar.asp
