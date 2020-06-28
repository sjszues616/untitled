import threading
import time


class Item_bag():
    def __init__(self):
        self.bag = []

    def an_item_is_available(self):
        return True if self.bag else False

    def get_an_available_item(self):
        if self.an_item_is_available():
            self.bag.pop()
        else:
            return None

    def make_an_item_available(self):
        self.bag.append(1)


def thread_1():
    with cv:
        print('thread_1_start')
        while not item_bag.an_item_is_available():
            print('thread_1_start_wait')
            cv.wait()
            print('thread_1_start_wait_close')
        item_bag.get_an_available_item()


def thread_2():
    with cv:
        item_bag.make_an_item_available()
        print('thread_2')
        cv.notify()


if __name__ == '__main__':
    cv = threading.Condition()
    item_bag = Item_bag()
    thread_1 = threading.Thread(target=thread_1)
    thread_2 = threading.Thread(target=thread_2)
    thread_1.start()
    thread_2.start()