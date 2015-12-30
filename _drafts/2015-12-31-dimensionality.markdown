---
layout: intuds_post
title:  "The Curse of Dimensionality"
date:   2015-12-31 15:00:00
categories: intuds
comments: true
intuds-weight: 8
intuds-category: Learning from Data
---

In the last post we have looked at one of the big problems of data science: when we want to learn [functions](/intuds/2015/07/20/functions.html) from data, we have to fight [overfitting](/intuds/2015/08/07/overfitting.html). In this post we will look at another archenemy of learning: dimensionality.

To do so, let us return to the problem of understanding (images by assigning them into different categories)(intuds/2015/07/25/vector-spaces.html). I have told you previously that this image

{% capture numbersFullUrl %}/intuds/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}

lives in a 945-dimensional [vector space](intuds/2015/07/25/vector-spaces.html). The question is now: how many possible gray scale pictures exist? The math is not so complicated [[1]](#[1]) but I can tell you that by making some reasonable assumptions we see that there are more than 10<sup>945</sup> possible gray scale images with 27x35 pixels - 10<sup>945</sup> is a number consisting of a 1 with 945 trailing zeros, and it is several orders of magnitudes higher than the [number of particles in the entire universe](http://www.quora.com/How-many-particles-are-there-in-the-universe)! In fact our eye has a much higher resolution and that there are even much more than 10<sup>945</sup> images possible.

What does this mean? From our little calculation follows *entire mankind* will only see a tiny fraction of all theoretically possible images. This means that representing an image by 27x35 pixels with gray scale values is highly *redundant*. To make an analogy, imagine telephone numbers would have 945 digits instead of 9 (that is length of an average phone number in [Berlin](http://www.berlin.de)). We would never even come close to using all the possible telephone numbers, even if every particle in the universe would get its own phone.

So images are not really efficiently represented, but why is that a problem for machine intelligence?

### Hughes effect

The problem manifests itself in two ways. The first one can be best explained considering the [image classification problem](/intuds/2015/07/25/vector-spaces.html) of categorizing whether an image is a picture of me, Sebastian, or of a blowfish.

*With every dimension we add to the data, we add one more possibilities to separate the data*. What is the right split then?

http://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/

http://www.edupristine.com/blog/curse-dimensionality

### Curse of dimensionality




### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- 

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Let us assume that a pixel can take a finite number of values. We assume that only 1 digits after the decimal point are allowed. So we have the numbers 0, 0.1, 0.2, ... 0.9, 1.0, which are 10 in total. We have 945 pixels, this makes 10<sup>945</sup> possible images. 

