


A way to understand 
To see this we have to understand how the function with the many wrinkles differs from the line. This is best understood by writing it down in form of a regularity:

<div class="pseudoformula">
<b>Stock price</b> = 0.00000000000000000000000000000000000000000000000838 * <b>Revenue</b><sup>9</sup> + -0.00000000000000000000000000000000000000003643696333 * <b>Revenue</b><sup>8</sup> + 0.00000000000000000000000000000000005884062004493454 * <b>Revenue</b><sup>7</sup> + -0.00000000000000000000000000003210461062540958370768 * <b>Revenue</b><sup>6</sup> + -0.00000000000000000000002460293193572738255386773582 * <b>Revenue</b><sup>5</sup> + 0.00000000000000005082055480013970865215833693431560 * <b>Revenue</b><sup>4</sup> + -0.00000000003578573935150710790314658698018117008455 * <b>Revenue</b><sup>3</sup> + 0.00001327106354536875418791662395445740685318014584 * <b>Revenue</b><sup>2</sup> + -2.58687704821982933367507939692586660385131835937500 * <b>Revenue</b> + 209497.52247695470578037202358245849609375
</div>

This *does* look much more complicated than the linear regularity! Don't worry you do not have to understand where all these numbers come from - you only have to accept that it is exactly these 10 numbers which make the wrinkled red curve look the way it does, similar to the two numbers in the linear case. The main difference is that we do not only multiple numbers with the revenue, but also with higher exponents of the revenue, that is Revenue<sup>4</sup> means Revenue*Revenue*Revenue*Revenue. A more closer inspection also reveals that the line is really a special case of the wrinkled function: if we set all numbers before  the <b>Revenue</b><sup>x</sup> parts to zero, we are back to the line regularity we have seen above (with different numbers though).
 
Anyway, we shall now focus on the *amount of numbers* because it is of particular importance: it let's us quantify how complex the function is. Therefore, the amount of numbers in a function you can choose is also called the *degrees of freedom* of a function. 

I hope now you are ready for the big thing: for the data I have shown you there is only *one line* that goes exactly through all of the points. For the wrinkled function, however, there are infinitely many, for instance:

{% include figure.html src="/intuds/images/2015-08-07-overfitting-sizeprice2.png" width="65%" %}

In other words, it is much much less likely to find a line (having two degrees of freedom) which goes through all the data points than finding a wrinkled function with 10 degrees of freedom going through all the points. 


1. <a name="[1]"></a>Some more terminology in case you are interested: The numbers themselves are usually called *parameters* of the function. And the wrinkled function with all of the exponents is called a *polynomial*.
