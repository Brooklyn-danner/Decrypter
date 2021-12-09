*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  Requirements Specification

I am to be given a DuckieCrypt that I have to translate. This DuckieCrypt consists of a flag (denoting uppercase, lowercase, 
and special characters) as well as a value for that specific letter or character. Each of these provided flags and values correlate 
to a letter or character that I must output. I will have to find the relationships between ASCII values and the DuckieCrypt 
characters in order to successfully translate.


# 1.  System Analysis

The words/ phrases I must translate will be presented in a file which I must safely open, read, and close (I already completed 
this process in lesson 2). I will use loops and if statements to analyze the text that I will read in to determine its value
and then translate it. I will then output the translation in a single string.

# 2.  Design

I plan to create a method, getFileSafe, that takes in the text in the provided file. I will send the single string created from 
getFileSafe into a method called incr (short for increment).

Incr will loop through the string given, taking in the characters by two because there will always be a flag and a character code. 
Within this method there will be a string called newOne. This holds the translated, readable characters. Each of these characters 
will be added to newOne when it is returned from calling translate.

The translate method will translate the flag and character code into its respective letters and symbols. I'll use variable string
flag to take in the given flag and int givenNum to take in the character code. I will begin by first taking in the flag. If it is 
a ^ I'll add 65 to the givenNum and use chr() to translate this ASCII value into a character. If it is a _ I will add 97 to 
givenNum and will also use chr() to translate this ASCII value into its respective character. If it's a plus I'll do a further 
check to see if the next character is an A, B, or C. If it's an A I will add 32 to the remaining number and use chr() to translate 
this ASCII value into a character. If it's a B, I will add 91 to the remaining number and use chr() to translate this ACII value 
into a character. Finally, if it's a C, I will add 123 to the remaining number and use chr() to translate this ASCII value into a 
character. Translate will output a string which will be accessed when I call the method.


# 3.  Implementation

Realized I needed another method for reading in the lines so that I could call translate within that method. Translate only takes
in and produces a single character. I needed a method for all contents in the line.

# 4.  Testing and Debugging

Ran into two main problems. I accidentally called ord() instead of chr() so it was throwing me a few errors.
I also didn't increment enough through the string char in the + if statement so it was reading in too many characters for char. It
was too much for my translate method to translate so it threw a few errors.

# 5. Deployment

In this course deployment means turning in your work.

Don't leave deployment to the last moment.
Give yourself plenty of time to correct any problems that you may discover.
Review the rubric and penalties to make sure that you won't be shocked by your score.  Pay particular attention to:

The naming of your git repository and its URL on the course GitLab server.
The presence of a .gitignore file which prevents unwanted files from being committed.

Verify that your final commit was received by browsing to its project page on GitLab.
Review the project to ensure that all required files are present and in correct locations.

Validate that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
Run through the test cases to avoid nasty surprises.
