---
layout: intuds_post
title:  "The Power of Data Science"
date:   2015-07-26 15:00:00
categories: intuds
comments: true
intuds-weight: 0
---

Thinking machines have already changed and will slowly revolutionalize our everyday life, maybe even more than industrialization and the invention of the car. However, everyone of us knows has an intuition about how a car works whereas thinking machines remain obscure and magical to most of us. But I believe that everyone should have at least a "car intuition" about thinking machines. Unfortunately, common introductions to artificial intelligence and machine learning require quite some knowledge about programming and math and scare laymen off. But any of these skills is required to grasp the core ideas behind thinking machines. And these core ideas are what I would like to tell you about in the forthcoming series of articles in this *introduction to data science*.

To whet your appetite I would like to present four prototypical applications of data science. We will get back to these applications later and get a more detailed understanding of how data science approaches each of these problems.

## Algorithmic Trading: Stock Price Prediction

Machines are slowly taking over the stock markets using [algorithmic trading](https://en.wikipedia.org/wiki/Algorithmic_trading). One important thing these machine traders have to do is predicting stock prices. How would data science approach this thing? The simplest idea would be to apply a technique called *regression*: first, you collect information, also called *features*, about the stock you would like to predict, for example last months's revenue of the company, the size of the company at the time, the stock price from last month, etc. Then you weigh each of the features in such a way that today's stock price (which you know) comes out. Then you cross your fingers and hope that you will be able to plug-in the same features, but with today's value, and that you will able to predict next month's stock price. 

Doesn't sound so complicated, does it? 
We will look later in more detail how to weigh the features to make predictions, and take a look at why this naive approach actually does not really work in practice, too.

## Spam Classification

Everyone knows the problem of [spam](http://www.stevenburgess.net/wp-content/uploads/2014/12/Spam-Can.jpg). It tastes weird and, even worse, it fills your mailbox with juicy offers for [penis enlargement](http://www.mensjournal.com/health-fitness/health/the-hard-truth-about-penis-enlargement-20141027) or earning money from [fake Nigerian royalty](http://www.419eater.com/img/news.pdf). But thanks to data science, nowadays most spam automatically finds its way into your junk folder. This application of data science is called *spam classification* and - in its simplest form - works as follows: your mail program receives an email and extracts features (as in the example before) from the email, such as what words the email  contains, whether you know the author of the email, and many more. It then weighs each of these features and makes a binary decision: spam or no spam. 

The approach to make this decision is a similar to the stock price example: data scientists collects many spam emails, and use their fancy tools to find the best weighting of all the features. The main difference is that not a continuous number (stock price), but a binary output (spam / no spam) is computed.

## Image Understanding

For decades researchers are trying to make machines see the world we do. In 1966, one of the most famous artificial intelligence researchers, Marvin Minsky, hired an undergrad to solve the following problem as a summer project: connect a TV camera to a computer and make the computer describe what it sees. Now, 50 years later, we still haven't fully solved the problem, but at least we have made some progress. In the *image classification* task computers are now able to [outperform humans](https://gigaom.com/2015/02/13/microsoft-says-its-new-computer-vision-system-can-outperform-humans/) in certain regards. In this problem, the computer gets one of [15 million images](http://www.image-net.org/) for learning, and it can then make a decision about which object it sees on any image. It is similar to spam classification, only that the input data for the machine is different, and that the decision is not binary, but the machine has to decide between 21841 object types. 

{% include figure.html src="/images/image-classification-msrdl1.jpg" width="300" id="image-understanding" link="true" caption="Top 5 predictions by an image classification approach. Credit: Microsoft Research" %}

Note that image classification is limited to pictures where only one object is present. Describing entire scenes is much more complicated, but recently [progress has been made there](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), too.

## Robot Skill Learning

The last and maybe most exciting application of data science is robotics. Interestingly, you can (to some extent) apply exactly the same techniques - regression and classification - to make a robot do cool things. The following video shows how to teach a robot to play table tennis.

<div class="imgcenter">
<iframe width="280" height="155" src="https://www.youtube.com/embed/SH3bADiB7uQ" frameborder="0" allowfullscreen></iframe>
</div>

In a nutshell, the researchers make something similar as in stock price prediction: from the position of the ball you try to "predict", or rather decide for, a motor command to send to the robot. Executing this motion will then allow the robot to hit the table tennis ball.

I hope I was able to get you excited about data science! In the next couple of posts I will try to convey the basic ideas how to data science approaches all of these problems.

In the next post will tell you in more detail why you don't need to understand complex math and programming to understand data science.