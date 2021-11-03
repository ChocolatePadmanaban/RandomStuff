# Logical Operators

## What are logical Operators 

To ask what logical operators are, we must first ask: what are operators? Operators are the simplest way to act on data, typically on simple data types like integers, strings, and floats.we’ll discuss two different types of operators: logical operators in this chapter, and mathematical operators

### Mathematical Operators
Mathematical operators are the more familiar but less important category of operators. Most languages have at least five mathematical operators: addition, subtraction, multiplication, division, and modulus. The first four of these are the same operations you’ve been discussing for years, since early arithmetic. The fifth, modulus, is the remainder function, the remainder when one integer is divided by another. Some languages might have dedicated operators for exponents or other common operations, while others might use functions for those tasks.

### Logical Operators
Logical operators are likely less familiar, but they play a bigger role in computing. Some of these are used for comparisons, like checking if two values are equal to
one another or if one is greater than the other. Others are used for chaining together logical decisions like these, checking if multiple conditions are true or if one of many conditions is true.

Logical operators are incredibly powerful in computing. They are how we check to see if complex sets of conditions are met, and they are fundamental to how we control the execution of our programs. Every condition and loop that we cover in the next unit is governed in some way by logical operators.

## Relational Operators
The ultimate goal of all logical operators is to assess whether certain statements are true or false. They only have two possible outcomes, true or false. A lot of complicated reasoning can go into that, though. The good thing is that we actually think in terms of logical operators every day, so we can pretty quickly jump to understanding these operators in our code.

Generally, there are two kinds of logical operators: relational operators and boolean operators. Relational operators check if things are true in the world or in our data. Boolean operators typically check the combination of multiple relational operators. Don’t let the complex terminology here scare you: you’ll see soon this reasoning is very natural, and in fact, you engage in it every day.

Relational operators check the relationships between multiple things. Let’s first
take some examples from the real world, and then look at some examples more core
to programming.

### Numeric Comparisons

Let’s say you go to the kitchen for a snack. You open the refrigerator to get some grapes, but you find that there aren’t any. So, you add grapes to your grocery list. That was a relational operator: you compared the number of grapes to some number in your head, in this case 0, and reasoned that it is true that the number of grapes in the refrigerator equals zero. That’s the relational operator between a variable, the
number of grapes, and some number you have in mind.

### Non-Numeric Equality Comparisons

Relational operators aren’t just numeric comparisons, though. We can compare non-numeric equality as well. You grab your orange and sit down in front of the TV. You check the listings to see what’s on, and you see your favorite show is on two different channels. You check what episodes are playing, and see both channels are playing the same episode, so you just choose which one to select randomly. That’s a non-numeric equality comparison: you judged that it was true that the two episodes
were “equal”, so you chose randomly.

### Set Operators

Right as you’re about to sit down, though, you realize you didn’t grab a drink. You go back to the fridge and see water, apple juice, and milk. You have a dairy allergy, though, so you select between water and apple juice. That’s another relational operator: you checked to see if each beverage was in the set of things to which you’re allergic, and chose one that gave the answer “false.”


## Relational Operators in Go

Our numeric comparison statements are very simple. If we want to compare whether two numbers are equal, we just write the numbers (or the variables holding the numbers) with two equals signs between them.


```
//1_numerical_equilaty_comparisons.go

package main

import "fmt"

func main() {
	fmt.Println(5 == 3)
	fmt.Println(5 == 3)
	a := 5
	b := 5
	c := 3
	fmt.Println(a == b)
	fmt.Println(a == c)

}

```
Output:
```
$ go run 1_numerical_equality_comparisons.go 
false
false
true
false
```
### Numeric Value Comparisons

In addition to checking if numbers are equal, we can check if they’re greater than or less than one another. We do this the way you might expect, by simply using the greater-than and less-than characters

we see the same principles applied with greater-than and less-
than. We can also use greater-than-or-equal-to and less-than-or-equal-to by adding an equals sign after the greater or less than sign
```
// 2_numeric_value_comparisons.go
package main

import "fmt"

func main() {
	fmt.Println(3 > 5)
	fmt.Println(3 < 5)
	fmt.Println(3 < 3)
	fmt.Println(3 <= 3)
	a := 7
	b := 9
	c := 9
	fmt.Println(a < b)
	fmt.Println(b > a)
	fmt.Println(c > b)
	fmt.Println(c >= b)
}

```
Output:
```
$ go run 2_numeric_value_comparisons.go 
false
true
false
true
true
true
false
true
```
### Non-Numeric Equality Comparisons

With numbers, it’s easy to look at relative value. It makes sense to ask, “Is 3 greater than 5?” It doesn’t make sense to ask, “Is blue greater than red?” With colors, names, and lots of other data types, there are no relative values. However, equality still exists in these areas. It doesn’t make sense to ask, “Is blue greater than red?”,but it does make sense to ask, “Is blue the same as red?”.

use the double-equals to mean equality among non-numeric data types. Most often, this will be strings.
```
//3_non_numeric_equality_comparisons.go
package main

import "fmt"

func main() {
	a := "Hello, world"
	b := "Hello, world"
	c := "Hello, "
	d := "world"
	fmt.Println(a == b)
	fmt.Println(a == c)
	fmt.Println(a == c+d)

}
```
Output:-
```
$ go run 3_non_numeric_equality_comparisons.go 
true
false
true
```
Whether or not the == operator works this way with the data types you’re using is dependent on a number of factors. Before relying on it, you should check to see if it operates as expected. The general point here is that for almost any data type, it
does make sense to check for equality.
```
//4_non_numeric_equality_comparisons.go
package main

import "fmt"

func main() {
	a := "Hello, world"
	b := "Hello, world"
	c := "Hello, "
	d := "world"
	fmt.Println(a > b)
	fmt.Println(a >= c)
	fmt.Println(a >= d)
}

```
Output:-
```
$ go run 4_nonnumeric_equality_comparisons.go 
false
true
false
```
It’s worth noting that the greater-than and less-than operators do work for strings as well, and they operate based on sorting the strings alphabetically. Strings that are earlier alphabetically are treated as “less” than strings that are later alphabetically

### String Compare
```
//6_string_compare.go
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Compare("A", "B"))             // A < B
	fmt.Println(strings.Compare("B", "A"))             // B > A
	fmt.Println(strings.Compare("Japan", "Australia")) // J > A
	fmt.Println(strings.Compare("Australia", "Japan")) // A < J
	fmt.Println(strings.Compare("Germany", "Germany")) // G == G
	fmt.Println(strings.Compare("Germany", "GERMANY")) // GERMANY > Germany
	fmt.Println(strings.Compare("", ""))
	fmt.Println(strings.Compare("", " ")) // Space is less
}
```
Output:
```
$ go run 6_string_compare.go 
-1
1
1
-1
0
1
0
-1
```