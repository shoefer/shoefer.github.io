---
layout: intuds_post
title:  "Functions as Data Translators"
date:   2015-07-20 15:00:00
categories: intuds
comments: true
---

In the last article we have come up with a definition of data: Data is numbers + the knowledge what these numbers mean + an instruction of how to convert between the numbers and the actual thing that the numbers represent. But we have also said that we want to do something with data. This is where functions come into play.

## Mathematical Functions

Mathematicians use the term function rather differently from the common sense definition. In everyday language we talk about the function of things in the sense "what is the purpose of the thing" or "how does this thing work". A function in mathematical sense is rather different. It can be best thought of as a translation from one type of data to another type. Let me give you some examples.

### Mathematical Functions
A very simple example is a function which helps us assess the price of apartments in Berlin. It translates the size of an apartment (in square meters) into its price. 

Another more complicated function map pictures to sequences of characters. It would get an image as input and should return a sequence of characters describing what is visible in the image. If we pass a picture of a cat to our function it should print out "cat", for a dog "dog" etc. 

Indeed, finding such a function is a very difficult task. Only recently, a [very complicated type of functions]{http://karpathy.github.io/2015/05/21/rnn-effectiveness/} has been found which shows promising performance at this task.

 Before we can understand these very complex functions, we shuold first look at some simpler functions.

, trying to find appropriate functions for a diverse set of problems has been the main problem researchers on artificial intelligence and machine learning have been bothering with over the past decades. And describing some advanced ways of how to find good functions is going to be the topic of the forthcoming articles.

To sum up, we have learnt that functions translate between data. Input and output data types of a function can be different, but they can also be the same (for example, think of a sepia effect applied to a picture which turns your original picture into one that looks like from a weird dream). We can generalize the concept of functions even more: Since we know that data is numbers, we can say that functions translate between numbers. This gives us much more flexibility and we will jump between the two views of functions as data-translators or as number-translators depending on which view fits better to our problem.

The main task of computer scientists is to find good functions for different problems, such as mapping picture to object names (object recognition), videos to face positions (face tracking), large texts to topics (natural language processing) and so on and so forth. I did not tell you the whole truth, though. People from machine learning approach the problem a bit differently. Instead of designing the function in its entirety by themselves, they use data to learn the function. That sounds paradox at first, but it really works! Before we come to this question, however, we will need to think a bit more about how functions actually look like and what we can do with them. This will be the topic of the next article.

*You could for example design the function such that it goes from top to bottom and from left to right when naming. Your you sort the things you see alphabetically, etc.


### TLDR:
- Formulas are good for condensing and bullet-proofing concepts and methods, but less often for understanding
- Most people conceptualize complex things in analogies, relating them to perception (e.g. vision) and language
- Formulas scare people

### <a name="further"></a>Further reading and thinking:
1. [Euler's formula on Wikipedia](http://en.wikipedia.org/wiki/Euler's_formula)
2. [Where Mathematics Comes From](https://en.wikipedia.org/wiki/Where_Mathematics_Comes_From) by Lakoff and Nunez
