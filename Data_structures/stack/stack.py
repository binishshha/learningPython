class Stack:
    def __init__(self, size):
        self.top=-1
        self.size=size
        self.stack=[None]*size

    def push(self, items):
        if self.top==self.size-1:
            print('the stack is in overflow state')
        else:
            self.top +=1
            self.stack[self.top]=items
            print(f'{items} is pushed')

    def pop(self):
        if self.pop==-1:
            print('the stack is in underflow state')
        else:
            self.stack[self.top]=None
            self.top -= 1
            print(f'{self.stack[self.top]} is removed')

    def peek(self):
        if self.top==-1:
            print('the stack is in underflow state')
        else:
            print(f'{self.stack[self.top]} is at the top of the stack')

    def display(self):
        if self.top==-1:
            print('the stack is in underflow state')
        else:
            for i in range(self.top, -1, -1):
                print(f'{self.stack[i]}')

def main():
    size=int(input('enter the size of the stack:'))
    s=Stack(size)

    while True:
        print('Stack Operations!!')
        print('1. Push ')
        print('2. Pop')
        print('3. Peek')
        print('4. Display')

        choice= input('Enter the choice from the following set of operations:')

        if choice == '1':
             value= input('Enter the items to be pushed onto the stack:')
             s.push(value)
        elif choice =='2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            break
        else:
            print('invalud choice')

if __name__=='__main__':
    main()

