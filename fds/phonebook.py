# Friend class to store name and mobile
class Friend:
    def __init__(self):
        self.name = None
        self.mobile = 0


# Implementation class for PhoneBook
class PhoneBook:
    def __init__(self):
        self.N = 0  # Number of friends in Phone Book
        self.friendList = []  # List of friends in phonebook
    
    # 1. Read friend name and mobile number
    def getFriendDetails(self, nof):
        self.N = nof
        for i in range(self.N):
            friend = Friend()
            print("Enter friend name and mobile no.", i + 1)
            name = input("Enter friend name: ")
            mobile = int(input("Enter mobile number of the friend: "))
            friend.name = name
            friend.mobile = mobile
            self.friendList.append(friend)

    # 2. Display Friend Detail
    def displayFriendList(self):
        print("\nThe Friend phonebook is:")
        for i in range(self.N):
            print(self.friendList[i].name, " ", self.friendList[i].mobile)

    # 3. Search friend name using Binary Search (Non-Recursive)
    def binarySearchNonrecursive(self, key):
        l = 0
        u = self.N - 1
        while l <= u:
            mid = (l + u) // 2
            if key == self.friendList[mid].name:
                print("Name found at location:", mid + 1)
                return mid
            elif key > self.friendList[mid].name:
                l = mid + 1
            else:
                u = mid - 1
        print("Name not found!")
        return None

    # 3. Search friend name using Binary Search (Recursive)
    def binarySearchRecursive(self, l, u, key):
        if l <= u:
            mid = (l + u) // 2
            if key == self.friendList[mid].name:
                print("Name found at location:", mid + 1)
                return mid
            elif key > self.friendList[mid].name:
                return self.binarySearchRecursive(mid + 1, u, key)
            else:
                return self.binarySearchRecursive(l, mid - 1, key)
        else:
            print("Name not found!")
            return None

    # 4. Search friend name using Fibonacci Search
    def fibonacci_search(self, key):
        size = len(self.friendList)
        f0 = 0
        f1 = 1
        f2 = f1 + f0

        while f2 < size:
            f0 = f1
            f1 = f2
            f2 = f1 + f0

        start = -1
        while f2 > 1:
            index = min(start + f0, size - 1)
            if self.friendList[index].name < key:
                f2 = f1
                f1 = f0
                f0 = f2 - f1
                start = index
            elif self.friendList[index].name > key:
                f2 = f0
                f1 = f1 - f0
                f0 = f2 - f1
            else:
                print("Element found at index", index)
                return index

        if f1 and self.friendList[start + 1].name == key:
            print("Element found at index", start + 1)
            return start + 1

        print("Element not found")
        return None

    # Sorting the list using Bubble Sort
    def bubbleSort(self):
        for i in range(self.N - 1):
            for j in range(0, self.N - i - 1):
                if self.friendList[j].name > self.friendList[j + 1].name:
                    # Swap the two friends
                    self.friendList[j], self.friendList[j + 1] = self.friendList[j + 1], self.friendList[j]

    # Insert a new friend and maintain sorted order
    def insertFriend(self, friend):
        self.friendList.append(friend)
        self.N += 1
        self.bubbleSort()


# Driver Code
frn = PhoneBook()
choice = 0

while choice != 6:
    print("\n*FRIEND PHONEBOOK*")
    print("1. Read friend name and mobile detail")
    print("2. Display Friend Detail")
    print("3. Search friend name using Binary Search")
    print("4. Search friend name using Fibonacci search")
    print("5. Insert new friend detail")
    print("6. Exit Application")
    
    choice = int(input("What operation: "))

    if choice == 1:
        n = int(input("Enter number of friends: "))
        frn.getFriendDetails(n)
        frn.bubbleSort()  # Sorting the list after input

    elif choice == 2:
        frn.displayFriendList()

    elif choice == 3:
        print("1. Search by Non-Recursive")
        print("2. Search by Recursive")
        choice1 = int(input("Enter the choice: "))
        
        if choice1 == 1:
            name = input("Enter Name to be searched: ")
            frn.binarySearchNonrecursive(name)
        elif choice1 == 2:
            name = input("Enter Name to be searched: ")
            frn.binarySearchRecursive(0, frn.N - 1, name)

    elif choice == 4:
        key = input("Enter the element you want to search: ")
        frn.fibonacci_search(key)

    elif choice == 5:
        name = input("Enter new friend's name: ")
        mobile = int(input("Enter new friend's mobile number: "))
        new_friend = Friend()
        new_friend.name = name
        new_friend.mobile = mobile
        frn.insertFriend(new_friend)

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Wrong Choice!")






