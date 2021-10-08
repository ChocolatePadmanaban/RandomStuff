// 7_logical_operators.go
package main

import "fmt"

func main() {
	// Creates myNum1 with value 1
	myNum1 := 1
	// Creates myNum2 with value 2
	myNum2 := 2
	// Creates myNum3 with value 3
	myNum3 := 3
	// Prints True if 2 is between 1 and 3,
	// False otherwise
	fmt.Println(2 > 1 && 2 < 3)
	// Prints True if myNum2 is between myNum1 and myNum3
	// False otherwise
	fmt.Println(myNum2 > myNum1 && myNum2 < myNum3)

}
