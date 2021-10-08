package main

import (
	"fmt"
	"reflect"
	"time"
)

func main() {
	var myDate = time.Now()
	var myDateAsString string = myDate.String()
	fmt.Println(reflect.TypeOf(myDateAsString), myDateAsString)
}
