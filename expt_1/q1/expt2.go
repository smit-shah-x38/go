package main

import (
	"fmt"
	"sync"
)

// displayString is a function to display a string six times.
func displayString(str string, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 0; i < 6; i++ {
		fmt.Println(str)
	}
}

// displayNumbers is a function to display numbers from start to end.
func displayNumbers(start, end int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := start; i <= end; i++ {
		fmt.Println(i)
	}
}

func main() {
	// Create a WaitGroup to wait for all Goroutines to finish.
	var wg sync.WaitGroup

	// Set the number of Goroutines to wait for.
	wg.Add(2)

	// Launch Goroutines to display string and numbers concurrently.
	go displayString("Hello, Go!", &wg)
	go displayNumbers(1, 5, &wg)

	// Wait for all Goroutines to finish.
	wg.Wait()
}
