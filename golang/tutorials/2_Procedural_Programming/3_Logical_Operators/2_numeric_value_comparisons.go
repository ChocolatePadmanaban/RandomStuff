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
