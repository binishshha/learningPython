class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def is_empty(self):
        return self.front == -1

    def insert_front(self, value):
        if self.is_full():
            print("Deque is full ")
            return
        if self.is_empty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.deque[self.front] = value
        print(f"Inserted {value} at front.")

    def insert_rear(self, value):
        if self.is_full():
            print("Deque is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.deque[self.rear] = value
        print(f"Inserted {value} at rear.")

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return
        removed = self.deque[self.front]
        self.deque[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        print("Deleted from front:", removed)

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty ")
            return
        removed = self.deque[self.rear]
        self.deque[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        print("Deleted from rear:", removed)

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return
        i = self.front
        print("Deque elements:", end=" ")
        while True:
            print(self.deque[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

def main():
    size = int(input("Enter the size of the deque: "))
    dq = Deque(size)

    while True:
        print("\nOperations:")
        print("1. Insert Front")
        print("2. Insert Rear")
        print("3. Delete Front")
        print("4. Delete Rear")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            value = int(input("Enter value to insert at front: "))
            dq.insert_front(value)
        elif choice == '2':
            value = int(input("Enter value to insert at rear: "))
            dq.insert_rear(value)
        elif choice == '3':
            dq.delete_front()
        elif choice == '4':
            dq.delete_rear()
        elif choice == '5':
            dq.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter between 1 and 6.")


if __name__ == "__main__":
    main()