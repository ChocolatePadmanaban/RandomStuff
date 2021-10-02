//2_variabels_in_go.go
package main

import (
	"fmt"
	"time"
)

func main() {
	var aNumber int = -2
	var aDecimal float64 = 7.1
	var aString string = "Hello world"
	var aBoolean bool = true
	var aDate time.Time = time.Now()
	fmt.Println(aNumber)
	fmt.Println(aDecimal)
	fmt.Println(aString)
	fmt.Println(aBoolean)
	fmt.Println(aDate)
}
