//11_converting_from_string.go
package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func main() {
	var myIntAsString string = "5"
	myIntAsFloat, err := strconv.ParseFloat(myIntAsString, 64)
	// this will work
	if err == nil {
		fmt.Println(reflect.TypeOf(myIntAsFloat))
	}

	var myFloatAsString string = "5.1"
	myFloatAsInt, err := strconv.Atoi(myFloatAsString)
	// this will cause an error
	if err == nil {
		fmt.Println(reflect.TypeOf(myFloatAsInt))
	} else {
		fmt.Println(err)
	}
}
