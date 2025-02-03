import multiprocessing

def producer(q):
    print("Producer started")
    for i in range(10):
        q.put(i)
        print(f"Produced: {i}")
    q.put(None)  # Add a sentinel to signal the consumer to stop
    print("Producer finished")

def consume(q):
    print("Consumer started")
    while True:
        item = q.get()  # Retrieve items from the queue
        if item is None:  # Check for sentinel
            print("Consumer received sentinel, stopping")
            break
        print(f"Consumed: {item}")

if __name__ == '__main__':
    print("Main program started")
    queue = multiprocessing.Queue()
    m1 = multiprocessing.Process(target=producer, args=(queue,))
    m2 = multiprocessing.Process(target=consume, args=(queue,))

    m1.start()
    m2.start()

    m1.join()
    m2.join()
    print("Main program finished")
