# Programming 

## What Is Programming?

Programming is the foundation of computing. Programming is effectively being
able to speak the computer’s language, to give it directions in a way that it under-
stands. Like any language, computers have vocabulary words and syntax that they
understand.

## Writing Code: Lines 

the most basic atom of development is the line of code. Lines of code are individual commands to give to the computer. Chains of these lines form complex behaviors or instructions for the computer to carry out.

### Chaining Together Instructions

Imagine we are developing a program to print out the roster of students in this class.
One command would instruct the program to grab a student’s profile from some file
or database. Another would instruct the program to grab the student’s name from
that profile. Another would instruct the program to print that name. Another would
instruct the program to repeat those three commands for every student in the class.
By chaining these instructions together, the computer can print out the entire class
roster

### The Print Statement

the Println() command is the first fundamental thing to understand. This is how you print output for you to see while running.

### Work in Small Chunks

We want to develop programs in small chunks. You don’t write an entire essay from start to end without reading over the paragraphs as you write them. You likely wouldn’t paint a picture from start to finish without pausing to
get feedback. So also, we want to develop our programs in small chunks, testing
throughout to make sure we’re on the right track

## Writing Code: Lines in Go

### Your First Program: Hello, World

```
// #1_hello_world.go
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}

```
you would get output like this if you run it
```
$ go run 1_hello_world.go 
Hello World
```
### Printing Other Values

In addition to printing strings of characters like “Hello, world,” . Go also lets us
directly print a couple other things. First, we can print numbers like 5 or 5.1 directly
using the print statement without quotation marks. Second, we can also print what
are called “boolean” values.

```
// 2_PrintingOtherValues.go
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
	fmt.Println(5)
	fmt.Println(5.1)
	fmt.Println(true)
	fmt.Println(false)
}

```
if you run this go code you would get output like this 
```
$ go run 2_PrintingOtherValues.go 
Hello World
5
5.1
true
false
$ 
```
## Executing Code in Go

### Encountering Errors
Let’s try an example of this.Below are five lines of code. You might notice
that the fifth line has an error: I’ve misspelled the word “Println.” 
```
// 3_ExecutingCode.go
package main

import "fmt"

func main() {
	fmt.Println("This is Line1")
	fmt.Println("This is Line2")
	fmt.Println("This is Line3")
	fmt.Println("This is Line4")
	fmt.Prinln("This is Line5")
}

```
What happens when
I run this code? it prints the error message
```
$ go run 3_executing_code.go 
# command-line-arguments
./3_executing_code.go:11:2: undefined: fmt.Prinln
$ 
```
### Compiling in Go

when we compile this code we get 
```
$ go build 3_executing_code.go 
# command-line-arguments
./3_executing_code.go:11:2: undefined: fmt.Prinln
$ 
```
