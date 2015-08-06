---
layout: intuds_post
title:  "Functions as Data Translators"
date:   2015-07-20 15:00:00
categories: intuds
comments: true
intuds-weight: 4
---

If you have read the previous posts carefully you should now be familiar with high-dimensional data. In this last introductory article we are now going to look at what data scientists mean when they think about manipulating data: they apply *functions*.

## Mathematical Functions

Mathematicians use the term function rather differently from the common sense definition. In everyday language we talk about the function of things in the sense "what is the purpose of the thing" or "how does this thing work". A function in mathematical sense is rather different. It can be best thought of as a translation from one type of data to another type. Let me give you two examples.

#### Stock price prediction function

Let us return to our simple example from the [introductory post](/intuds/2015/07/26/datascience-showoff.html). We want to assess the stock price of some company. For the sake of simplicity, we will only use information about the annual revenue of the company (in Euro) and try to predict the stock price (also in Euro). We can describe this relationship in a big table:

<table class="data-table">
<tr>
<th>Year</th>
<th>Annual Revenue in January (Euro)</th>
<th>Price (Euro)</th>
</tr>
<tr>
<td>2010</td>
<td>40.000</td>
<td>590</td>
</tr>
<tr>
<td>2011</td>
<td>50.000</td>
<td>720</td>
</tr>
<tr>
<td>2012</td>
<td>60.000</td>
<td>850</td>
</tr>
<tr>
<td>2013</td>
<td>80.000</td>
<td>1110</td>
</tr>
<tr>
<td>2014</td>
<td>100.000</td>
<td>1370</td>
</tr>
</table>

This table can be considered a function, as for a annual revenue it gives you a stock price value.
Such tabular functions are common but they have a severe drawback: we cannot *extrapolate* - from this table alone we do not know how to predict the value for 2015 or 2016! However, the example data I have given exhibits a regularity (surprise, surprise!), namely that the stock price values in the right column are exactly 0.00013 times the annual revenue plus 70 (check this for yourself). This gives us a much more concise way of describing this function:

<div class="pseudoformula">
<b>Price</b> = 0.00013 * <b>Revenue</b> + 70
</div>

Let us visualize this function by plotting a graph which has on one axis the size and on the other the price:
{% include figure.html src="/intuds/images/2015-07-20-functions_sizeprice.png" width="65%" %}

We see two interesting things here: first, we can now predict the stock price value from the annual revenue, no matter which revenue (or year). Secondly, when the relationship between revenue and stock price in our example turns out to be a line. The fact that such relationships / functions can be drawn by a line results in them being called *linear functions*. Linear functions  are amongst the most important types of relationships in mathematics - and actually they are one of the few that mathematics can really deal with [[2]](#[2]). Therefore, the majority of methods in machine learning are based on linear functions as the one given here. 
<!-- We will talk about them in more detail in the next article. -->

Still, there are a few more questions arising here. 
<ol>
<li>Can we find this regularity automatically from the data?</li>
<li>Who guarantees the regularity is actually true in the real world?</li>
</ol>
The answer to the first question is clearly yes. Finding regularities in data is the core discipline of data science, in particular statistical machine learning, and we will talk about this later.
<!-- Methods that find regularities by fitting lines (or other shapes) into data are called *regression* methods. -->

Answering the second question is much harder. But to be honest *no one* can guarantee that! It could be that we use entirely wrong assumptions, e.g. that the company's revenue has nothing to do with the stock price. In fact, it is easy find [totally meaningless regularities](http://www.tylervigen.com/spurious-correlations) everywhere. Neither is it clear that the relationship should be a line at all - maybe it should rather have the form of a delicious [Currywurst](https://en.wikipedia.org/wiki/Currywurst#/media/File:Currywurst_%26_Pommes_frites.jpg). 
However, machine learning has come up with ways to say "well, I'm not sure, but I'm kind of confident that this function is the right one". We will talk about that later in more extent, too.

#### Image classification function
Another more complicated function we have considered before is mapping pictures to object categories. In the [previous post](/intuds/2015/07/25/vector-spaces.html) we have seen that we can draw (hyper)planes to separate two categories of objects, namely blowfish and Sebastians:
{% include figure.html src="/intuds/images/2015-07-21-vector_spaces-arrow-plane.png" width="300" gifplayer="true" id="vector-spaces-arrow-plane" %}
The trick we did for finding this visualization was shrinking the 27x35 images to a 3x1 image which allowed us to treat images as points (vectors) in 3D space.
What does this look like if we shrink the images even further, namely to a 2x1 image? We can then visualize the images as vectors in 2D. Similar as before we can now ask how to separate the shrinked Sebastians and blowfish. The answer is that we have to find a "2D hyperplane" - which turns out to be just a line!
{% include figure.html src="/intuds/images/2015-07-20-functions_image_class_2d.png"  width="65%" id="2015-07-20-functions_image_class_2d" %}
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

By now it should be clear how these linear functions translate into higher-dimensional spaces: the plane is a generalization of the line to 3D, and the hyperplane a generalization of the line/plane to higher dimensions! So in the future if we think about discriminating hyperplanes, we will usually visualize this as a line or a plane separating two sets of 2D or 3D points. And as before the mathematical field of [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) describes how to deal with these lines, planes and hyperplanes. 

<!-- The main difference to the stock price example is that the image classification problem is *multi-dimensional*: we are not mapping from one single number (size of apartment) to another single number (price), but from one *set of numbers* (an image, using an encoding as described in [this article](/intuds/2015/07/19/data-numbers-representations.html)) to another set (the sequence of characters). If you have read the previous article on [vector spaces](/intuds/2015/07/25/vector-spaces.html) you already now how this works: we consider the multi-dimensional data to be a vector in a high-dimensional space. In the same way we define functions on numbers, we can define functions on vectors - and these functions have numbers or again vectors (of the same or different dimensionality) as output [[3]](#[3]). Functions can map vectors to new vectors in the same space (for example, image transformed to new image) or into different spaces (image transformed to text) [[4]](#[4]).  -->

## Machine learning &cong; learning functions

We have now learned what most data scientists are basically doing all day long: trying to learn functions from data. We have seen two types of functions learning problems: 
<ol>
<li>Predicting a continuous value by fitting a line (or any other type of shape) into data; data scientists call methods to fit functions to data <i>regression</i> methods</li>
<li>Finding a function which separates different subparts of data in order to discriminate between them; data scientists call them <i>classification</i> methods. </li>
</ol>
There are some more types of functions and ways to learn them, but by understanding regression and classification from we have got the basic idea of the biggest field of machine learning, [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning). The name *supervised* comes from the fact that the data needs to be *labeled*: for every data sample, we need to know the value of the prediction target. In the stock price example we needed to know the stock price for each annual revenue, and in the image classification example we needed to know the category (Sebastian vs. blowfish) depicted on each picture.
And digging into some advanced ways of how to automatically learn the right functions is going to be the main topic of the forthcoming articles.

<!--To sum up, we have learned that functions translate between data. Input and output data types of a function can be numbers or vectors, of same dimensionality (as in the stock price example: one to one) or of different dimensionality (image classification: many to one), living in the same space (stock price: Euro to Euro) or different spaces (image classification: image to object type). 
-->

Having understood the powerful concept of functions, we will take a look at why it is actually so hard to learn them in the next posts.

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Functions in the mathematical sense translate from one representation to another
- The simplest and best understood functions are linear functions
- Functions map between numbers, or more general vectors.
- Machine learning tries to learn functions from data
- Regression maps onto continuous numbers, classification onto categories

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Of course this is largely oversimplified. The actual price would also depend on the size of the company at the time, economic health of the country, stock market crashes, etc. But for the sake of the example let's assume none of these factors plays a role.
2. <a name="[2]"></a>To cite the [mathematician Ian Stewart](http://books.google.de/books?id=dUhMAQAAQBAJ&pg=PA182&lpg=PA182&dq=Classical+mathematics+concentrated+on+linear+equations+for+a+sound+pragmatic+reason:+it+could+not+solve+anything+else.&source=bl&ots=PuRT666z3D&sig=YBZtoUP_y0siL0RUXfC14keMGe4&hl=de&sa=X&ei=upteVPDfBIysPJChgZgE&ved=0CCsQ6AEwAQ#v=onepage&q=Classical%20mathematics%20concentrated%20on%20linear%20equations%20for%20a%20sound%20pragmatic%20reason%3A%20it%20could%20not%20solve%20anything%20else.&f=false): "Classical mathematics concentrated on linear equations for a sound pragmatic reason: it could not solve anything else."

<!--
3. <a name="[3]"></a>You might remember that in the post on [vector spaces](intuds/2015/07/25/vector-spaces) we mentioned that *linear algebra* is the mathematical discipline taking care of moving or rotating vectors. It is not a coincidence that the term *linear* appears in the title of this field: every possible movement or rotation of objects can be formalized by exactly the same kind of linear functions that we have seen above! Only that they are defined on vectors not on numbers. 
4. <a name="[4]"></a> Indeed, finding a function for the image captioning problem is a very difficult task. Only recently, a [very complicated type of functions](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) has been found which shows promising performance at this task. These functions - called recurrent neural networks - are actually not that different from the linear functions we have just learned above, and we will hopefully cover them at a later point.
-->
