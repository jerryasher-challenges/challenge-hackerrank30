#Day 8: Dictionaries and Maps

https://www.hackerrank.com/challenges/30-dictionaries-and-maps

Objective 

Today, we're learning about Key-Value pair mappings using a Map or
Dictionary data structure. Check out the Tutorial tab for learning
materials and an instructional video!

Task 

Given names and phone numbers, assemble a phone book that maps
friends' names to their respective phone numbers. You will then be
given an unknown number of names to query your phone book for; for
each name queried, print the associated entry from your phone book (in the
form name=phonenumber) or notfound if there is no entry for name.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer, n , denoting the number of entries
in the phone book.  Each of the subsequent lines describes an entry in
the form of 2 space-separated values on a single line. The first value
is a friend's name, and the second value is an 8-digit phone number.

After the lines of phone book entries, there are an unknown number of
lines of queries. Each line (query) contains a to look up, and you
must continue reading lines until there is no more input.

Note: Names consist of lowercase English letters and are first names
only.

Constraints

Output Format

On a new line for each query, print not found if the name has no corresponding
entry in the phone book; otherwise, print the full name and phonenumber in the format name=phonenumber.

Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933

Explanation
N = 3

We add the n subsequent (Key,Value) pairs to our map so it looks like
this:

phonebook = {(sam, 99912222),(tom,11122222),(harry, 12299933)}

We then process each query and print key=value if the queried Key is found in
the map, or notfound otherwise.

Query 0:  sam

Sam is one of the keys in our dictionary, so we print sam=9991222

Query 1:  edward

Edward is not one of the keys in our dictionary, so we print not found

Query 2:  harry

Harry is one of the keys in our dictionary, so we print harry=12299933
