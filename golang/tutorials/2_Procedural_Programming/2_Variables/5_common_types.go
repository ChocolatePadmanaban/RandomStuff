//5_common_types.go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var myInteger int = 5
	//first of the three methods to determine type
	fmt.Printf("%T \n", myInteger)
	var myFloat float64 = 5.0
	//second method to determine type
	fmt.Println(reflect.TypeOf(myFloat))
	var myString string = "5.0"
	fmt.Println(reflect.ValueOf(myString).Kind())
	var myBoolean bool = true
	fmt.Println(reflect.ValueOf(myBoolean).Kind())
}
