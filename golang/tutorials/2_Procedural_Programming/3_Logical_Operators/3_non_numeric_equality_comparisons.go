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
