// 6_mixing_types.go
package main

import "fmt"

func main() {
	var myNumber1 int = 5
	var myNumber2 int = 3
	//var myString string = "Hello world"
	var myFloat float64 = 5.1
	fmt.Println(myNumber1 * myNumber2)
	fmt.Println(myFloat * float64(myNumber2))
	//fmt.Println(myNumber1 * myString)

}
