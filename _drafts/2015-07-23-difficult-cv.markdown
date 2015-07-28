---
layout: intuds_post
title:  "On the Difficulty of Computer Vision"
date:   2015-07-23 15:07:27
categories: intuds
comments: true
intuds-weight: 100
---

Let's look at picture example again:
{% capture numbersFullUrl %}/intuds/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}

It's a picture of [myself](/intuds/images/2015-07-19-data-numbers-representations_picture.png) of course! It's hard to see and if you don't you could try to watch [The Matrix](https://en.wikipedia.org/wiki/The_Matrix) at least 10 more. Anyway, the trick is that I have taken [this grey scale picture](/intuds/images/2015-07-19-data-numbers-representations_picture.png)

Why is it so hard for you to recognize me in this table of numbers, whereas it isn't when looking at the picture? To put it very crudely, your brain takes care of transforming the grey scale values in the picture into something equivalent to numbers (namely firing rates of the cells on the retina in your eye), routes these numbers to a special part of your brain called the *visual cortex* which then takes care of recognizing my face. The problem is that we do not know exactly how the visual cortex processes these data,  [[2]](#visualcortex) and so the computer has to recognize me in the table of numbers, which is apparently much harder than just using your powerful human hardware, your visual cortex!


2. <a name="visualcortex"></a>In fact, we already know many things about the structure of the visual cortex, and what the first processing steps look like. This information has already been used in computer vision extensively, and has also inspired how neural networks for image processing are built. 
