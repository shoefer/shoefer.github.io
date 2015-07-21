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

A very simple example is a function which helps us assess the price of apartments in Berlin. It translates the size of an apartment (in square meters) into its price. One way to describe a function is a table:

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

The problem with this kind a tabular function is that we cannot *interpolate*, that is we do not know how much an apartment with e.g. 55 m<sup>2</sup> costs because it does not appear in the table. Interestingly, the example data I have given exhibits one regularity, namely that the values in the right column are exactly 13 times the value in the left column plus 70 (check this for yourself). In fact, this is equivalent to saying that an apartment costs at least 70 Euros to which we add the price per square meter which is 13 Euros. More importantly, it gives us a much more concise way of describing this function:
<div class="pseudoformula">
<b>Price</b> = 13 * <b>Size</b> + 70
</div>
Let us visualize this function by plotting a graph which has on one axis the size and on the other the price:


#### Image captioning function
Another more complicated function map pictures to sequences of characters. It would get an image as input and should return a sequence of characters describing what is visible in the image. If we pass a picture of a cat to our function it should print out "cat", for a dog "dog" etc. 

Indeed, finding such a function is a very difficult task. Only recently, a [very complicated type of functions](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) has been found which shows promising performance at this task. These functions - called recurrent neural networks - are actually not that that different from the linear functions we have just learned above, but we will cover them at a later point.

## Machine learning &cong; learning functions

What do these functions have to do with the everyday life of a researcher in machine learning and artificial intelligence? In fact, the main task of researchers in artificial intelligence is to find good functions for different problems, such as mapping picture to object names (object recognition), videos to face positions (face tracking), large texts to topics (natural language processing) and so on and so forth.
And digging into some advanced ways of how to find good functions automatically is going to be the topic of the forthcoming articles.

To sum up, we have learnt that functions translate between data. Input and output data types of a function can be different, but they can also be the same. We can generalize the concept of functions even more: Since we know that data is numbers, we can say that functions translate between numbers. This gives us much more flexibility and we will jump between the two views of functions as data-translators or as number-translators depending on which view fits better to our problem.

Instead of designing the function in its entirety by themselves, they use data to learn the function. That sounds paradox at first, but it really works! Before we come to this question, however, we will need to think a bit more about how functions actually look like and what we can do with them. This will be the topic of the next article.

In fact, the main task of computer scientists is to find good functions for different problems, such as mapping picture to object names (object recognition), videos to face positions (face tracking), large texts to topics (natural language processing) and so on and so forth. I did not tell you the whole truth, though. People from machine learning approach the problem a bit differently. Instead of designing the function in its entirety by themselves, they use data to learn the function. That sounds paradox at first, but it really works! Before we come to this question, however, we will need to think a bit more about how functions actually look like and what we can do with them. This will be the topic of the next article.


### TLDR:
- Functions in the mathematical sense translate from one representation to another
- The simplest and best understood functions are linear functions
- Machine learning tries to learn functions from data

### <a name="further"></a>Further reading and thinking:
1. 
