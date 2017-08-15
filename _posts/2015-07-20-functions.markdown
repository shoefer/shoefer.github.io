---
layout: intuitivemi_post
title:  "Functions as Data Translators"
date:   2015-12-28 18:10:00
categories: intuitivemi
comments: true
intuitivemi-weight: 4
intuitivemi-category: Basics
---

If you have read the previous posts carefully you should now be familiar with high-dimensional data. In this last introductory article we are now going to look at what machine intelligence people mean when they think about manipulating data: they apply *functions* to data.

We will learn what functions are and look at different examples. Once we know what they are, we can in the next post see how to learn them - which is essentially what learning machines do.

## Mathematical Functions

Mathematicians use the term function rather differently from the common sense definition. In everyday language we talk about the function of things in the sense "what is the purpose of the thing" or "how does this thing work". A function in mathematical sense is rather different. It can be best thought of as a translation from one type of data to another type. Or in other words, you give some input (data) to the function, and get some output (data):

{% include figure.html src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Function_machine2.svg" width="35%" %}

(This figure and the first example are taken from the highly recommended [Wikipedia page on functions](https://en.wikipedia.org/wiki/Function_(mathematics)))

Let me give you a couple of examples of these things called functions.

#### Object description functions

Let's assume a couple of primitive shapes, such as triangles, squares, etc. all of different color. We can now define a function that, given a shape, outputs the color of the function:

{% include figure.html src="/intuitivemi/images/2015-07-20-functions-color_example_wp.svg" width="35%" %}

This visualization shows how to map *input data* X (the shape) to some *output*, the shape's color Y. All the arrows between X and Y are the defining elements of the function. 

Note that for each object in X there is only one arrow pointing away from it. This is indeed a requirement because we want a function to be a unique mapping: for each input we get exactly one output. The inverse is not required, though: the square and the triangle have the same color, so the red color in Y has two arrows pointing to it. You also notice that some colors, namely blue and purple have no arrows pointing to it. All of these things are very common in functions.

<!--
We can also come up with a whole bunch of other functions, defined on shapes: for example, we could define functions that counts the edges of each shape; or a function that calculates the area of the shape, and so on.
-->

<!-- You see, many concepts and things can be cast as function. However, 
-->
So far we have only talked about functions conceptually but we have not stated how a function *can automatically compute* the output from the input. Let us therefore look at a simpler example to shed some light on this.

#### Stock price prediction function

Let us now re-introduce our simple example from the [introductory post](/intuitivemi/2015/07/28/datascience-showoff.html). We want to assess the stock price of some company. For the sake of simplicity, we will only use information about the annual revenue of the company (in Euro) and try to predict the stock price (also in Euro). We can describe this relationship in a big table:

<table class="data-table">
<tr>
<th style="color: gray">Year</th>
<th>Annual Revenue in January (Euro)</th>
<th>Price (Euro)</th>
</tr>
<tr>
<td style="color: gray">2010</td>
<td>40.000</td>
<td>122</td>
</tr>
<tr>
<td style="color: gray">2011</td>
<td>50.000</td>
<td>135</td>
</tr>
<tr>
<td style="color: gray">2012</td>
<td>60.000</td>
<td>148</td>
</tr>
<tr>
<td style="color: gray">2013</td>
<td>80.000</td>
<td>174</td>
</tr>
<tr>
<td style="color: gray">2014</td>
<td>100.000</td>
<td>200</td>
</tr>
</table>

This table can be considered a function in at least three ways: either we use the year as input, we use the annual revenue as input, or we use the stock price as input. We choose the annual revenue as the input and the stock price as the output because we believe that the annual revenue is more predictive for the stock price than the year - if the company was founded 10 years earlier, we would still expect the relationship of annual revenue and stock price to be similar (unless there was something like a global crisis, but we ignore that for now).

So the input of our function is *annual revenue* and the output *stock price*. And "computing" this function is very simple: given a number for the annual revenue, we look up the row in the table containing this number and return the corresponding stock price.

Such tabular functions are common but they have a severe drawback: we cannot *extrapolate* - from this table alone we do not know how to get the value for the stock price for an annual revenue of 90.000 Euros or 200.000 Euros! 
However, the example data I have given exhibits a regularity (surprise, surprise!), namely that the stock price values in the right column are exactly 0.00013 times the annual revenue plus 70 (check this for yourself). This gives us a much more concise way of describing this function:

<div class="pseudoformula">
<b>Stock price</b> = 0.00013 * <b>Revenue</b> + 70
</div>

You see that the function gets as input the revenue, and gives as output the stock price. To make this even clearer, we usually denote the function by the symbol *f* and write:

<div class="pseudoformula">
f(<b>Revenue</b>) = 0.00013 * <b>Revenue</b> + 70
</div>

The parentheses behind the *f* contain the inputs of the function, sometimes called *arguments*.

Let us visualize this function by plotting a graph which has on one axis (the *x-axis*) the annual revenue and on the other (the *y-axis*) the stock price:

{% include figure.html src="/intuitivemi/images/2015-07-20-functions_sizeprice.png" width="65%" %}

We see two interesting things here: first, we can now *predict* the stock price value from the annual revenue, no matter which revenue. Secondly, the relationship between revenue and stock price in our example turns out to be a line. The fact that such relationships / functions can be drawn by a line results in them being called *linear functions*. Linear functions are amongst the most important types of relationships in mathematics - and actually they are one of the few that mathematics can really deal with [[2]](#[2]). Therefore, the majority of methods in machine intelligence are based on linear functions as the one given here. 
<!-- We will talk about them in more detail in the next article. -->

<!--
##### Truthfulness of a function

In the previous paragraph, I have come up with a function to predict the stock price, by postulating a linear function that relates annual revenue to stock price. Now the question is: Who guarantees this function is actually "true" in the real world? 

To be honest:  *no one* can guarantee you that! I have come up with this function because I saw the regularity in the data; but  I might be totally off. Maybe the stock price drops at 1100000 Euros annual revenue? 
-->

In this example, we have talked about functions that takes a single number as input, and outputs another single number. Let's now look how functions can be applied to vectors.

#### Vectorial functions

In the [previous post](/intuitivemi/2015/07/25/vector-spaces.html) we have dealt with the question of representing high-dimensional images as vectors. Of course, we can also define functions on these vectors. Recall that a vector is merely a list of numbers of fixed size, e.g. a 3-dimensional vector looking like this:

<table class="data-table">
<tr>
<td style="background-color: #000; opacity: 0.909; width: 30px">0.909</td>
<td style="background-color: #000; opacity: 1.0; width: 30px">1.000</td>
<td style="background-color: #000; opacity: 0.860; width: 30px">0.860</td>
</tr>
</table>

So let's define a *linear* function on 3-dimensional *vectors*: 

<div class="pseudoformula">
f<sub>a</sub>(<b>Image</b>) = f(<b>Image</b><sub>1</sub>, <b>Image</b><sub>2</sub>, <b>Image</b><sub>3</sub>) = 2*<b>Image</b><sub>1</sub> + 5*<b>Image</b><sub>2</sub> - 1* <b>Image</b><sub>3</sub>
</div>

What does this function do? With the little subscript we denote the individual dimensions of the input image. The function therefore computes the sum of the individual dimensions of the input vector, each dimension multiplied with some number. These numbers (here 2, 5 and -1, which I have chosen arbitrarily in this example) are called the *parameters* of a function. The result for this function applied to the example vector above is:

<div class="pseudoformula">
f<sub>a</sub>(<b>Image</b>) = 2*0.909 + 5*1.0 - 1*0.86 = 5.958
</div>

At first sight this function does not really seem to make much sense. Why should we sum up pixel values of an image? For example, it allows us draw some conclusions on whether the image is rather dark (low value of f<sub>a</sub>) or light (high value); and the different parameters of f<sub>a</sub> allow us to emphasize certain regions of the image more than others. 
We will see later that this is actually very useful for recognizing things in images.
<!--
But wait a second: we have as many parameters (2, 5 and 1) as input dimensions. This means, if the input data is an image, the parameters are in principle also an image! If you now think of input that are real 945-dimensional images, the parameters of the function can be used to "weigh" certain areas of the images higher. If you don't quite see this now, don't worry, we will talk about this later.
-->

You might have noticed that the previous function mapped a vectorial input to a single number. But we can also define functions that map vectors to vectors:

<div class="pseudoformula">
f<sub>b</sub>(<b>Image</b>)</b> = [ &nbsp;&nbsp;&nbsp; 2*<b>Image</b><sub>1</sub> + 4*<b>Image</b><sub>2</sub>,
	&nbsp;&nbsp;&nbsp; 3*<b>Image</b><sub>2</sub> + 1*<b>Image</b><sub>3</sub>
&nbsp;&nbsp;&nbsp;]
</div>

This function maps the 3-dimensional input vector to a *2-dimensional* output vector by summing over subparts of the input (the brackets indicate that the output is a vector, and the comma separates the two output dimensions). These types of functions will be very useful as they allow us to transform data into different representations, for example lower-dimensional ones.

####  Image classification function

I will now introduce a last type of functions which I call decision functions or *classification functions*. In a nutshell, these functions look like that:

<div class="pseudoformula">
f<sub>c</sub>(<b>Input</b>) = 1	&nbsp;&nbsp;&nbsp; If <b>Input</b> &gt; 10  <br/>
f<sub>c</sub>(<b>Input</b>) = 0	&nbsp;&nbsp;&nbsp; otherwise
</div>

Classification functions map input data to 2 (or more) categories which we simply enumerate from 0 to the number of categories (minus one).

If we put together classification functions with our knowledge about vectorial functions, we can reconsider the example in the [previous post](/intuitivemi/2015/07/25/vector-spaces.html) we have seen that we can draw (hyper)planes to separate two categories of objects, namely blowfish and Sebastians:

{% include figure.html src="/intuitivemi/images/2015-07-21-vector_spaces-arrow-plane.png" width="500" height="375" gifplayer="true" id="vector-spaces-arrow-plane" %}

We would now assign the category Sebastian to 0 and blowfish to 1, and make the if-else-part of f<sub>c</sub> such that it takes into account whether an input sample lies on one or the other side of the line. I will not write that out explicitly, but in fact the left-of-or-right-of-line can also be cast as a multiplication of the input with a bunch of numbers. So classification functions are exactly what we want if we want to solve classification tasks - surprised?

#### Relationship between functions

Before closing this article, I would like to point out the relationship between the stock price and the image classification function.

For image classification, the trick for visualizing the hyperplane that separated Sebastians from blowfish was to shrink the 27x35 images to a 3x1 image which allowed us to treat images as points (vectors) in 3D space.
What does this look like if we shrink the images even further, namely to a 2x1 image? We can then visualize the images as vectors in 2D. Similar as before we can now ask how to separate the shrinked Sebastians and blowfish. The answer is that we have to find a "2D hyperplane" - which turns out to be just a line!

{% include figure.html src="/intuitivemi/images/2015-07-20-functions_image_class_2d.png"  width="65%" id="2015-07-20-functions_image_class_2d" %}

Interestingly, this looks very much like the stock price prediction above. The main difference is that we do not draw the line *through* the data but in such a way to *separate* the data. Still, in both applications we use a *linear* function. 

<!--
Therefore, we can down write the Sebastian-vs.-Blowfish discriminator in the following way:
<div class="pseudoformula">
<b>Category = <i>Sebastian</i></b> &nbsp; <b>IF</b> { -0.9 * <b>gray value 1</b> + 0.00013 * <b>gray value 2</b> + 1 } <b> &gt; x </b><br/>
<b>Category = <i>Blowfish</i></b> &nbsp; <b>IF</b> { -0.1 * <b>gray value 1</b> + 0.00013 * <b>gray value 2</b> + 1 } <b> &lt; x </b><br/>
</div>
The expression in 
The two expressions only differ with respect to the &gt; or &lt; after the linear expression.
-->

Maybe it's now a bit clearer how these linear functions translate into higher-dimensional spaces: the plane is a generalization of the line to 3D, and the hyperplane a generalization of the line/plane to higher dimensions! So in the future if we think about discriminating hyperplanes, we will usually visualize this as a line or a plane separating two sets of 2D or 3D points. And as before the mathematical field of [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) describes how to deal with these lines, planes and hyperplanes. 

#### Summary

For now, you should have gotten a feeling for what functions do: translating input to output data. Functions can take different inputs and return different outputs, such as numbers and vectors. (In fact, they can even take other functions as inputs as well! But we won't bother with these insane cases now.)

In the next post, we will get to the real meat: how to learn functions automatically.

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Functions in the mathematical sense translate an input to an output
- The simplest and best understood functions are linear functions
- Functions map between numbers, or more general, vectors.
- Functions can map to single numbers, but also to vector
- If functions map onto a limited set of categories/classes, we call them classification functions

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Of course this is largely oversimplified. The actual price would also depend on the size of the company at the time, economic health of the country, stock market crashes, etc. But for the sake of the example let's assume none of these factors plays a role.
2. <a name="[2]"></a>To cite the [mathematician Ian Stewart](http://books.google.de/books?id=dUhMAQAAQBAJ&pg=PA182&lpg=PA182&dq=Classical+mathematics+concentrated+on+linear+equations+for+a+sound+pragmatic+reason:+it+could+not+solve+anything+else.&source=bl&ots=PuRT666z3D&sig=YBZtoUP_y0siL0RUXfC14keMGe4&hl=de&sa=X&ei=upteVPDfBIysPJChgZgE&ved=0CCsQ6AEwAQ#v=onepage&q=Classical%20mathematics%20concentrated%20on%20linear%20equations%20for%20a%20sound%20pragmatic%20reason%3A%20it%20could%20not%20solve%20anything%20else.&f=false): "Classical mathematics concentrated on linear equations for a sound pragmatic reason: it could not solve anything else."

<!--
3. <a name="[3]"></a>You might remember that in the post on [vector spaces](intuitivemi/2015/07/25/vector-spaces) we mentioned that *linear algebra* is the mathematical discipline taking care of moving or rotating vectors. It is not a coincidence that the term *linear* appears in the title of this field: every possible movement or rotation of objects can be formalized by exactly the same kind of linear functions that we have seen above! Only that they are defined on vectors not on numbers. 
4. <a name="[4]"></a> Indeed, finding a function for the image captioning problem is a very difficult task. Only recently, a [very complicated type of functions](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) has been found which shows promising performance at this task. These functions - called recurrent neural networks - are actually not that different from the linear functions we have just learned above, and we will hopefully cover them at a later point.
-->
