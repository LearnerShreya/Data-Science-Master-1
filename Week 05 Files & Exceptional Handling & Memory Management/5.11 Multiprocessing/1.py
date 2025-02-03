
import multiprocessing

def test():
    print("This is my multiprocessing program")

if __name__ == '__main__':
    m = multiprocessing.Process(target=test)
    print("This is my main program")
    m.start()
    m.join()

# test()
