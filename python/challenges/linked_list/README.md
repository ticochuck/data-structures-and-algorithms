# Linked Lins

[Link to Latest PR](https://github.com/ticochuck/data-structures-and-algorithms/pull/43)

## Description

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
    - Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    -   Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    -   Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"

- Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.


## Tests

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list


## Usage

Start by creating a new LinkedList:
```
ll = LinkedList()
```

Then insert some values into your LinkedList
```
ll.insert('Saturday')
ll.insert('Friday')
ll.insert('Thursday')
ll.insert('Wednesday')
ll.insert('Tuesday')
ll.insert('Monday')
ll.insert('Sunday')
```
Then print the head value
```
print(ll.head)
```

returns:
Sunday, Next_Node=Monday, Next_Node=Tuesday, Next_Node=Wednesday, Next_Node=Thursday, Next_Node=Friday, Next_Node=Saturday, Next_Node=None

## Challenges

Writing tests is always a bit confusing. 

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)