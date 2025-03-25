import concurrent.futures
import time
import random
import logging
from queue import Queue

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class PrescriptionProcessor:
    def __init__(self, max_workers=5, max_retries=3):
        self.max_workers = max_workers
        self.max_retries = max_retries
        self.task_queue = Queue()
    
    def process_prescription(self, prescription_id):
        """Simulates processing a prescription request with a random failure."""
        for attempt in range(1, self.max_retries + 1):
            try:
                # Simulate a 30% chance of failure
                if random.random() < 0.3:
                    raise Exception(f"Failed processing {prescription_id}")
                logging.info(f"Successfully processed prescription {prescription_id}")
                return True
            except Exception as e:
                logging.warning(f"Retry {attempt}/{self.max_retries} for {prescription_id} due to {e}")
                time.sleep(0.5)  # Simple backoff
        
        logging.error(f"Prescription {prescription_id} failed after {self.max_retries} retries")
        return False

    def worker(self):
        """Worker function that processes tasks from the queue."""
        while not self.task_queue.empty():
            prescription_id = self.task_queue.get()
            self.process_prescription(prescription_id)
            self.task_queue.task_done()

    def start_processing(self, prescriptions):
        """Starts the worker pool and distributes jobs."""
        for p in prescriptions:
            self.task_queue.put(p)

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.worker) for _ in range(self.max_workers)]
            concurrent.futures.wait(futures)


def process_prescription(prescription_id):
    try:
        # Simulating failure probability
        if random.random() < 0.2:
            raise Exception(f"Error processing {prescription_id}")
        print(f"Processed prescription {prescription_id}")
    except Exception as e:
        print(f"Retrying {prescription_id} due to: {e}")
        time.sleep(1)  # Simple backoff
        process_prescription(prescription_id)


def main():
    begin = time.time()
    prescriptions = [f"RX-{i}" for i in range(10)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_prescription, prescriptions)
    end = time.time()
    print(f"Total time taken: {end - begin} seconds")


def main_v2():
    begin = time.time()
    prescriptions = [f"RX-{i:03d}" for i in range(10)]
    for prescription in prescriptions:
        process_prescription(prescription)
    end = time.time()
    print(f"Total time taken: {end - begin} seconds")


if __name__ == "__main__":
    # Seed random generator
    # random.seed(time.time())

    # # Sample prescriptions
    # prescriptions = [f"RX-{i:03d}" for i in range(10)]

    # # Create processor and start workers
    # processor = PrescriptionProcessor(max_workers=5, max_retries=3)
    # processor.start_processing(prescriptions)
    main_v2()
