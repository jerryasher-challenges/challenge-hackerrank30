# Day 20: Sorting

https://www.hackerrank.com/challenges/30-sorting

Objective 

Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}

Task 

Given an array, a, of size n containing distinct elements, sort array a in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:

Array is sorted in numSwaps swaps
where  is the number of swaps that took place.
 
First Element: firstElement
where  is the first element in the sorted array.
 
Last Element: lastElement
where  is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, n, denoting the number of elements in array a. 
The second line contains n space-separated integers describing a, where the ith integer is a[i].

Constraints

0 <= n <= 600
 
Output Format

There should be  lines of output:

 
where  is the number of swaps that took place.
 
where  is the first element in the sorted array.
 
where  is the last element in the sorted array.

Sample Input 0

3
1 2 3

Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3