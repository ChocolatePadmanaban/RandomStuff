// 10_code_block_comments.go
package main

import "fmt"

//Count function
//Prints the number from 1 to i
//On a single line
func countdown(i int) {
	for j := 1; j < i+1; j++ {
		fmt.Printf("%d ", j)
	}
	fmt.Println()
}

func main() {
	countdown(10)
	countdown(5)
	countdown(2)
}
