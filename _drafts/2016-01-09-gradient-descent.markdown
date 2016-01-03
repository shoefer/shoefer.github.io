---
layout: intuds_post
title:  "Gradient Descent - Walking Down the Error"
date:   2016-01-10 15:00:00
categories: intuds
comments: true
intuds-weight: 20
intuds-category: Machine Learning Methods
---

### Building blocks

#### Functions

#### Derivatives

derivative ~ difference (in *output space*) between two very close-by (in *input space*) values



#### Prediction function

f

Three types of numbers:
- Input
- Output
- Parameters

Looking for the parameters that predict the right output for all possible inputs.

Figure 1: Stock price prediction functions


#### Training error function

<div class="pseudoformula">
<b>err</b>(<b>f</b>) =   <b>f</b>(x[1]) - y[1] &nbsp; &nbsp; + &nbsp; &nbsp;  <b>f</b>(x[2]) - y[2] &nbsp; &nbsp;  + &nbsp; &nbsp; ...
</div>


We could have added the x-y-pairs to the argument list of the function, but we assume they are fixed.


<div class="pseudoformula">
<b>err</b>(p) =   p*x[1] - y[1] &nbsp; &nbsp; + &nbsp; &nbsp;  p*x[2] - y[2] &nbsp; &nbsp; +&nbsp; &nbsp;  ...
</div>


<div class="pseudoformula">
<b>err</b>(p) =   (p*x[1] - y[1])<sup>2</sup> &nbsp; &nbsp;  + &nbsp; &nbsp;  (p*x[1] - y[2])<sup>2</sup> &nbsp; &nbsp; + &nbsp; &nbsp; ...
</div>


### Minimizing the training error



### Gradient descent




#### Competitors

#### Extensions


#### Summary