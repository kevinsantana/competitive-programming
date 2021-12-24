package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	var chess string
	var a int
	var d int

	fmt.Scanln(&n)
	fmt.Scanln(&chess)

	for _, char := range strings.ToUpper(chess) {
		s := string(char)
		if s == "A" {
			a++
		} else if s == "D" {
			d++
		}

	}

	if a > d {
		fmt.Println("Anton")
	} else if d > a {
		fmt.Println("Danik")
	} else {
		fmt.Println("Friendship")
	}

}
