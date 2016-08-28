# Day 27: Testing

This challenge is very different from the others we've completed because it requires you to generate a valid test case for a problem instead of solving the problem. There is no input to read, you simply have to generate and print test values for the problem that satisfy both the problem's Input Format and the criteria laid out in the Task section. Check out the Tutorial tab for an instructional video on testing!

Consider the following problem (but do not solve it):

Problem Statement

A Discrete Mathematics professor has a class of  students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than  students are present when class starts. Given the arrival time of each student, determine if the class is canceled.
Input Format

The first line of input contains , the number of lectures.
The information for each lecture spans two lines. The first line has two space-separated integers,  (the number of students in the class) and  (the cancelation threshold). The second line contains  space-separated integers describing the array of students' arrival times ().

Note: Non-positive arrival times () indicate the student arrived early or on time; positive arrival times () indicate the student arrived  minutes late. If a student arrives exactly on time , the student is considered to have entered before the class started.
Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.
Example

When properly solved, this input:
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Produces this output:
YES
NO
For the first test case, . The professor wants at least  students in attendance, but only  arrive on time ( and ). Thus, the class is canceled.

For the second test case, . The professor wants at least  students in attendance, and  do arrive on time ( and ). Thus, the class is not canceled.