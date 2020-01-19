package main

import (
	"fmt"
	"time"
)

func decorator(f func(s string)) func(string) {
	return func(s string) {
		fmt.Println("before")
		f(s)
		fmt.Println("after")
	}
}

func benchmark(f func(s string)) func(string) {
	return func(s string) {
		start := time.Now()
		f(s)
		fmt.Printf("benchmark: %v\n", time.Since(start))
	}
}

func printString(s string) {
	fmt.Println(s)
}

func main() {
	// benchmark(printString)("hello")
	// decorator(printString)("hello")
	// decorator(benchmark(printString))("hello")
}
