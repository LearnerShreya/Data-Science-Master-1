# import multiprocessing

# def producer(q):
#     for i in ["sudh", "kumar", "asdf"]:
#         q.put(i)

# def consume(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(item)

# if __name__ == '__main':
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer, args = (queue,))
#     m2 = multiprocessing.Process(target=consume, args = (queue,))
#     m1.start()
#     m2.start()
#     queue.put("sudh")
#     m1.join()
#     m2.join()



import multiprocessing

def producer(q):
    for i in ["sudh", "kumar", "asdf"]:
        q.put(i)  # Add items to the queue
    q.put(None)  # Add a sentinel to signal the consumer to stop

def consume(q):
    while True:
        item = q.get()  # Retrieve items from the queue
        if item is None:  # Check for sentinel
            break
        print(f"Consumed: {item}")  # Print the item

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # Create producer and consumer processes
    m1 = multiprocessing.Process(target=producer, args=(queue,))
    m2 = multiprocessing.Process(target=consume, args=(queue,))

    # Start the processes
    m1.start()
    m2.start()
    # queue.put("sudh")
    
    # Wait for the processes to finish
    m1.join()
    m2.join()
