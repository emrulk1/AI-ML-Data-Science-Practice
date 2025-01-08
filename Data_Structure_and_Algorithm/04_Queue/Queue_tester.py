from Queue import Queue

if __name__ == '__main__':

    q=Queue()

    val = 4
    q.enqueue(val)
    print("enqueued {} in Queue".format(val))
    print("Size of the Queue after adding {} : ".format(val), q.size(), end = "\n\n")

    val = True
    q.enqueue(val)
    print("enqueued {} in Queue".format(val))
    print("Size of the Queue after adding {} : ".format(val), q.size(), end = "\n\n")


    val = q.dequeue()
    print("Dequeued {} from Queue".format(val))
    print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")

    val = q.dequeue()
    print("Dequeued {} from Queue".format(val))
    print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")

    #safe way to remove from Queue
    try :
        val = q.dequeue()
        print("Dequeued {} from Queue".format(val))
        print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")
    except:
        print("Failed to dequeue because Queue is empty!")