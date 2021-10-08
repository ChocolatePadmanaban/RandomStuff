// 7_converting_to_strings.go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var myNumber int = 5
	fmt.Printf("%T \n", myNumber)
	var myNumberAsString string = string(myNumber)
	fmt.Println(reflect.TypeOf(myNumberAsString))
}
