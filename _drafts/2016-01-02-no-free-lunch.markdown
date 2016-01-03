---
layout: intuitivemi_post
title:  "The Curse of No Free Lunch"
date:   2016-1-2 15:00:00
categories: intuitivemi
comments: true
intuitivemi-weight: 9
intuitivemi-category: Learning from Data
---

Proce

The no free lunch problem

-> nature vs. nurture
-> the blank slate


### More data?

Ok, so with every dimension we add we get an exponential increase in the number of parameters to consider. But is that really a practical issue?

Unfortunately, yes. To see that, let us return to the problem of understanding (images by assigning them into different categories)(intuitivemi/2015/07/25/vector-spaces.html). I have told you previously that this image

{% capture numbersFullUrl %}/intuitivemi/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}

lives in a 945-dimensional [vector space](intuitivemi/2015/07/25/vector-spaces.html). The question is now: how many possible gray scale pictures exist? The math is not so complicated [[1]](#[1]) but I can tell you that by making some reasonable assumptions we see that there are more than 10<sup>945</sup> possible gray scale images with 27x35 pixels - 10<sup>945</sup> is a number consisting of a 1 with 945 trailing zeros, and it is several orders of magnitudes higher than the [number of particles in the entire universe](http://www.quora.com/How-many-particles-are-there-in-the-universe)! In fact our eye has a much higher resolution and that there are even much more than 10<sup>945</sup> images possible.

What does this mean? From our little calculation follows *entire mankind* will only see a tiny fraction of all theoretically possible images. This means that representing an image by 27x35 pixels with gray scale values is highly *redundant*. To make an analogy, imagine telephone numbers would have 945 digits instead of 9 (that is length of an average phone number in [Berlin](http://www.berlin.de)). We would never even come close to using all the possible telephone numbers, even if every particle in the universe would get its own phone.

So images are not really efficiently represented, but why is that a problem for machine intelligence?