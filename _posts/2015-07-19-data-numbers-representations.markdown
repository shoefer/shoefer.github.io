---
layout: intuds_post
title:  "Data, Numbers and Representations"
date:   2015-07-19 15:07:27
categories: intuds
comments: true
intuds-weight: 1
---
I would like to start the intuitive introduction to data science by looking at the term *data*.  Let us try to gain an informal but sufficient understanding of how we could define data.

### Data is numbers

Big data, data mining, data analysis, data, data, data - everyone wants data. But what *is* data? The philosophical answer could be: information. The statistician's answer would probably be: a bunch of numbers. 
Indeed, we are going to stick to the latter definition, namely that *data is everything that can be encoded by numbers* [[1]](#numbersencode).

Some examples: a picture you have taken with your digital camera is data. You can look at it, see the things depicted on it. But your digital camera uses numbers to store the pictures. Also the MP3 sound file that your are currently listening to is data. Even this text here is data! So how is data numbers?
<!-- However, information is also quite an obscure term. So let's define data as "everything you might consider doing something with".  -->

Let's look at concrete example of a picture:
{% capture numbersFullUrl %}/intuds/images/2015-07-19-data-numbers-representations_numbers.png{% endcapture %}
{% include figure.html src=numbersFullUrl width="85%" %}

What do we see here? It's a picture of [my face](/intuds/images/2015-07-19-data-numbers-representations_picture.png) of course! Ok, if you don't see it don't worry (and if you do then you have probably watched [The Matrix](https://en.wikipedia.org/wiki/The_Matrix) too often). The trick is that I have taken [this grey scale picture](/intuds/images/2015-07-19-data-numbers-representations_picture.png)  and replaced every dot in the original picture with a number between 0 and 1 where 0 means "black" and 1 means "white", and the numbers in between represent the different shades of grey between these black and white tones. So effectively, I have become a bunch of numbers!

(If you wonder why it is so difficult to recognize my face in the table of numbers while it is not in the grey scale picture read [this short post](/intuds/2015/07/23/difficult-cv.html).)

### Data is numbers + what + encoding

However, the way how I have chosen the numbers to substitute grey values in the picture is entirely arbitrary. We could have done the same by representing black with 0.5 and white with 12, reverse the order, or even mix up the order of the numbers, etc. The way how you choose the numbers is completely up to you. But it is very important to know that: somebody else will not know how to make sense of the numbers unless you tell her that it is a picture and which numbers correspond to which grey scale. The latter information, of how to translate grey scale values to numbers and back is what we call the *representation*, and is also sometimes called the *encoding* of the data. 

<!-- 
Moreover, some representation might be better or worse with respect to some criterion. For example, when encoding grey scale values between 0 and 1 is immediately know that 0.5 is an average grey; we wouldn't have this intuitive understanding if we encoded the values between 41543 and 341125.
 -->

What about the sound file example? This one is a bit more tricky. You have to know quite a lot about the physics of sound. Let's take a 10 seconds sound file. The easy way to think about how to encode sound by numbers is to divide the 10 seconds a sound file into say 10000 equally sized parts à 1 millisecond and assign a number to each part. Every number corresponds to the "loudness" of a part. That's basically it! You might wonder now how a human voice, a guitar and the engine of a car can all be broken done to these few numbers. Well, it's really just that! The real "magic" is happening in your brain which collects these pieces of information and generates a certain sensation which you identify as an opera singer or Jimi Hendrix playing his guitar. 
If you want to learn more about these things I recommend you to look into [this book [2]](#brainonmusic) which does a great job at explaining what sound and music really is and how the brain comes at perceiving it the way it is. 

What is finally left is the text example. This one is easy, too. I leave it as an exercise to you to think of how to encode or represent text as numbers. (A hint: think about how many different letters and characters we have in our alphabet).

As a final remark, don't forget that the representation of data is a very crucial thing. 
The representation of a problem can drastically influence the ability to solve it (as exemplified very well in [[3]](#funwithrepr)), and corresponds directly to the question of how to represent data.
Lots of the stuff you will read about in future articles deals with transforming numbers from one representation into another. In the next article we will come up with an interesting way of looking at data in order to extract information from it.

### [TL;DR](http://de.urbandictionary.com/define.php?term=tl%3Bdr):
* Data is numbers + representation (what these numbers represent)
* How data is represented is crucial

### Further reading and thinking:
1. <a name="numbersencode">Is there something that cannot be encoded by numbers?</a> Some people would argue there isn't. Do you agree? What would be the consequences of it?
2. <a name="brainonmusic">[This Is Your Brain on Music](https://en.wikipedia.org/wiki/This_Is_Your_Brain_on_Music) by Daniel J. Levitin</a>
3. <a name="funwithrepr">[Fun with representations](https://catenary.wordpress.com/2006/08/19/fun-with-representations-i-nine-numbers/)</a> is a fantastic series of articles about representations, and how different representations enable us to solve complex problems more easily than others.
