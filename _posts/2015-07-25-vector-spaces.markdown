---
layout: intuds_post
title:  "High-dimensional Spaces"
date:   2015-07-25 16:02:00
categories: intuds
comments: true
intuds-weight: 3
---

In the [last post](/intuds/2015/07/19/data-numbers-representations.html) we have seen examples for how numbers can encode information, becoming data. In this post we will talk about a very important way to look at data. This view will allow us to play around with data in a powerful way, and this view lies at the core of data science.

I have previously told you that any [image](/intuds/images/2015-07-19-data-numbers-representations_picture.png) can be represented by a [table of numbers](/intuds/images/2015-07-19-data-numbers-representations_numbers.png) where each number encodes the gray scale value of the image. For the trick that I want to show you, this image is actually pretty large. So for the sake of the argument, let us shrink the image drastically until it gets really really tiny, namely only 3 pixels wide and 1 pixel high - bear with me for a second even if this sounds silly to you because we won't see anything on this image. Our 3x1 image expressed in gray scale values now looks like this:

<table class="data-table">
<tr>
<td style="background-color: #000; opacity: 0.909; width: 30px">0.909</td>
<td style="background-color: #000; opacity: 1.0; width: 30px">1.000</td>
<td style="background-color: #000; opacity: 0.860; width: 30px">0.860</td>
</tr>
</table>

I have set the color of each table cell to correspond to the actual gray scale value the number encodes. Here comes the trick: although we know that these three numbers encode gray scale values we can *do as if* they were actually encoding the location of a point in 3D space. So instead of encoding "luminosity" we think of the numbers are being in "meters" or "centimeters". As you might remember from high school we draw locations as an arrow in an coordinate system:

{% include figure.html src="/intuds/images/2015-07-21-vector_spaces-arrow.png" width="300" gifplayer="true" id="vector-spaces-arrow" %}

So you might think: "drawing arrows is really fun but why the heck are we doing this?" There are two reasons for that: the first reason is this that we humans are really good at manipulating objects in 3D space. We know how to move objects, we know how to rotate them, how to distort and mirror them, how to project them on a 2D planar surface (by taking a picture of it), and much more. Thus, if we treat data as locations in space we can apply all our spatial 3D knowledge to it. 
In fact, [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) has got all the math worked out to simulate these 3D operations on computers (as you can admire in Toy Story, Madagascar, and so on) [[1]](#[1]). 

The second reason justifies why I am telling you all of this while talking about 27x35 pixel wide images: linear algebra is so general that it does not care about the dimensionality of the data - it works for 3D spaces in the same way as for 5-dimensional or 500-dimensional spaces, even though our brains are not capable of imagining 500-dimensional data visually! This allows us to treat the 27x35 [picture of my face](/intuds/images/2015-07-19-data-numbers-representations_picture.png) as a point in some crazy unimaginable 945-dimensional space [[2]](#[2])! We will see later that applying such operations as moving and rotating a point in this huge space will be the basis for extracting information from it, as for example detecting what is in the image represented by this point [[3]](#[3]).

Another really cool thing is that we can understand how the computer can discriminate between images depicting objects from different categories. Imagine we have another image of, say a [blobfish](http://conservationmagazine.org/wordpress/wp-content/uploads/2013/11/blobfish.jpg). By the same procedure as before we can make the blobfish a point in 945-dimensional space. Now let's assume we do not only have one picture of me and one of the blobfish, but a whole bunch of pictures for each category. We can now try to discriminate between the two categories by finding a plane which separates these two points (blue is me, red the blobfish):

{% include figure.html src="/intuds/images/2015-07-21-vector_spaces-arrow-plane.png" width="300" gifplayer="true" id="vector-spaces-arrow-plane" %}

Using this plane, the computer can now automatically discriminate between blobfish and Sebastians. To do so it first translates the image into this 945-dimensional space, and checks on which side of the plane the point lies. 

Sit back for a second and make sure that you have understood this. Because if so you can be proud - you have just understood the key principle behind data science approaches to [image classification](/intuds/2015/07/26/datascience-showoff.html), the problem that I have presented in the intro article! Of course, there are some "details" that I have omitted. 
First, we would not use the shrinked 3x1 images, but rather try to find a discriminating plane in the original 945-dimensional space of 27x35 images  (there it would actually be called a *hyperplane*, that's what a plane is called in four or more dimensions - not to be confounded with [hyperspace](http://starwars.wikia.com/wiki/Hyperspace)). Of course, we can then neither visualize the images nor the discriminating hyperplane in this high-dimensional 945-d space, but the discrimination would still work the same way as in 3D. 

Second, I have not (yet) told you how to find this hyperplane. This is of course a crucial aspect of data science; there are actually different ways to find this hyperplane, and I will cover this in a later article.

Third, I have to lower your expectations about this method a bit: discriminating Sebastians and blowfish by finding a plane in this 945-dimensional space does not really work well in practise. The reason is that pictures of Sebastians and blowfish are not as nicely separable as I have suggested in the 3D arrow picture above. But the general idea of finding discriminating hyperplanes in high-dimensional spaces still holds. And we can get it to work by first bringing the image into a different *representation*, that is a different space, and then finding the hyperplane in this new space (at this point you should remember our discussion about representations in [the previous post](/intuds/2015/07/19/data-numbers-representations.html)). You can either try to transform images in these representations explicitly, i.e. think of a good representation and program it yourself, or implicitly, trying to find a cool data science tool that does this automatically. We will talk about both approaches later, too.

#### Terminology

Some last notes on terminology.

Often, sequence of numbers, such as the 3d point or the 945-dimensional representation of the image is called a *vector*, and it then lives in a  *vector space* of some dimensionality. Although being basically the same thing, the term vector has a slightly different connotation which we will ignore for now. But I will often use the vector just because it sounds cooler.

Secondly, mathematics tries to be parsimonious with concepts, mainly because it makes talking about things easier. Therefore, we get rid of the concept "numbers" by treating them as 1-dimensional vectors. So in the future if I talk about vectors, you can often think of them as just being numbers. 

#### Summary

To summarize, the approach of data science is the following: we transform some input, for example an [image](/intuds/images/2015-07-19-data-numbers-representations_picture.png) into a [table of numbers](/intuds/images/2015-07-19-data-numbers-representations_numbers.png), call this a *vector* and then treat this vector as a point in a high-dimensional space. We then apply our knowledge of how to manipulate points in 3D to transform this high-dimensional vector in order to extract information from it. Moreover, we can classify between different types of data, for example object categories, by finding discriminating hyperplanes in this space.

In the next post we will look at how be more precise about what we mean by transformations and how to describe these hyperplanes by introducing the concept of functions.

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
- Data can be viewed as points in high-dimensional spaces
- We can apply the same transformations to points in this space as in 3D
- Such points are called vectors
- Hyperplanes in space discriminate between vectors

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>Actually, linear algebra can do even a bit more than what is "physically possible" in the 3D world. 
2. <a name="[2]"></a>For images this requires us to remove the column and row structure and write all of the numbers in one very long row. This is indeed common practise when learning from images.
3. <a name="[3]"></a>It is important to notice that moving or rotating a point in 945-dimensional space which represents an image *is not the same* as shifting or rotating the image! Since moving in 3D is equivalent to "adding a number to one or more dimensions", this is also the definition of moving in 945-dimensional space. If you push a 3D object 3m up and 5m to the right you effectively add these two numbers some coordinates of the object. Hence, in the image example, moving is equivalent to changing the gray scale value of certain pixels. Neither do vector rotations actually rotate the image. 
<!--  Rotations look even weirder: -->
<!-- TODO rotated image -->
