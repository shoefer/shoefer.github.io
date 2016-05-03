---
layout: intuitivemi_post
title:  "Understanding Machine Intelligence without Formal Math"
date:   2015-07-19 15:00:00
categories: intuitivemi
comments: true
intuitivemi-weight: 1
intuitivemi-category: Basics
---

In this post I want to defend the basic idea of this series of articles, namely why I am trying to avoid mathematical formalism for explaining data science.

If you don't care about math anyway, you can skip this post and start reading about [data](/intuitivemi/2015/07/19/data-numbers-representations.html).

I do not have anything against formulas. Quite the contrary: mathematical formalisms are a fantastic way to condense and sort out the necessary ingredients of a method. Without formalism, we could not program a computer to operationalize any method. Think of a formula as a packing list for your camping trip. It has to be complete and all the things you need have to be on it, and you only on site you might realize if you did something wrong ("Oh no, I forgot to bring my [hiking heels](http://consumerist.com/2010/11/29/go-hiking-in-style-with-these-teva-high-heels/)"). In a similar way a formula has to contain everything required to describe your mathematical concept or method, and only when applying it / executing your method you realize whether something in your mathematical description is wrong or missing.

However, I find formulas a very bad way to understand things. I see three main reasons for that. 

The first reason is that after studying and working in academia for a couple of years, I realized that the magic "ahhh, THAT'S how it works!" moments while trying to grasp a complex method always happened when I could find analogies in "bodily" or linguistic terms: while rotating three-dimensional structures in my head, while visualizing probabilities as a contour (like a mountainous landscape), while breaking down complex relationships to sets of causal if-then statements, and so on. Maybe not everybody thinks of mathematics like this. It is possible that some mathematical geniuses think differently when reasoning about math. But the vast majority of researchers and students that I have met so far strive for analogies in order to explain or grasp complex mathematical concepts. I think there is a lot of empirical evidence for that, for example that scientific papers plot graphs, bar charts and the like in order to visualize results instead of just printing some numbers. Two famous cognitive scientists even have made an endeavor to argue that the holy grail of mathematics, Euler's formula, can be derived only from the way we perceive the world (in contrast to a Platonic view of universal mathematical truths) [[1,2]](#further).

The second reason is that formulas often do not reflect the way how people figured out the concept or method underlying the formula [[3]](#further). It is like not telling the whole story but just the end of it. You will have a hard time reconstructing the rest of the story from that little information. I think it is similar for formulas, although it is in principle possible since they condense the whole method; but you will still have a hard time figuring out its meaning without some context.

The third reason is much simpler: Formulas scare many people. I believe one reason for this lies in the condensed nature of formulas that I have mentioned before. Formulas use a very precise and non-redundant language, which is far less verbose than natural language. Therefore, you can spend an entire day by looking at one formula without getting it. I believe this being the reason for some people thinking that they are not good at math, although they probably could be. They get disappointed too quickly because they cannot grasp the formula within an eyelash. Relax guys, that holds true for most of us.

So let us now jump right into the topic and talk a bit about *data*!

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Formulas are good for condensing and bullet-proofing concepts and methods, but less often for understanding
- Most people conceptualize complex things in analogies, relating them to perception (e.g. vision) and language
- Formulas scare people

### <a name="further"></a>Further reading and thinking:
1. [Euler's formula on Wikipedia](http://en.wikipedia.org/wiki/Euler's_formula)
2. [Where Mathematics Comes From](https://en.wikipedia.org/wiki/Where_Mathematics_Comes_From) by Lakoff and Nunez
3. Of course, this might not be true for everybody. A colleague of mine argued that real understanding only happens if you understand both, the high-level concept or analogy, and the mathematical formula. I agree that to get a full understanding you need to care about the details -- but to get a rough idea of how and why something works, I will argue that the mathematical details are not required.
4. [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) takes a similar stance as this blog and features cool visualizations of data and machine learning algorithms, as well as brief technical descriptions.
