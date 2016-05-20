package main

import "fmt"

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n int
	fmt.Scanf("%d", &n)
	// var line string
	var slice = make([]int, n)

	for l := 0; l < n; l++ {
		fmt.Scanf("%d", &slice[l])
	}

	for l := n - 1; l >= 0; l-- {
		fmt.Printf("%d ", slice[l])
	}
	fmt.Printf("\n")
}
