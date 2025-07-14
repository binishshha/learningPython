class Linearqueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f'{item} is enqueued')

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Underflow")
        else:
            removed = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print(f'{removed} is dequeued')

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Underflow")
        else:
            for i in range(self.front, self.rear + 1):
                element = self.queue[i]
                print(f'{element} is displayed')

    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Underflow")
        else:
            element = self.queue[self.front]
            print(f'{element} is at the front')

def main():
    size = int(input('Enter the size of the queue: '))
    q = Linearqueue(size)

    while True:
        print('\nQueue Operations!!')
        print('1. Enqueue')
        print('2. Dequeue')
        print('3. Peek')
        print('4. Display')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            value = input('Enter the item to enqueue into the queue: ')
            q.enqueue(value)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.display()
        elif choice == '5':
            print('Exiting program.')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
