// 4_naming_rules_and_conventions.go
package main

import "fmt"

func main() {
	// Bad Variables
	a := 30
	foo := "David"
	qwerty := 10
	fmt.Println(a, foo, qwerty)
	// Good Variables
	var age int = 30
	var firstName string = "David"
	var catCount int = 10
	fmt.Println(age, firstName, catCount)
}
