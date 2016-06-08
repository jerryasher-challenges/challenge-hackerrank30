package main

import "fmt"

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n int
	fmt.Scanf("%d", &n)
	// var line string
	var name string
	var num int
	var phonebook = make(map[string]int)
	for l := 0; l < n; l++ {
		fmt.Scanf("%s", &name)
		fmt.Scanf("%d", &num)
		phonebook[name] = num
	}

	for {
		var query string
		_, err := fmt.Scanf("%s", &query)
		if err != nil {
			break
		}

		num, ok := phonebook[query]
		if ok {
			fmt.Printf("%s=%d\n", query, num)
		} else {
			fmt.Printf("Not found\n")
		}

	}
}
