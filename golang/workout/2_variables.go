package main

import ( 
	"fmt"
	// "strconv" 
)

var outsidemain bool = true

var i int = 23

//upper case variable exposes variable to outside world 

func main()  {
	// var i int = 42
	// i = 42
	// i = 27
	fmt.Println("%v, %T", i,i)
	i := 42
	fmt.Println("%v, %T", i,i)
	fmt.Printf(" %v, %T", i, i)
	fmt.Printf("Hello World\n")
	var j float32 
	j = 27
	fmt.Printf("Printing j %v and it Type %T \n", j, j)
	k := 42.
	fmt.Printf("Printing k %v and it Type %T \n", k, k)
	j= 33
	fmt.Printf("Printing j %v and it Type %T \n", j, j)
	fmt.Printf("Printing outsidemain %v and its Type %T \n", outsidemain, outsidemain)
	var theURL string = "wwww.google.com" // acronyms are all upper case 
	fmt.Println(theURL)
	// conversion 
	j = float32(i)
	fmt.Printf("Printing j %v and it Type %T \n", j, j)
	// j = strconv.Itoa(i)
	// fmt.Printf("Printing j %v and it Type %T \n", j, j)
	// from float to int may cause error 

}