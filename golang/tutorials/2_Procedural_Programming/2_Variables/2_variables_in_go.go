//2_variabels_in_go.go
package main

import (
	"fmt"
	"time"
)

func main() {
	aNumber := -2
	aDecimal := 7.1
	aString := "Hello world"
	aBoolean := true
	aDate := time.Now()
	fmt.Println(aNumber)
	fmt.Println(aDecimal)
	fmt.Println(aString)
	fmt.Println(aBoolean)
	fmt.Println(aDate)
}
