---
layout: intuds_post
title:  "The Real Dimensionality of Data"
date:   2015-07-25 15:00:00
categories: intuds
comments: true
intuds-weight: 4
---

We should agree by now that [data is a bunch of numbers](/intuds/2015/07/19/data-numbers-representations.html) encoding some information, and that data can be multi-dimensional which makes them live in [vector spaces](/intuds/2015/07/22/vector-spaces.html). In this post we want to look at the very important concept of *dimensionality* more closely.

To do so, let us return to our image example. I have told you previously that this image
{% capture numbersFullUrl %}/intuds/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}
lives in a 945-dimensional vector space. The question is now: how many possible grey scale pictures exist? The math is not so complicated [[1]](#[1])

http://www.quora.com/How-many-particles-are-there-in-the-universe

So let us introduce one of the earliest techniques in dimensionality reduction, PCA with a toy example. Take a look at the following 3d data.
     3d scatter plot of 3d sinus wave rotated in 3d
What do you see? When looking at the animation you will probably notice some kind of wave, floating through 3D space. This wave, however, seems to be only 2-dimensional. You can see that if we draw a plane which contains all the points of the wave:
     3d scatter plot of 3d sinus wave rotated in 3d + plane
This is interesting. Although the dimensionality of our vector space is 3d (we have an x, y and z axis), the wave, i.e. the data is actually in 2D, but somewhat rotated in that space, namely around the z-axis. If we rotate -45 degrees around y, we see that the plane is parallel to x and z, and that the y value of all the data points is 0:
     3d scatter plot of 3d sinus wave rotated to xy + plane

The question is now: How can we devise a method which i) tells us the "real dimensionality" of our data and ii) gives us the rotation that we need to apply such that our data it aligns with the original axes?

The answer is: Of course, PCA will do the job! But how?

The main idea behind PCA is the concept of variation of the data along one dimension. It tries to find the directions, along which the data varies the most, in this case the two directions given by the plane.

- it can also deal with noisy data, e.g. if the wave plotted above would look like this:
     noisy sine wave in 3d

Note that one could be tempted to state variation = amount of information. But there are exceptions. Consider the following 
     Gaussian noise
There is lot of variation, but is there actually information? There isn't really that much, as I just plotted a bunch of random numbers; there is no apparent pattern in this data, unlike the wave we have seen before. Hence, people have been studying other measures for information. Although there is no conclusive answer to the question how to quantify information, I will present another candidate called "slowness" or "temporal coherence" in a forthcoming article on Slow Feature Analysis.

- Applications: Compression

Summary:
- PCA finds out a lower dimensionality of our data, given that only rotations are allowed
- It also finds the optimal rotation in your data space such that the axes of the resulting space vary the most.
performs 
- By reducing the dimensionality of your data, PCA can also be used to compress your data
- Variation can be an indicator for amount of information, but not always


Further Reading:
- Bishop's chapter on PCA. Mathematically dense and very, but contains proofs for the two derivations of PCA, for both the "minimum reconstruction error" and the "" interpretation (TODO lookup) 
- Some PDF which I found once


http://www.flotcharts.org/
http://canvasxpress.org/

Eigenfaces:  http://www.mitpressjournals.org/doi/abs/10.1162/jocn.1991.3.1.71
http://en.wikipedia.org/wiki/Eigenface


Practical Example: Eigenfaces

I hope the toy example above served well to explain the method, but was a bit artificial. Why would we rotate waves in 3D? Hence, let us look at a really cool example from computer vision, so-called Eigenfaces. 

Summary:
- If you apply PCA to pictures of faces, you get Eigenfaces which are helpful for face recognition

Practical Example: Eigengrasps / Motor synergies






### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- 

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Let us assume that a pixel can take a finite number of values. We assume that only 1 digits after the decimal point are allowed. So we have the numbers 0, 0.1, 0.2, ... 0.9, 1.0, which are 10 in total. We have 945 pixels, this makes 10<sup>945</sup> possible images. This is a 1 with 945 trailing zeros! 

2. <a name="[2]"></a>To cite the [mathematician Ian Stewart](http://books.google.de/books?id=dUhMAQAAQBAJ&pg=PA182&lpg=PA182&dq=Classical+mathematics+concentrated+on+linear+equations+for+a+sound+pragmatic+reason:+it+could+not+solve+anything+else.&source=bl&ots=PuRT666z3D&sig=YBZtoUP_y0siL0RUXfC14keMGe4&hl=de&sa=X&ei=upteVPDfBIysPJChgZgE&ved=0CCsQ6AEwAQ#v=onepage&q=Classical%20mathematics%20concentrated%20on%20linear%20equations%20for%20a%20sound%20pragmatic%20reason%3A%20it%20could%20not%20solve%20anything%20else.&f=false): "Classical mathematics concentrated on linear equations for a sound pragmatic reason: it could not solve anything else."
