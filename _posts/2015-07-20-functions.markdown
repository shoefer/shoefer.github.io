---
layout: intuds_post
title:  "Functions as Data Translators"
date:   2015-07-20 15:00:00
categories: intuds
comments: true
intuds-weight: 4
---

If you have read the previous posts carefully you should now be familiar with high-dimensional data. In this last introductory article we are now going to look at what data scientists mean when they think about transforming data: they apply *functions*.

## Mathematical Functions

Mathematicians use the term function rather differently from the common sense definition. In everyday language we talk about the function of things in the sense "what is the purpose of the thing" or "how does this thing work". A function in mathematical sense is rather different. It can be best thought of as a translation from one type of data to another type. Let me give you two examples.

#### Stock price prediction function

Let us return to our simple example from the [introductory post](/intuds/2015/07/26/datascience-showoff.html). We want to assess the stock price of some company. For the sake of simplicity, we will only use information about the annual revenue of the company (in Euro) and try to predict the stock price (also in Euro). One way to describe a function is a table:

<table class="data-table">
<tr>
<th>Year (Euro)</th>
<th>Annual Revenue (Euro)</th>
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

Tabular functions are common, but have some drawbacks. The main drawback is, we cannot *interpolate*, that is we do not know how much the stock price was in between 2012 and 2013. But even worse, we do not know the value for 2016, so we cannot even predict anything! However, the example data I have given exhibits a regularity (surprise, surprise!), namely that the values in the right column are exactly 0.00013 times the annual revenue plus 70 (check this for yourself). This gives us a much more concise way of describing this function:
<div class="pseudoformula">
<b>Price</b> = 0.00013 * <b>Revenue</b> + 70
</div>
Let us visualize this function by plotting a graph which has on one axis the size and on the other the price:
{% include figure.html src="/intuds/images/2015-07-20-functions_sizeprice.png" width="65%" %}

We see something interesting here: when visualizing the relationship between revenue and stock price in our example, it turns out to be a line. The fact that such relationships / functions can be drawn by a line resulted in them being called *linear*. Linear functions  are amongst the most important types of relationships in mathematics - and actually they are one of the few that mathematics can really deal with [[2]](#[2]). Therefore, the majority of methods in machine learning are based on linear functions as the one given here. 
<!-- We will talk about them in more detail in the next article. -->

Still, there are a few more questions arising here. 
<ol>
<li>Can we find this regularity automatically from the data?</li>
<li>Who guarantees the regularity is actually true in the real world?</li>
</ol>
The answer to the first question is clearly yes. Finding regularities in data is the core discipline of statistics and machine learning.

Answering the second question is much harder. But to be honest *no one* can guarantee that! It could be that we use entirely wrong assumptions, e.g. that the company's revenue has nothing to do with the stock price. In fact, it is easy find [totally meaningless regularities](http://www.tylervigen.com/spurious-correlations) everywhere.
However, machine learning has come up with ways to say "well, I'm not sure, but I'm kind of confident that it is true". We will talk about that later in more extent.

#### Image classification function
Another more complicated function maps pictures to sequences of characters. It would get an image as input and should return a sequence of characters describing what is visible in the image. If we pass a picture of a cat to our function it should print out "cat", for a dog "dog" etc. 

The main difference to the stock price example is that image captioning problem is *multi-dimensional*: we are not mapping from one single number (size of apartment) to another single number (price), but from one *set of numbers* (an image, using an encoding as described in [this article](/intuds/2015/07/19/data-numbers-representations.html)) to another set (the sequence of characters). If you have read the previous article on [vector spaces](/intuds/2015/07/25/vector-spaces.html) you already now how this works: we consider the multi-dimensional data to be a vector in a high-dimensional space. In the same way we define functions on numbers, we can define functions on vectors - and these functions have numbers or again vectors (of the same or different dimensionality) as output [[3]](#[3]). Functions can map vectors to new vectors in the same space (for example, image transformed to new image) or into different spaces (image transformed to text) [[4]](#[4]). 

## Machine learning &cong; learning functions

What do these functions have to do with the everyday life of a researcher in machine learning and artificial intelligence? In fact, the main task of researchers in artificial intelligence and machine learning is to find the right functions for different problems, such as the ones mentioned above.
Instead of designing a function by hand, machine learning uses data to *learn the function* (or at least some part of it). 
And digging into some advanced ways of how to automatically learn the right functions is going to be the main topic of the forthcoming articles.

To sum up, we have learned that functions translate between data. Input and output data types of a function can be numbers or vectors, of same dimensionality (as in the stock price example: one to one) or of different dimensionality (image classification: many to one), living in the same space (stock price: Euro to Euro) or different spaces (image classification: image to object type). 

Now that you have learned about the powerful concept of functions let us look at why learning regularities is so hard.


### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Functions in the mathematical sense translate from one representation to another
- The simplest and best understood functions are linear functions
- Functions map between numbers, or more general vectors.
- Machine learning tries to learn functions from data

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Of course this is largely oversimplified. The actual price would also depend on the size of the company at the time, economic health of the country, stock market crashes, etc. But for the sake of the example let's assume none of these factors plays a role.
2. <a name="[2]"></a>To cite the [mathematician Ian Stewart](http://books.google.de/books?id=dUhMAQAAQBAJ&pg=PA182&lpg=PA182&dq=Classical+mathematics+concentrated+on+linear+equations+for+a+sound+pragmatic+reason:+it+could+not+solve+anything+else.&source=bl&ots=PuRT666z3D&sig=YBZtoUP_y0siL0RUXfC14keMGe4&hl=de&sa=X&ei=upteVPDfBIysPJChgZgE&ved=0CCsQ6AEwAQ#v=onepage&q=Classical%20mathematics%20concentrated%20on%20linear%20equations%20for%20a%20sound%20pragmatic%20reason%3A%20it%20could%20not%20solve%20anything%20else.&f=false): "Classical mathematics concentrated on linear equations for a sound pragmatic reason: it could not solve anything else."
3. <a name="[3]"></a>You might remember that in the post on [vector spaces](intuds/2015/07/25/vector-spaces) we mentioned that *linear algebra* is the mathematical discipline taking care of moving or rotating vectors. It is not a coincidence that the term *linear* appears in the title of this field: every possible movement or rotation of objects can be formalized by exactly the same kind of linear functions that we have seen above! Only that they are defined on vectors not on numbers. 
4. <a name="[4]"></a> Indeed, finding a function for the image captioning problem is a very difficult task. Only recently, a [very complicated type of functions](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) has been found which shows promising performance at this task. These functions - called recurrent neural networks - are actually not that different from the linear functions we have just learned above, and we will hopefully cover them at a later point.