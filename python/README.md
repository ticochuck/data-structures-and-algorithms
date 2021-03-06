# Data Structures and Algorithms

## Language: `Python`

# Code Challenges Table of Contents

## Code Challenge 30
Hashtables

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/master/python/challenges/hashtable/README.md)

## Code Challenge 18
Fizzbuzz - Trees

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/hashtable/README.md)

## Code Challenge 18
Fizzbuzz - Trees

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/master/python/challenges/fizz_buzz_tree/README.md)

## Code Challenge 17
Trees - Breadth First

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/tree/README.md)

## Code Challenge 16
Trees - Max Value

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/tree/README.md)

## Code Challenge 15
Trees

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/tree/README.md)

## Code Challenge 13
Multi Bracket Validation

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/multi-bracket-validation/README.md)

## Code Challenge 12
Implementation of a Queue using two Stacks

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/stack-and-queue/python/challenges/fifo_animal_shelter/README.md)


## Code Challenge 11
Implementation of a Queue using two Stacks

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/stack-and-queue/python/challenges/queue_with_stacks/README.md)

## Code Challenge 10
Stack and a Queue Implementation

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/stack-and-queue/python/challenges/stacks_and_queues/README.md)

## Code Challenge 08
Zip 2 lists, alternate value

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/blob/master/python/challenges/ll_merge/README.md)

## Code Challenge 07
k-th value from the end of a linked list

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/tree/master/python/challenges/linked_list)

## Code Challenge 06
append, insert before, insert after

[README.md](https://github.com/ticochuck/data-structures-and-algorithms/tree/master/python/challenges/linked_list)

## Code Challenge 05
[README.md](https://github.com/ticochuck/data-structures-and-algorithms/tree/master/python/challenges/linked_list)

## Code Challenge 03 
[Click here to view the README.md](/challenges/array_binary_search/README.md)

## Reverse an Array
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency
I chose to create a new array and slice the original array into the new one stating from the last index.

## Solution
I sliced the original array into a new array starting at the last index:
```
new_arr = arr[::-1]
```
![](./challenges/assets/array-reverse.png)

# Shift into an Array
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
Find the middle of the array, insert the integer. 

## Solution
I wasn't sure if I could use len to determine the length of the array so I loop through the array and counted the length with a variable called count. 

Once I had the length, I divided by 2 to get the middle point (+1 for odd arrays). Then I used sliced the array from the begining until the middle, and from the middle until the end and concatenated the integer in between. 

```
new_arr = arr[::-1]
```
![](./challenges/assets/array_shift.png)