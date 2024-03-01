package main

import (
	"fmt"
	"sync"
)

var mutex sync.Mutex // Create a global mutex

func criticalSection(id int) {
	mutex.Lock()         // Acquire the lock
	defer mutex.Unlock() // Release the lock when done (even if panic occurs)

	fmt.Printf("Process %d is in the critical section.\n", id)
	// Perform critical section operations here
}

func main() {
	const numProcesses = 5

	var wg sync.WaitGroup
	wg.Add(numProcesses)

	for i := 0; i < numProcesses; i++ {
		go func(id int) {
			defer wg.Done()
			criticalSection(id)
		}(i)
	}

	wg.Wait()
}
