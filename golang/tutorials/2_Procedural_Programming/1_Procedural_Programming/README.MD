# Procedural Progamming 

What is procedural
programming? At this point, procedural programming is just what you would call…
programming. We defined programming as giving instructions to the computer to
carry out in order. That’s what procedural programming is.

### Functional Programming 

Much of programming is based around the idea of “functions”, in some circum-
stances referred to as “methods.” A function is like a little machine: you drop
something in, and it spits something out. We refer to what you put in as the “input”
and what you get out as the “output”, and we usually say that the function or method
“returns” the output. Functional programming is a fundamental part of most modern
programming languages

### Hello World 

```
// 1_hello_world.go
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
}

```
outputs:
```
$ go run 1_hello_world.go 
Hello world
```
A series of these lines would execute that command a series of times. The
computer executes each line one by one. If one line is repeated several times, it gets
executed several times.
```
// 2_hello_world_2.go
package main

import "fmt"

func main() {
	fmt.Println("Hello world")
	fmt.Println("Hello world")
	fmt.Println("Hello world")
	fmt.Println("Hello world")
}

```
outputs
```
$ go run 2_hello_world_2.go 
Hello world
Hello world
Hello world
Hello world
$ 
```
### Data Types and Variables
Strings of characters aren’t the only things we print. Oftentimes, we’ll print integers,
decimal numbers, and more complex information as well.
```
// 3_datatypes_and_variables.go
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(5)
	fmt.Println(5.1)
	fmt.Println(time.Now())
}

```
output will be 
```
$ go run 3_datatypes_and_variables.go 
5
5.1
2021-09-26 15:50:39.101307189 +0530 IST m=+0.000311423
$ 

```
Most often, we don’t print or use values like those directly. Typically, we store
them in variables, and then use the variables in our programming.
```
// 4_datatypes_and_variables.go
package main

import (
	"fmt"
	"time"
)

func main() {
	myInteger := 5
	fmt.Println(myInteger)
	myFloat := 5.1
	fmt.Println(myFloat)
	currentTime := time.Now()
	fmt.Println(currentTime)
}

```
Outputs
```
$ go run 4_datatypes_and_variables.go 
5
5.1
2021-09-26 15:56:42.859983434 +0530 IST m=+0.000212550
$ 

```
The usefulness of this is that we can have a single variable name that changes its
value over time. Imagine you have a variable representing a bank account balance,
The value of the bank account balance changes over time, but the
idea of having a balance is consistent. So, the variable name, myBalance, stays the
same, but its value can change.
```
// 5_datatypes_and_variables.go
package main

import "fmt"

func main() {
	myBalance := 100.0
	fmt.Println(myBalance)
	myBalance = 105.0
	fmt.Println(myBalance)
}
```
Output:
```
$ go run 5_datatypes_and_variables.go 
100
105
$ 
```
The usefulness of variables is in our ability to interact with and modify them, and
one of the most fundamental ways we interact with and modify variables is with
operators. **There are two kinds of operators: logical operators and mathematical
operators.**

### Logical Operators
- Relational Operators
``` 
  - ==
  - >
  - < 
  - >=
  - <=
```
- Logical Operators 
```
  - and 
  - or
  - not
```
