---
layout: intuds_post
title:  "High-dimensional Spaces"
date:   2015-07-25 16:02:00
categories: intuds
comments: true
intuds-weight: 1
---

In the [last post](/intuds/2015/07/19/data-numbers-representations.html) we have seen examples for how numbers can encode information, yielding data. In this post we will talk about a very important way to look at data. This view will allow us to play around with data in a powerful way, and this view lies at the core of data science.

I have previously told you that any [image](/intuds/images/2015-07-19-data-numbers-representations_picture.png) can be represented by a [table of numbers](/intuds/images/2015-07-19-data-numbers-representations_numbers.png) where each number encodes the gray scale value of the image. Let us pick some arbitrary three consecutive numbers in a row, for example the first three numbers in the 10th row:
<table class="data-table">
<tr>
<td style="background-color: #000; opacity: 0.909; width: 30px">0.909</td>
<td style="background-color: #000; opacity: 1.0; width: 30px">1.000</td>
<td style="background-color: #000; opacity: 0.860; width: 30px">0.860</td>
</tr>
</table>
I have set the color of each table cell to correspond to the actual gray scale value the number encodes. Now comes the trick: although we know that these three numbers encode gray scale values we can *do as if* they were actually encoding the location of a point in 3D space. So instead of encoding "luminosity" we think of the numbers are being in "meters" or "centimeters". As you might remember from high school we draw locations as an arrow in an coordinate system:
{% include figure.html src="/intuds/images/2015-07-21-vector_spaces-arrow.png" width="300" gifplayer="true" id="vector-spaces-arrow" %}
So you might think: "drawing arrows is really fun but why the heck are we doing this?" The reason is this that we humans are really good at manipulating objects in 3D space. We know how to move objects, we know how to rotate them, how to distort and mirror them, how to project them on a 2D planar surface (by taking a picture of it), and much more. Thus, if we treat data as locations in space we can apply all our spatial 3D knowledge to it. 
In fact, [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) has got all the math worked out to simulate these 3D operations on computers (as you can admire in Toy Story, Madagascar, and so on) [[1]](#[1]). But even better, linear algebra is so general that it does not care about the dimensionality of the data - it works for 3D spaces in the same way as for 5-dimensional or 500-dimensional spaces, even though our brains are not capable of imagining 500-dimensional data visually! This allows us to treat the 27x35 [picture](/intuds/images/2015-07-19-data-numbers-representations_picture.png) of me as a point in 945-dimensional space [[2]](#[2]). We will see later that applying such operations as moving and rotating a point in this huge space will be the basis for extracting information from it, as for example detecting what is in the image represented by this point [[3]](#[3]).

#### Terminology

Some notes on terminology.
Often, a point is called a *vector*, and it then lives in a  *vector space* of some dimensionality. Although being basically the same thing, the term vector has a slightly different connotation which we will ignore for now and stick to the term vector.

Moreover, mathematics tries to be parsimonious with concepts, mainly because it makes talking about things easier. Therefore, we get rid of the concept "numbers" by treating them as 1-dimensional vectors. So in the future if I talk about vectors, you can often think of them as just being numbers. 

#### Summary

To summarize, the approach of data science is the following: we transform some input, for example an [image](/intuds/images/2015-07-19-data-numbers-representations_picture.png) into a [table of numbers](/intuds/images/2015-07-19-data-numbers-representations_numbers.png), call this a *vector* and then treat this vector as a point in a high-dimensional space. We then apply our knowledge of how to manipulate points in 3D to transform this high-dimensional vector in order to extract information from it. 

In the next post we will take a closer look at what dimensionality of data means. 
After that we will look at how be more precise about what we mean by transformations by introducing the concept of functions.

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Data can be viewed as points in space
- We can apply the same transformations to points in this space as in 3D
- Such points are called vectors

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Actually, linear algebra can do even a bit more than what is "physically possible" in the 3D world. 
2. <a name="[2]"></a>For images this requires us to remove the column and row structure and write all of the numbers in one very long row. This is indeed common practise when learning from images.
3. <a name="[3]"></a>It is important to notice that moving or rotating a point in 945-dimensional space which represents an image *is not the same* as shifting or rotating the image! Since moving in 3D is equivalent to "adding a number to one or more dimensions", this is also the definition of moving in 945-dimensional space. If you push a 3D object 3m up and 5m to the right you effectively add these two numbers some coordinates of the object. Hence, in the image example, moving is equivalent to changing the gray scale value of certain pixels. 
<!--  Rotations look even weirder: -->
<!-- TODO rotated image -->