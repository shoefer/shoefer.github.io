---
layout: intuds_post
title:  "Overfitting - The Curse of Data Science"
date:   2015-08-07 15:00:00
categories: intuds
comments: true
intuds-weight: 5
---

We should agree by now that [data is a bunch of numbers](/intuds/2015/07/19/data-numbers-representations.html) encoding some information, and that data can be multi-dimensional which makes them live in [vector spaces](/intuds/2015/07/22/vector-spaces.html). 
We have also looked at the core competence of data science: learning  [functions](/intuds/2015/07/20/functions.html) from data. In this post we will find out why learning a function is actually such a difficult problem.

<!--
QUESTION: better explain by intuitive example, e.g. correlating the hypothesis that it is raining to the 
  hmm, but isn't that more about priors?
  -->

In the [last post](/intuds/2015/07/20/functions.html) I have introduced the stock price prediction problem: given the annual revenue of a company, we want to predict the company's stock price. I have given you set of example data and we have found the following regularity in the data:

<div class="pseudoformula">
<b>Stock price</b> = 0.00013 * <b>Revenue</b> + 70
</div>

I have told you that this regularity is a *linear* one which enables us to visualize it with a line:

{% include figure.html src="/intuds/images/2015-07-20-functions_sizeprice.png" width="65%" %}

More importantly, the regularity enabled us to predict the stock price given any annual revenue. Intuitively, when the the revenue gets higher, the stock price moderately increases.

Alhough I told you that these linear functions are really cool and mathematics can cope with them quite well you have probably already thought of many cases where linear functions do not suffice and we need different ones. And indeed, even in the stock price problem, there seems to be no reason for disregarding different functions, for example this one (red curve): 

{% include figure.html src="/intuds/images/2015-08-07-overfitting-sizeprice.png" width="65%" %}

It is not as nice as the line, but it perfectly passes through all of the data points. And
from an economic perspective this function looks much better as it predicts that if annual revenues exceed 1000000 Euro the stock price will go up much more quickly! So better go and by some shares now! 

### Occam's Razor

Let me give you a couple of reasons in defense of using the linear function. The first one is the function's simplicity: although both functions perfectly fit the data (both the blue line and the red curve perfectly coincide with the blue dots) the line has much less wrinkles than the curve - namely zero rather than six! For the line we do not have to choose whether the wrinkles go up or down, how high the go etc. 

In fact, this type of reasoning is very common has been brought up over 700 years ago by William of Ockham and is therefore called [Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor). It states that "among competing hypotheses that predict equally well, the one with the fewest assumptions should be selected". 

### Overfitting

Although Occam's Razor sounds like a good explanation, there is an even better reason for prefering the line in this stock price example. Occam's razor rejects the wrinkled function because we have to make too many choices about the direction and the size of the wrinkles. In fact, there are infinitely many wrinkled functions going through all of the points, for instance:

{% include figure.html src="/intuds/images/2015-08-07-overfitting-sizeprice2.png" width="65%" %}

The problem with that is that the chance of picking the *wrong* wrinkled function is much higher than picking the wrong line - because there is only *one line* that goes exactly through all of the points. I cannot rotate or shift the line up without it losing contact with one or more of the points. Therefore, we should prefer the line. So in a way, we have given a justification of Occam's razor by realizing that using a more complex function for predictions makes us more prone to making mistakes.

### Random fluctuations

In the case where the data lies exactly on a line the answer was clear that the line is the best choice. However, in reality, data is not perfect but almost always undergoes random fluctuations and noise. So let us make the stock prediction data a bit more realistic and then look at how well line and wrinkled function explain the data:

{% include figure.html src="/intuds/images/2015-08-07-overfitting-sizeprice_noise.png" width="65%" %}

We see that no line will be able to pass directly through all the data points, but have easily found a wrinkled function doing so. Still the line shown here seems to capture the main trend quite well. Which of the two functions do you prefer for making predictions about future stock prices? 

Since I have told you that the fluctuations are random, you will probably prefer the line - even though it does not fit the data exactly. Although the wrinkled function explains the individual data points well, it does not explain the trend of the function well; it focuses too much on explaining the random fluctations. Data scientists call this general effect *overfitting*, and we say that the wrinkled function *overfits* the data. 

### Battling Overfitting

Out there in the real world, discovering whether your function overfits or not is really hard. Probably, it is *the* problem of data science and machine learning. 
It is so prominent that two machine learning professors have even written a song about it. Seriously:

<div class="imgcenter">
<iframe width="560" height="315" src="https://www.youtube.com/embed/DQWI1kvmwRg" frameborder="0" allowfullscreen></iframe>
</div>

Luckily, there are a few things you can do to counteract overfitting apart from singing about it. I want to give you a few examples.

First, you can retain some preference for simpler explanations, by making a similar argument as before: even for the randomly fluctuating data there are still only a few lines that are  not too far away from any of the points. But since there are infinitely many wrinkled functions passing directly through all of the points, the chance of picking the wrong wrinkled function is very high. So using a simpler function is better.

Secondly, you can hold back some of your data and not use it for finding the function - you only use it *after* having computed the function to test how your function copes with that unseen data. If your function really sucks at explaining the data you have held out you should consider using a different or simpler function.

Third, you can use *more data*. In fact, this is way everyone is so excited about *big data* which heavily relies on lots of data being available.

Forth, you can get more knowledge about which shape of the functions you actually expect. If for example you know that the stock price varies in cycles, that is goes up, slightly down, then up again etc., you can try to find a function which reflects this knowledge.

Although all of these things are good ideas and there are many more, in the end there is only one thing you can do: cross your fingers and hope your function predicts the right thing. Understanding overfitting should hopefully make you think more critically about decision making - both in machines as well as in humans.

### Underfitting

Last but not least, let me say that of course also the opposite thing can happen: *underfitting*. If we choose a function that is too simple to explain a relationship we will not get a good prediction, either. I leave it as an exercise for you to think about a good example of underfitting.

<!--  Quadratic function -->

And in case you want to brag in front of your friends, here is some more terminology: the topic of this post, that a function learned from data always has to balance under- and overfitting is also called the *bias-variance trade-off*. *Variance* relates to the variance of all the different complex (e.g. wrinkled) functions that can explain the same data, causing overfitting. *Bias* refers to underfitting, stating that a too simple function adds a systematic bias to the prediction which cannot be overcome by the learner, not even when given more data.

In the next post we will look at the problem of overfitting in the more complex image classification scenario, and we will see how the dimensionality aggrevates the problem of learning and overfitting even more. 

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Finding the right predictive function for data is hard
- Even if the function perfectly fits the data it might be totally wrong: an effect called overfitting
- Occam's razor states that one should prefer simpler solutions
- A justification for this is: when using simpler functions we are less likely to pick the wrong one   
- Underfitting occurs when choosing too simple functions
- Singing about data science is fun 

### <a name="further"></a>Further Reading:
1. <a name="[1]"></a>[Lecture notes](http://courses.cs.washington.edu/courses/cse546/12wi/slides/cse546wi12LinearRegression.pdf) by Luke Zettlemoyer from University of Washington on overfitting.
2. <a name="[2]"></a>[Wikipedia article on Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor).
3. <a name="[2]"></a>[Simple Java applet](http://mste.illinois.edu/exner/java.f/leastsquares/) for playing around with data fitting. The switch "degree of polynomial" corresponds to the "wrinkles" in the function. 
