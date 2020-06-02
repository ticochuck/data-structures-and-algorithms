# Data Structures and Algorithms

## Language: `Python`

# Reverse an Array
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency
I chose to create a new array and slice the original array into the new one stating from the last index.

## Solution
I sliced the original array into a new array starting at the last index:
```
new_arr = arr[::-1]
```
![](./challenges/assets/array-reverse.png)