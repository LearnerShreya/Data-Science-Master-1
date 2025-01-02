# import multiprocessing

# def producer(q):
#     for i in range(10):
#         q.put(i)  # Add numbers to the queue
#     q.put(None)  # Add a sentinel to signal the consumer to stop

# def consume(q):
#     while True:
#         item = q.get()  # Retrieve items from the queue
#         if item is None:  # Check for sentinel
#             break
#         print(f"Consumed: {item}")  # Print the item

# if __name__ == '__main':
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer, args = (queue,))
#     m2 = multiprocessing.Process(target=consume, args = (queue,))
#     m1.start()
#     m2.start()
#     # queue.put("sudh")
#     m1.join()
#     m2.join()



import multiprocessing

def producer(q):
    for i in range(10):
        q.put(i)  # Add numbers to the queue
    # q.put("sudh")  # Add "sudh" after all numbers
    q.put(None)  # Add a sentinel to signal the consumer to stop

def consume(q):
    while True:
        item = q.get()  # Retrieve items from the queue
        if item is None:  # Check for sentinel
            break
        print(f"Consumed: {item}")  # Print the item

if __name__ == '__main__':
    # Create a shared queue
    queue = multiprocessing.Queue()

    # Create producer and consumer processes
    m1 = multiprocessing.Process(target=producer, args=(queue,))
    m2 = multiprocessing.Process(target=consume, args=(queue,))

    # Start the processes
    m1.start()
    m2.start()

    queue.put("sudh")
    # Wait for the processes to finish
    m1.join()
    m2.join()
