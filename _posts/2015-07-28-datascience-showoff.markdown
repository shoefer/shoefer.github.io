---
layout: intuds_post
title:  "The Power of Machine Intelligence"
date:   2015-07-26 15:00:00
categories: intuds
comments: true
intuds-weight: 0
---

Thinking machines have revolutionalized our everyday life, maybe even more than industrialization or the invention of the car. But although everyone of has an intuition about how a car works thinking machines remain obscure and magical to most of us. 

I believe that everyone should have at least a "car intuition" about thinking machines. Unfortunately, common introductions to artificial intelligence and machine learning require quite some knowledge about programming and math and scare laymen off. Luckily, none of these skills is required to grasp the core ideas behind thinking machines. And these core ideas are what I would like to tell you about in the forthcoming series of articles in this *introduction to machine intelligence*.

To whet your appetite I would like to present four prototypical applications of machine intelligence. We will get back to these applications later and get a more detailed understanding of how machine intelligence approaches each of these problems.

## Image Understanding

For decades, researchers have been trying to make machines see the world we do. In 1966, one of the most famous artificial intelligence researchers, Marvin Minsky, hired an undergrad to solve the following problem as a summer project: connect a TV camera to a computer and make the computer describe what it sees. Now, 50 years later, we still haven't fully solved the problem, but at least we have made some progress. In the *image classification* task computers are now able to [outperform humans](https://gigaom.com/2015/02/13/microsoft-says-its-new-computer-vision-system-can-outperform-humans/) in certain regards. In this task, the computer has to decide for any given image what kind of object is depicted on that image. As manually programming the computer to do so has failed, machine intelligence tries to solve the problem by learning from data. 
To learn successfully huge amounts of *labeled data* (images together with descriptions of what object category is depicted on each image) are required which is why the community  created a [database of over 15 million images](http://www.image-net.org/) containing 21841 object types. By learning from these images, using a method called *deep neural networks*, machine intelligence is now able to predict the object category correctly in over 95% of all cases - which is above human performance. These neural networks will one of the topics covered later.

{% include figure.html src="/images/image-classification-msrdl1.jpg" width="300" id="image-understanding" link="true" caption="Top 5 predictions by an image classification approach. Credit: Microsoft Research" %}

Note however that the general problem of seeing machines hasn't been solved yet since the image classification task is limited to pictures where only one object is present. Describing entire scenes is much more complicated, but recently [progress has been made there](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), too.

## Algorithmic Trading: Stock Price Prediction

Machines are slowly taking over the stock markets using [algorithmic trading](https://en.wikipedia.org/wiki/Algorithmic_trading). One important thing these machine traders have to do is predicting stock prices. How would machine intelligence approach this problem? In fact, the task is very similar to the image classification problem, only that, instead of an object type, the computer should predict a continuous valued number: the stock price. But what data should the stock price predictor use for learning?
In the image classification task this was obvious: the image itself. Here, it is not clear what influences the stock price. It could be last months's revenue of the company, the size of the company, the stock price from last month, last year, and many more. 
A data scientist will approach this problem by collecting as many of these pieces of information, so-called *features*, and try to weigh the features in the best way to predict the stock price. We will look later in more detail how the computer can automatically weigh features to make predictions, and take a look at why the task of "weighing in the best way" is much more difficult then it sounds.

## Spam Classification

Everyone knows the problem of [spam](http://www.stevenburgess.net/wp-content/uploads/2014/12/Spam-Can.jpg). It tastes weird and, even worse, it fills your mailbox with juicy offers for [penis enlargement](http://www.mensjournal.com/health-fitness/health/the-hard-truth-about-penis-enlargement-20141027) or earning money from [fake Nigerian royalty](http://www.419eater.com/img/news.pdf). But thanks to machine intelligence, nowadays most spam automatically finds its way into your junk folder. This application of machine intelligence is called *spam classification* and - in its simplest form - works as follows: your mail program receives an email and extracts features (as in the example before) from the email, such as what words the email  contains, whether you know the author of the email, and many more. It then weighs each of these features and makes a binary decision: spam or no spam. 

We see a pattern emerging here. Spam classification is very similar to image classification and stock price prediction: data scientists collects many spam emails, extract features from these emails, and use fancy tools to find the best weighting of all the features. The main difference is that not a continuous number (stock price), or an object category, but a binary output (spam / no spam) is computed.

## Robot Skill Learning

The last and maybe most exciting application of machine intelligence is robotics. Interestingly, you can (to some extent) apply exactly the same techniques - as before - to make a robot do cool things. The following video shows how to teach a robot to play table tennis.

<div class="imgcenter">
<iframe width="280" height="155" src="https://www.youtube.com/embed/SH3bADiB7uQ" frameborder="0" allowfullscreen></iframe>
</div>

The type of learning slightly differs from the approaches seen before. Instead of telling the robot exactly what the right motion, the researchers let the robot try out motions on its own and give the robot a reward if it performs a good stroke, or a penalty if it performs bad (in fact, the robot doesn't get lollipops as rewards, but delicious large numbers). The robot will then repetitively generate motions, collect rewards/penalties and step by step correct its motions in order to get more reward and finally execute an excellent table tennis stroke. 

<!-- 
However, you can also formulate the problem In a nutshell, the researchers make something similar as in stock price prediction: from the position of the ball you try to "predict", or rather decide for, a motor command to send to the robot. Executing this motion will then allow the robot to hit the table tennis ball.
 -->

I hope I was able to get you excited about machine intelligence! In the next couple of posts I will try to convey the basic ideas of how to machine intelligence approaches all of these problems.

The next post will tell you in more detail why you don't need to understand complex math and programming to understand machine intelligence.
