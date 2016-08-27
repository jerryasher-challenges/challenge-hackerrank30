# Day 12: Inheritance

https://www.hackerrank.com/challenges/30-inheritance

Objective 
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, first name
A string, last name
An integer, id
An integer array (or vector) of test scores, scores

A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

O avg >= 90
E avg >= 80
A avg >= 70
P avg >= 55
D avg >= 40
T avg >= 0

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin: 
The first line contains first name, lastname, and id, respectively. The second line contains the number of test scores. The third line of space-separated integers describes scores.

Constraints

4 <= |first name|, |lastname| < 10

|id| 7

0 <= score, average <= 100

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

