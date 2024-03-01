package main

import (
	"fmt"
	"sync"
)

func sendData(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 5; i++ {
		fmt.Println("Sending:", i)
		ch <- i // Send data to the channel
	}
	close(ch) // Close the channel after sending all data
}

func receiveData(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		// Receive data from the channel
		data, ok := <-ch
		if !ok {
			// Channel is closed
			fmt.Println("Channel closed. Exiting.")
			return
		}
		fmt.Println("Received:", data)
	}
}

func main() {
	// Create a channel for communication
	dataChannel := make(chan int)

	// Create a WaitGroup to wait for Goroutines to finish
	var wg sync.WaitGroup

	// Set the number of Goroutines to wait for
	wg.Add(2)

	// Launch Goroutines for sending and receiving data
	go sendData(dataChannel, &wg)
	go receiveData(dataChannel, &wg)

	// Wait for all Goroutines to finish
	wg.Wait()
}
