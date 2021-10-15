//13_user_input.go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println("Enter an Integer: ")
	var myInt int
	fmt.Scanln(&myInt)
	fmt.Println("The Type of the variable entered before is: ", reflect.TypeOf(myInt))

	fmt.Println("Enter a Float: ")
	var myFloat float64
	fmt.Scanln(&myFloat)
	fmt.Println("The Type of the variable entered before is: ", reflect.TypeOf(myFloat))

	fmt.Println("Enter a string: ")
	var myString string
	fmt.Scanln(&myString)
	fmt.Println("The Type of the variable entered before is: ", reflect.TypeOf(myString))
}
