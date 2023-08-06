# Headfuck
A Brainfuck-like esoteric programming language based on matrices.
This language has all of the usual Brainfuck commands, as well as a few more, bolded below:
* \> moves forward in an array
* < moves backward in an array
* \+ adds one to the value of the current cell in the array
* \- removes one from the value of the current cell in the array
* . displays the value of the current cell to the user
* , requests user input to modify the value of the current cell
* \[ starts a loop
* \] closes a loop
* **^ moves up in a matrix**
* **v mves down in a matrix**
* **# displays the first ten rows of the matrix**
* **! reads and interpret the contents of a file**
* **& dumps the outputs of the code to a file**
* **\* multiplies the value of the current cell by two**
* **/ sets the value of the current cell to zero**
* **? sets the value of the current cell to a random ASCII-compatible number**
* **= sets a variable with the name of the letter after it (e.g. =a creates a variable called a)**
* **@ sets the value of the current cell to the variable with the name of the letter after it (e.g. @a sets the current cell to a)**

Headfuck adds I/O and 2-D arrays on top of the functionalities of basic Brainfuck.

Installing this package via `pip3 install headfuck` will grant you access to the `headfuck` and `hff` commands. `headfuck` is a live interpreter where you simply type that command and then type your code as input. `hff` interprets a file that is passed as an argument, e.g. `hff file.bf`.