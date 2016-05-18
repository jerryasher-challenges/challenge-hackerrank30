package main

import "fmt"

type person struct {
	age int
}

func (p person) NewPerson(initialAge int) person {
	//Add some more code to run some checks on initialAge
	if initialAge < 0 {
		fmt.Println("Age is not valid, setting age to 0.")
		p.age = 0
	} else {
		p.age = initialAge
	}
	return p
}

func (p person) amIOld() {
	//Do some computation in here and print out the correct statement to the console

	var statement string
	if p.age < 13 {
		statement = "You are young."
	} else if p.age < 18 {
		statement = "You are a teenager."
	} else {
		statement = "You are old."
	}
	// Write code determining if this person's age is old and print the correct statement:
	fmt.Println(statement)

}

func (p person) yearPasses() person {
	//Increment the age of the person in here
	p.age++

	return p
}

func main() {
	var T, age int

	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		fmt.Scan(&age)
		p := person{age: age}
		p = p.NewPerson(age)
		p.amIOld()
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		p.amIOld()
		fmt.Println()
	}
}
