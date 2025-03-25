// Problem Statement: High-Throughput Prescription Processing
// You need to design a highly concurrent prescription processing system in Golang. Given a list of prescription requests, your system should:

// Process requests concurrently using Goroutines.
// Retry failed requests up to 3 times before logging an error.
// Use a worker pool to limit concurrency to 5 workers.
// Ensure thread safety while logging results.

package main

import (
	"fmt"
	"log"
	"math/rand"
	"sync"
	"time"
)

type Prescription struct {
	ID string
}

const maxRetries = 3
const workerCount = 5

func ProcessPrescription(p Prescription) error {
	if rand.Float32() < 0.3 {
		return fmt.Errorf("failed to process prescription %s", p.ID)
	}
	fmt.Printf("processed prescription %s\n", p.ID)
	return nil
}

func worker(id int, jobs <-chan Prescription, wg *sync.WaitGroup, logMutex *sync.Mutex) {
	defer wg.Done()

	for p := range jobs {
		attempts := 0
		for attempts < maxRetries {
			err := ProcessPrescription(p)
			if err == nil {
				break
			}
			attempts++
			time.Sleep(time.Millisecond * 500)
		}

		if attempts == maxRetries {
			logMutex.Lock()
			log.Printf("Prescription %s failed after %d attempts\n", p.ID, maxRetries)
			logMutex.Unlock()
		}
	}
}

func StartProcessing(prescriptions []Prescription) {
	jobs := make(chan Prescription, len(prescriptions))
	var wg sync.WaitGroup
	var logMutex sync.Mutex

	for i := 0; i < workerCount; i++ {
		wg.Add(1)
		go worker(i, jobs, &wg, &logMutex)
	}

	for _, p:= range prescriptions {
		jobs <- p
	}
	close(jobs)

	wg.Wait()
}

func main() {
	rand.Seed(time.Now().UnixNano())

	prescriptions := []Prescription{
		{"RX-001"}, {"RX-002"}, {"RX-003"}, {"RX-004"},
		{"RX-005"}, {"RX-006"}, {"RX-007"}, {"RX-008"},
		{"RX-009"}, {"RX-010"},
	}

	StartProcessing(prescriptions)
}
