---
layout: intuds_post
title:  "The Curse of Dimensionality"
date:   2015-12-31 15:00:00
categories: intuds
comments: true
intuds-weight: 8
intuds-category: Learning from Data
---

In the last post we have looked at one of the big problems of machine learning: when we want to learn [functions](/intuds/2015/07/20/functions.html) from data, we have to fight [overfitting](/intuds/2015/08/07/overfitting.html). In this post we will look at another archenemy of learning: dimensionality.

### Parameters

Let's start with running stock price prediction example. In an [earlier post](/intuds/2015/12/29/learning-functions.html) we used random search to find the parameters of a line that explains the data samples we had well. 
The algorithm learned two numbers, namely the *parameters* p<sub>1</sub> and p<sub>2</sub>:

<div class="pseudoformula">
f(<b>Revenue</b>) = p<sub>1</sub> * <b>Revenue</b> + p<sub>2</sub>,
</div>

where visually, p<sub>1</sub> changes the slope of the line and p<sub>2</sub> the shift along the y-axis of a line.

The random search learned the numbers p<sub>1</sub>=0.00015 and p<sub>2</sub>=58:

{% include figure.html src="/intuds/images/2015-12-29-learning-random_guess.png" width="500"  %}

This line is not very far away from the parameters of the "true" function  p<sub>1</sub><sup>true</sup>=0.00013 and p<sub>2</sub><sup>true</sup>=70. Interestingly, for the learned function the slope is a bit higher, but this is "compensated" by a lower shift. Intuitively, this makes sense: the higher the slope, the more we need to shift the line downwards in order to approximately hit the training examples.

### Adding dimensions

Now, I would like to reason about the influence of the number of parameters of a function on the difficulty of learning that function. You can think about the parameters of the line, but in fact I will formulate it in a general way.

For the sake of the argument let's assume that we do not consider all possible numbers as possible parameter values, but that we restrict ourselves a fixed list of numbers (in mathematics that's called *discretization*), and we make this list finite. To make it really simple, we will only use the numbers from 1 to 10. 

Assume that we have a function that has only *one* parameter (for example, only the slope), we immediately see that there are 10 possible values that the parameter can take. We visualize each value of the parameter by a blue box:

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

We see that we have 10 *times* 10, i.e. 100 possible parameter pairs. What happens if we add a third parameter? We get a cube with 10 times 10 times 10 equals 1000 parameters! 

You probably understand the formula: If we have *n* values a parameter can take, and *m* parameters, we end up with *n*<sup>*m*</sup> possible parameter value assignments. We say that the number of parameter values grows *exponentially*.

Now how big of a problem is it? Well, it is very big indeed which is why this problem is called *the curse of dimensionality*. The problem is that data are usually high-dimensional.
For example, the tiny pictures we played around with in an [earlier post](/intuds/2015/07/25/vector-spaces.html) had 27x35, that is 945 pixels. We could build a function that multiplies every pixel with a parameter.
If we again assume that every pixel can only take 1 out of 10 values (which is not true because cameras can differentiate between many more shades of gray) we would still end up with 10<sup>945</sup> parameter values - this is a number consisting of a 1 with 945 trailing zeros, and it is several orders of magnitudes higher than the [number of particles in the entire universe](http://www.quora.com/How-many-particles-are-there-in-the-universe)! We will never be able to try out all of these parameters.

So we see that the curse of dimensionality forces us to find smarter ways of finding the parameters of functions.

### Hughes effect

Unfortunately, high dimensionality has another very problematic (and somewhat unintuitive) implication, namely for classification. In classification, we aim to find a function that discriminates between two or more categories of input data. We looked at the [image classification problem](/intuds/2015/07/25/vector-spaces.html), categorizing whether an image is a picture of me, Sebastian, or of a blowfish.

Remember that the classification function we wanted to find is a hyperplane, and that images from one category lie on one side, and images from another category on the other side of that hyperplane. The hyperplane lies in the space of 945 pixels. 

[in this blog article](http://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/)

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
-->

*With every dimension we add to the data, we add one more possibilities to separate the data*. What is the right split then?

http://www.edupristine.com/blog/curse-dimensionality

<!--
### Real dimensionality of data
-->



### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- 

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a> Note that this decision function does not exactly correspond to the notion of a separating hyperplane; the decision function for the hyperplane would first multiply all pixel values with a set of parameters, and than look at the resulting number. But since the functions are somewhat similar, we can pretend that they are the same  for the sake of the argument.

