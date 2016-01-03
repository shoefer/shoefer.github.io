---
layout: intuds_post
title:  "The Curse of Dimensionality"
date:   2016-01-03 13:45:00
categories: intuds
comments: true
intuds-weight: 8
intuds-category: Learning from Data
---

In the last post we have looked at one of the big problems of machine learning: when we want to learn [functions](/intuds/2015/12/28/functions.html) from data, we have to fight [overfitting](/intuds/2015/08/07/overfitting.html). In this post we will look at another archenemy of learning: dimensionality.

### Parameters

Let's briefly recap our stock price prediction example. In an [earlier post](/intuds/2015/12/29/learning-functions.html) we used random search to find the parameters of a line that explains the training data examples well. 
The algorithm learned two numbers, namely the *parameters* p<sub>1</sub> and p<sub>2</sub>:

<div class="pseudoformula">
f(<b>Revenue</b>) = p<sub>1</sub> * <b>Revenue</b> + p<sub>2</sub>,
</div>

where visually, p<sub>1</sub> changes the slope of the line and p<sub>2</sub> the shift along the y-axis of a line.

The random search learned the numbers p<sub>1</sub>=0.00015 and p<sub>2</sub>=58:

{% include figure.html src="/intuds/images/2015-12-29-learning-random_guess.png" width="500"  %}

This line is not very far away from the parameters of the "true" function  p<sub>1</sub><sup>true</sup>=0.00013 and p<sub>2</sub><sup>true</sup>=70. Interestingly, for the learned function the slope p<sub>1</sub> is a bit higher, but this is "compensated" by a lower shift p<sub>2</sub>. Intuitively, this makes sense: the higher the slope, the more we need to shift the line downwards in order to approximately hit the training examples. We will see in a second why this observation is important.

### Adding dimensions

Now, I would like to reason about the influence of the number of parameters of a function on the difficulty of learning that function. You can think about the parameters of the line, but in fact I will formulate it in a general way.

For the sake of the argument let's assume that we do not consider all possible numbers as possible parameter values, but that we restrict ourselves a fixed list of numbers (in mathematics that's called *discretization*), and we make this list finite. To make it really simple, we will only use the numbers from 1 to 10. 

Assume that we have a function that has only *one* parameter (for example, only the slope of a line), we immediately see that there are 10 possible values that the parameter can take. We visualize each value of the parameter by a blue box:

<table border="0" style="border-collapse: collapse; margin: 0 0 15px 25px;">
<tr>
{% for i in (1..10) %}
<td style="width:40px; height:30px; border:1px solid blue; font-size: 8pt; color: blue; " align="center">
{{ i }}
</td>
{% endfor %}
</tr>
</table>

What happens if we add a second parameter that can take 10 values? Well, you might think that results in 10 values for parameter one and another 10 for parameter two, which makes 20. But unfortunately that's wrong: we need to consider all possible combinations of the parameter values! The reason is that the parameters are usually dependent as we have seen in the line example: when changing parameter one (here the slope), we can still improve how well the line fits the data by changing parameter two (shift). Let's visualize all possible combinations:

<table border="0" style="border-collapse: collapse; margin: 0 0 15px 25px;">
{% for j in (1..10) %}
<tr>
{% for i in (1..10) %}
<td style="width:40px; height:30px; border:1px solid blue; font-size: 8pt; color: blue; " align="center">
({{ j }}, {{ i }})
</td>
{% endfor %}
</tr>
{% endfor %}
</table>

We see that we have 10 *times* 10, i.e. 100 possible parameter pairs. What happens if we add a third parameter? We get a cube with 10 times 10 times 10 equals 1000 parameters! And with 10 parameters each taking 10 values, we get 10.000.000.000 which are 10 billion different combinations of parameter values!

You probably see the formula behind our reasoning: If we have *n* values a parameter can take, and *m* parameters, we end up with *n*<sup>*m*</sup> possible parameter value assignments. We say that the number of parameter values grows *exponentially*.

Now how big of a problem is it? Well, it is very big indeed, which is why this problem is called *the curse of dimensionality*. The problem is that data are usually high-dimensional, and that each parameter usually has significantly more than 10 possible values.

For example, the tiny pictures we played around with in an [earlier post](/intuds/2015/07/25/vector-spaces.html) had 27x35, that is 945 pixels. If we were to learn a function that has a parameter for every pixel and again every parameter can only take 1 out of 10 values we would still end up with 10<sup>945</sup> parameter values - this is a number consisting of a 1 with 945 trailing zeros, and it is several orders of magnitudes higher than the [number of particles in the entire universe](http://www.quora.com/How-many-particles-are-there-in-the-universe)! We will never be able to try out even a tiny fraction of all possible parameter values.

So we see that the curse of dimensionality forces us to find smarter ways of finding the parameters of functions. We will save this for a later articles.

### Hughes effect

Irrespective of the way how smart we go about searching for parameters, high dimensionality has another very problematic (and somewhat unintuitive) implication, namely for classification. This problem is also known as the *Hughes effect*.
I will only sketch the idea very briefly but you find a more elaborate explanation with nice illustrative figures [in this blog article](http://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/).

The problem is stated as follows: recall that in classification, we aim to find a function that discriminates between two or more categories of input data. We presented a way of doing so, namely by finding [hyperplanes in space](/intuds/2015/07/25/vector-spaces.html) that separate the categories. So how much easier or simpler does it get to find a hyperplane if the dimensionality of the data is higher?

Here comes the problem: the more dimensions the data has, the *easier* it is to find a hyperplane separating categories in the *training data*; but at the same time, the *harder* it gets to also perform well on the *unseen data* (for example, *test data*). The reason is that because we have more dimensions that we can choose from to lay the hyperplane through, we are much more prone to [overfitting](/intuds/2015/08/07/overfitting.html). Thus, having higher-dimensional data has the same effect as allowing our function to have more "wrinkles". And the less training data we have, the less sure we are that we have identified the dimensions that really matter for discriminating between the categories.

<!--
<div class="pseudoformula">
f(<b>Image</b>) = 1	&nbsp;&nbsp;&nbsp; if <br/>
&nbsp;&nbsp;&nbsp; <b>Image</b><sub>(1,1)</sub> * 10  + <br/>
&nbsp;&nbsp;&nbsp; <b>Image</b><sub>(1,2)</sub> * 1.1  + <br/>
&nbsp;&nbsp;&nbsp; ... <br/>
&nbsp;&nbsp;&nbsp; <b>Image</b><sub>(27,35)</sub> * 2.5 <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &gt; 0
f(<b>Input</b>) = 0	&nbsp;&nbsp;&nbsp; otherwise
</div>

### Real dimensionality of data
-->

### Summary

In this post, we got to know another nemesis of data: high dimensionality. When looking at learning from the perspective of searching for the right parameters, each additional dimensionality means that we must search an exponential number of more parameter values. And in classification, every additional dimension makes it harder to find the right hyperplane to discriminate between the categories.

But another curse is already on its way; and it has to do with (no) free lunch. 


### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Curse of dimensionality refers to the dimensionality of the data and parameters to be learned
- Searching for the right parameter values becomes exponentially harder with every dimension
- Similarly, in classification every dimension makes us more prone to overfitting by choosing the wrong dimension as discriminatory

### <a name="further"></a>Further reading:
1. <a name="[1]"></a>Excellent [blog article](http://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/) by Vincent Spruyt on the curse of dimensionality in classification, aka the Hughes effect.
