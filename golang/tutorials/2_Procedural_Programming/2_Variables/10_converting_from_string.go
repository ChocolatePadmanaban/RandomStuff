//10_converting_from_string.go
package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func main() {
	var myIntAsString string = "5"
	myInt, err := strconv.Atoi(myIntAsString)
	if err == nil {
		fmt.Println(reflect.TypeOf(myInt))
	}

	var myFloatAsString string = "5.1"
	myFloat, err := strconv.ParseFloat(myFloatAsString, 64)
	if err == nil {
		fmt.Println(reflect.TypeOf(myFloat))
	}

	var myBoolAsString string = "true"
	myBool, err := strconv.ParseBool(myBoolAsString)
	if err == nil {
		fmt.Println(reflect.TypeOf(myBool))
	}
}
