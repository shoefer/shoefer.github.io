---
layout: post
title:  "Why Machine Learning and AI Needs Agency"
date:   2016-06-06 17:43:00
categories: artificial intelligence
tags: machine learning, artificial intelligence, perception, action
comments: true
---

For a long time now, I have been wondering about whether we need agency to solve difficult AI problems, such as identifying objects on images.  By *agency* I mean that the AI [[1]](#[1]) needs to be able to take actions and possibly have a body, rather than just being a passive observer. The recent advances of deep learning in solving image classification tasks seem to answer this question in the negative: these approaches are given images and labels about the content of these images, and [learn to classify](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) previously unseen images only from these data.
 
<i>Does this mean, we don't need agency and can solve any AI problem with this simple, yet brute-force approach?</i>

In this post, I want to discuss this question, and I will argue that agency <i>is indispensable</i> for solving difficult AI tasks. 
Obviously, this claim is not new -- however, the main contribution of this post is that it puts into perspective a wide variety of approaches that make this claim, and therefore give an [overview](#overview) of the different ways agency is required for AI.

#### Perceptual vs. Control Tasks

To approach the question of agency's role for AI, I distinguish between two categories of AI tasks:
*purely perceptual tasks* and *control tasks*.

Purely *perceptual tasks* are tasks that do not naturally require agency, for example the image classification task described above. Here, the AI makes a decision for every perceptual input independently, i.e. it's prediction for one input does not influence it's prediction on another one.

In contrast, *control tasks* require choosing the right *sequence of actions* in order to solve a problem, e.g. the moves for [winning a game of Go](https://deepmind.com/alpha-go). Thus, the goal is not perception itself, but rather some problem that requires perception -- e.g. analyzing the state of a Go board. 
Of course, these tasks require agency trivially, but they involve perceptual subtasks.

My argument will now go as follows:

1. In control tasks, not only the control task itself but also the perceptual subtasks require agency. The reason is that in these tasks there is no principle difference between perception and action. 
2. Certain purely perceptual tasks can be turned into control tasks -- and thus, for these tasks, all arguments for agency from point 1 apply.
3. Finally, I will argue that even purely perceptual tasks that do not fall under 2 require agency. The reason is that also in these tasks agency enables the learnable AI to leverage information it would not have access to otherwise -- going beyond self-supervised and even for the task of classifying camera images!

<!-- ---------------------------------------- -->

### Control Tasks Blur the Distinction between Perception and Action

#### Motor chauvinism

#### Embodiment


#### Ball and Frisbee Catching

In control problems from perception, we must not solve perception without looking at the task and the action


#### Perception and Action Cannot be Separated

end-to-end learning - where does perception, where does action happen?

<!-- ---------------------------------------- -->

### Purely Perceptual Tasks Turned into Control Tasks

#### Active and Interactive Perception

-> active learning

Tasks that cannot be solved passively.

#### Sensorimotor Contingencies


<!-- ---------------------------------------- -->

### Purely Perceptual Tasks Require Agency

#### Self-supervised Learning


#### Learning with Side Information



<!-- ---------------------------------------- -->

#### Summary

<!-- ---------------------------------------- -->

#### <a name="overview"></a>Overview of Joint Approaches to Perception and Action:

The following list references the different approaches to the role of agency in AI covered in this post:

- Motor chauvinism (Wolpert)
- Mirror neurons (Rizzolatti et al.
- Embodiment (Pfeifer)
- Sensorimotor Contingencies (Noe, O'Reagan)
- Active Learning and Active Perception (Settles, Bajcsy, Aloimonos)
- interactive perception (Brock)
- Learning with side information (Vapnik, Jonschkowski/H&ouml;fer)

The following papers are rerference 
- Do dogs know calculus?
- How to catch a fly-ball

<!-- ---------------------------------------- -->

### <a name="further"></a>Footnotes:
1. <a name="[1]"></a>By "AI" I will denote the algorithm or machine that solves a particular task. Usually, the word "agent" is used here, but I am avoiding it since the key question of this article is whether agency is needed or not.
<!-- 
 2. <a name="[2]"></a>
 3. <a name="[3]"></a>
-->