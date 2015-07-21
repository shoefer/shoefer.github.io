---
layout: intuds_post
title:  "Functions as Data Translators"
date:   2015-07-20 15:00:00
categories: intuds
comments: true
---

In the last article we have come up with a definition of data: Data is numbers + the knowledge what these numbers mean + an instruction of how to convert between the numbers and the actual thing that the numbers represent. But we have also said that we want to do something with data. This is where functions come into play.

## Mathematical Functions

Mathematicians use the term function rather differently from the common sense definition. In everyday language we talk about the function of things in the sense "what is the purpose of the thing" or "how does this thing work". A function in mathematical sense is rather different. It can be best thought of as a translation from one type of data to another type. Let me give you two examples.

#### Apartment price prediction function

A very simple example is a function which helps us assess the price of apartments in Berlin. It translates the size of an apartment (data given in square meters) into its price (given in Euro). One way to describe a function is a table:

<table class="data-table">
<tr>
<th>Size (m<sup>2</sup>)</th>
<th>Price (Euro)</th>
</tr>
<tr>
<td>40</td>
<td>590</td>
</tr>
<tr>
<td>50</td>
<td>720</td>
</tr>
<tr>
<td>60</td>
<td>850</td>
</tr>
<tr>
<td>80</td>
<td>1110</td>
</tr>
<tr>
<td>100</td>
<td>1370</td>
</tr>
</table>

Using this function we can now assess how much an apartment with a certain size would cost [[1]](#[1]).

Tabular functions are common, but have some drawbacks. For example, we cannot *interpolate*, that is we do not know how much an apartment with e.g. 55 m<sup>2</sup> costs because it does not appear in the table. However, the example data I have given exhibits a regularity (surprise, surprise!), namely that the values in the right column are exactly 13 times the value in the left column plus 70 (check this for yourself). In fact, this is equivalent to saying that an apartment costs has a basic price of 70 Euros to which we have to add the price per square meter which is 13 Euros. More importantly, it gives us a much more concise way of describing this function:
<div class="pseudoformula">
<b>Price</b> = 13 * <b>Size</b> + 70
</div>
Let us visualize this function by plotting a graph which has on one axis the size and on the other the price:
{% include figure.html src="/intuds/images/2015-07-20-functions_sizeprice.png" width="65%" %}

We see something interesting here: when visualizing the relationship between price and size in our example, it turns out to be a line. In fact, such relationships / functions are called *linear* and are one of the most important type of relationship in mathematics - and actually they are one of the few mathematics can actually really deal with [[2]](#[2]). The majority of methods in machine learning are based on linear functions as the one given here. We will talk about them in more detail in the next article.

#### Image captioning function
Another more complicated function map pictures to sequences of characters. It would get an image as input and should return a sequence of characters describing what is visible in the image. If we pass a picture of a cat to our function it should print out "cat", for a dog "dog" etc. 

The main difference to the apartment price example is that image captioning problem is *multi-dimensional*: we are not mapping from one single number (size of apartment) to another single number (price), but from one *set of numbers* (an image, using an encoding as described in [the previous article](intuds/2015/07/19/data-numbers-representations)) to another set (the sequence of characters). The next article will explain how we can extend our understanding of linear functions to such multi-dimensional problems.

Indeed, finding a function for the image captioning problem is a very difficult task. Only recently, a [very complicated type of functions](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) has been found which shows promising performance at this task. These functions - called recurrent neural networks - are actually not that different from the linear functions we have just learned above, and we will hopefully cover them at a later point.

## Machine learning &cong; learning functions

What do these functions have to do with the everyday life of a researcher in machine learning and artificial intelligence? In fact, the main task of researchers in artificial intelligence and machine learning is to find the right functions for different problems, such as the ones mentioned above.
But, instead of designing a function by hand, machine learning uses data to *learn the function* (or at least some part of it). That might sound paradox at first, but it really works! 
And digging into some advanced ways of how to automatically learn the right functions is going to be the main topic of the forthcoming articles.

To sum up, we have learned that functions translate between data. Input and output data types of a function can be different, but they can also be the same. We can generalize the concept of functions even more: Since we know that data is encoded numbers, we can say that functions translate between numbers. In the next article, we are going to talk about *vector spaces* which allow us to understand how a function can map between sets of numbers.


### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Functions in the mathematical sense translate from one representation to another
- The simplest and best understood functions are linear functions
- Machine learning tries to learn functions from data

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Of course this is largely oversimplified. The actual price would also depend on whether it is close to the city center or in the suburb, whether it is a new apartment or a shabby one, etc. But for the sake of the example let's assume none of these factors plays a role.
2. <a name="[2]"></a>To cite the [mathematician Ian Stewart](http://books.google.de/books?id=dUhMAQAAQBAJ&pg=PA182&lpg=PA182&dq=Classical+mathematics+concentrated+on+linear+equations+for+a+sound+pragmatic+reason:+it+could+not+solve+anything+else.&source=bl&ots=PuRT666z3D&sig=YBZtoUP_y0siL0RUXfC14keMGe4&hl=de&sa=X&ei=upteVPDfBIysPJChgZgE&ved=0CCsQ6AEwAQ#v=onepage&q=Classical%20mathematics%20concentrated%20on%20linear%20equations%20for%20a%20sound%20pragmatic%20reason%3A%20it%20could%20not%20solve%20anything%20else.&f=false): "Classical mathematics concentrated on linear equations for a sound pragmatic reason: it could not solve anything else."
