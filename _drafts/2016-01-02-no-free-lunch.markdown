---
layout: intuitivemi_post
title:  "The Curse of No Free Lunch"
date:   2016-1-2 15:00:00
categories: intuitivemi
comments: true
intuitivemi-weight: 9
intuitivemi-category: Learning from Data
---

In case the title whetted your appetite, I suggest to get lunch break before starting to read this article; the reason is that I'll have to inform you that there is no such thing as free lunch -- not even in machine learning!

In machine learning, though, being for free or not does not have anything to do with money but with <i>prior assumptions</i>.
The following post will explain why any learner (including non-artificial learners!) needs to make suitable prior assumptions to be able to learn something. This is because learning requires the ability to generalize from a limited amount of training samples; and is thus clearly distinct from pure memorization. But in order to generalize from few samples to new ones we must make suitable prior assumptions about <i>how to generalize</i>.

The importance of this insight extends well beyond machine learning as it touches upon such as long-running debates like the one about  [nature vs. nurture](https://en.wikipedia.org/wiki/Nature_versus_nurture). But we'll come to that at the end of the post. So bon appétit and let's get started!

### Inductive bias 

Let us begin by

Ok, so with every dimension we add we get an exponential increase in the number of parameters to consider. But is that really a practical issue?

Unfortunately, yes. To see that, let us return to the problem of understanding (images by assigning them into different categories)(intuitivemi/2015/07/25/vector-spaces.html). I have told you previously that this image

{% capture numbersFullUrl %}/intuitivemi/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}

lives in a 945-dimensional [vector space](intuitivemi/2015/07/25/vector-spaces.html). In fact our eye has a much higher resolution and that there are even much more than 10<sup>945</sup> images possible.

What does this mean? From our little calculation follows *entire mankind* will only see a tiny fraction of all theoretically possible images. This means that representing an image by 27x35 pixels with gray scale values is highly *redundant*. To make an analogy, imagine telephone numbers would have 945 digits instead of 9 (that is the length of an average phone number in [Berlin](http://www.berlin.de)). We would never even come close to using all the possible telephone numbers, even if every particle in the universe would get its own phone.

So images are not really efficiently represented, but why is that a problem for machine intelligence?
