//12_user_input.go
package main

import "fmt"

func main() {
	fmt.Println("Enter an Integer: ")
	var myInt int
	fmt.Scanln(&myInt)
	fmt.Println("The Entered integer is: ", myInt)
}
