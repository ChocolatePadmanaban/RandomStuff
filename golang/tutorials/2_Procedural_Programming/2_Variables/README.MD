# Variables

## What is a Variable?
Variables are possibly the most fundamental element of programming. There
really isn’t much you can do without variables. You’re probably familiar with vari-
ables from your days learning algebra. Variables aren’t really any different here.
A ­variable is a name that holds a value. The name stays the same while the value
can change. In algebra, that variable was often x.

### Examples of Variables
A variable is a name that holds some value. It’s like a question with an answer. The
question always exists, but the answer to the question might change. Let’s think of
some examples:

- How many kids do I have? The variable would be the count of David’s kids, and
the value would be one. That might change, though.
- What’s the current stock price of Microsoft? The variable would be Microsoft
stock price, and the current value would be 53.74.
- What color shirt am I wearing? The variable would be David’s shirt color, and
the current value would be blue.

Notice how in each case, there’s a variable and a value. The variable can take on
different values. Notice also how unlike in math, variables don’t have to represent
numbers. You could have variables that represent any number of things, such as
names, colors, and dates.

Variables are the heart of programming. Nearly everything we do involves
manipulating variables. We’ll use variables to represent the information in which
we’re interested, like stock prices or usernames. We’ll use variables to control how
our programs run, like counting repeated actions or checking if something has been
found.

## Variables in Go
```
//1_variables_in_go.go
package main

import "fmt"

func main() {
	x := 5
	fmt.Println(x)
}

```
Output
```
$ go run 1_variables_in_go.go 
5
$
```
### Different Kinds of Variables
Just as we talked about lots of different kinds of variables previously
```
//2_variabels_in_go.go
package main

import (
	"fmt"
	"time"
)

func main() {
	aNumber := -2
	aDecimal := 7.1
	aString := "Hello world"
	aBoolean := true
	aDate := time.Now()
	fmt.Println(aNumber)
	fmt.Println(aDecimal)
	fmt.Println(aString)
	fmt.Println(aBoolean)
	fmt.Println(aDate)
}

```
OutPut:
```
$ go run 2_variables_in_go.go 
-2
7.1
Hello world
true
2021-09-30 05:28:22.297022693 +0530 IST m=+0.000104275
$ 
```
Remember, we could have named these anything we wanted,
but we gave them names that made it clear what they are. Think of this like giving
names to a pet: you could name a cat “Fido” and a dog “Tiger,” but you wouldn’t
be surprised if these names confused people. The same way, you could name your
variables phineas, celery, and sovngarde, but these names wouldn’t tell the
reader anything about what they are.

### Naming Rules and Convention 

- Variable names can contain only letters, numbers, and underscores. No spaces
or special characters.
- Variable names must start with letters. Underscores are technically allowed, too,
but we usually only use these in certain situations.
- Variable names must not duplicate certain reserved words. We’ll talk about the
reserved keywords later.
When you violate these rules, you’ll usually get a syntax error
```
//3_naming_rules_and_conventions.go
package main
import "fmt"
func main() {
	my$variable :=5
	my variable := 5
	$variable := 5
	for := 5
}
```
Output:
```
$ go run 3_naming_rules_and_conventions.go 
# command-line-arguments
./3_naming_rules_and_conventions.go:5:4: invalid character U+0024 '$'
./3_naming_rules_and_conventions.go:5:5: syntax error: unexpected variable at end of statement
./3_naming_rules_and_conventions.go:6:5: syntax error: unexpected variable at end of statement
./3_naming_rules_and_conventions.go:7:2: invalid character U+0024 '$'
./3_naming_rules_and_conventions.go:8:6: syntax error: unexpected :=, expecting expression
./3_naming_rules_and_conventions.go:9:1: syntax error: unexpected }, expecting expression
$ 
```
