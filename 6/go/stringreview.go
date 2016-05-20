package main

import "fmt"

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n int
	fmt.Scanf("%d", &n)

	for l := 0; l < n; l++ {
		var s string
		fmt.Scanf("%s", &s)

		var even, odd string
		var counter int
		for _, r := range s {
			if counter%2 == 0 {
				even += string(r)
			} else {
				odd += string(r)
			}
			counter++
		}
		fmt.Printf("%s %s\n", even, odd)
	}
}
