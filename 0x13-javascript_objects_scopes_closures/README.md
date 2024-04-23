# 0x13. JavaScript - Objects, Scopes and Closures
## JavaScript Objects, Scopes, and Closures

This repository contains a collection of JavaScript scripts demonstrating various concepts related to objects, scopes, and closures.

## Scripts

### 0-rectangle.js

Defines a simple Rectangle class in JavaScript.

### 1-rectangle.js

Defines a Rectangle class with width and height attributes and a print() method to print a rectangle using the character 'X'.

### 2-rectangle.js

Defines a Rectangle class with width and height attributes, but initializes an empty object if either width or height is not valid.

### 3-rectangle.js

Enhances the Rectangle class with a print() method to print a rectangle using the character 'X', a rotate() method to exchange width and height, and a double() method to double the width and height.

### 4-rectangle.js

Defines a Square class that inherits from Rectangle, with additional methods charPrint(c) to print the square using the character `c` (or 'X' if `c` is undefined).

### 5-square.js

Defines a Square class that inherits from Rectangle and initializes width and height with the same value.

### 6-square.js

Enhances the Square class with a charPrint(c) method to print the square using the character `c` (or 'X' if `c` is undefined).

### 7-occurrences.js

Exports a function nbOccurences(list, searchElement) that returns the number of occurrences of searchElement in the list.

### 8-esrever.js

Exports a function esrever(list) that returns the reversed version of a list without using the built-in method reverse.

### 9-logme.js

Exports a function logMe(item) that prints the number of arguments already printed and the new argument value.

### 10-converter.js

Exports a function converter(base) that converts a number from base 10 to another base passed as an argument.

### 100-data.js

Exports an array named list.

### 100-map.js

Imports list from 100-data.js and computes a new array where each value is equal to the value of the initial list multiplied by the index in the list.

### 101-data.js

Exports a dictionary named dict.

### 101-sorted.js

Imports dict from 101-data.js and computes a new dictionary where keys are the number of occurrences and values are lists of user ids.

### 102-concat.js

Concatenates the contents of two files specified as command-line arguments and saves the result to a destination file.

## Usage

To run any of the scripts, ensure you have Node.js installed on your system. Then, navigate to the project directory in your terminal and execute the desired script using Node.js. For example:


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
