package main
import (
	"fmt"
)
func main(){
	n := 1 == 1
	m := 2 == 1
	fmt.Printf("Value and type of n %v, %T \n", n, n)
	fmt.Printf("Value and tyoe of m %v, %T \n", m, m)
	// Zero value initialization 
	var z bool
	fmt.Printf("Zero value initiasation will initialize the value by default  %v , %T \n", z,z)
	var unsigned_int uint = 42
	fmt.Printf("Value and type of unsigned_int %v, %T \n", unsigned_int, unsigned_int)	
	a := 10
	b := 3
	fmt.Printf("Addition of a and b : %v \n", a + b)
	fmt.Printf("Subraction of a by b : %v \n", a-b )
	fmt.Printf("Multiplication of a and b : %v \n", a*b)
	fmt.Printf("Division of a by b : %v \n", a/b)
	fmt.Printf("Remainder Division of a by b : %v \n", a%b)
	fmt.Printf("Note: operations between different variable types will result in error \n")
	var c int  = 10
	var d int8  = 3
	fmt.Printf("We have to do type convertion to add two variables of different types: %v \n", c +int(d))
	fmt.Printf("Binary AND of a and b : %v \n", a & b) // 1010 AND 0011 = 0010 = 2
	fmt.Printf("Binary OR of a and b : %v \n", a | b) // 1010 OR 0010 = 1011 = 11
	fmt.Printf("Binary XOR of a and b : %v \n", a ^ b) // 1010 XOR 0011 = 1001 = 9
	fmt.Printf("Binary ANDNOT of a and b : %v \n", a &^ b)// 1010 ANDNOT 0011 = 0100 = 8
	a=a-2//=8
	fmt.Printf("Bit shifting left 3 places: %v \n ", a << 3)
	fmt.Printf("Bit shifting right 3 places: %v \n", a >> 3)
	n1:= 3.14
	n1=13.7e72
	n1=2.1E14
	fmt.Printf("Printing Value of n though re assiging three times: %v Type: %T \n", n1 , n1)

}

