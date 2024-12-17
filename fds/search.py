'''

1)Write a Python program :
a) To store name and mobile number of your friend in sorted order.
b) Search friend name using Binary Search.
c) Insert new friend in phoneBook List.

2) Write a Python program:

a) To store name and mobile number of your friend in sorted order.
b) Search friend name using Fibonacci search..
c) Insert new friend in phoneBook List.

'''


class Friend:
	def __init__(self):
		name=None
		mobile=0
		
#Implementation class
class PhoneBook:
	def __init__(self):
		self.N=0	# Number of friend in Phone Book
		self.friendList=[]	# Friend in phoneBook
    
	#1. Read friend name and mobile number
	def getFriendDetails(self,nof):
		self.N=nof
		for i in range(self.N):
			friend=Friend()
			print("Enter friend name and mobile no.",i+1)
			name=input("Enter friend name:")
			mobile=int(input("Enter mobile number of the friend::"))
			friend.name=name
			friend.mobile=mobile
			self.friendList.append(friend)
        
	#2. Display Friend Detail
	def displayFriendList(self):
		print("\nThe Friend phonebook is")
		for i in range(self.N):
			print(self.friendList[i].name," ",self.friendList[i].mobile)
	
	
	#3. Search friend name using Binary Search
	def binarySearchNonrecursive(self,key):
		l=0
		u=self.N-1
		while(l<=u):
			mid=(l+u)//2
			if(key==self.friendList[mid].name):
				print("Name has found on location:",mid+1)
				break
			elif(key>self.friendList[mid].name):
				l=mid+1
			else:
				u=mid-1
	
	def binarySearchrecursive(self,l,u,key):
		if(l<=u):
		
			mid=(l+u)//2
			if(key==self.friendList[mid].name):
				print("Name has found on location:",mid+1)
			  
			elif(key>self.friendList[mid].name):
				return self.binarySearchrecursive(mid+1,u,key)
			else:
				return self.binarySearchrecursive(l,mid-1,key)
		else:
		    print("name not found!!")
	def fibonacci_search(self, key):
            size = len(self.friendList)
             
            start = -1
             
            f0 = 0
            f1 = 1
            f2 = 1
            while(f2 < size):
                f0 = f1
                f1 = f2
                f2 = f1 + f0
             
             
            while(f2 > 1):
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
                    return index
            if (f1) and (self.friendList[size - 1] == key):
                print("element found at index",index)
                return size - 1
            else:
                print("element not found")
            return None
	#sorting the list		
	def bubbleSort(self):
        	for i in range(self.N-1):
            		for j in range(0,self.N-i-1):
                		if self.friendList[j].name>self.friendList[j+1].name:
                    			temp=self.friendList[j]
                    			self.friendList[j]=self.friendList[j+1]
                    			self.friendList[j+1]=temp
        
#Driver Code
frn=PhoneBook()
choice=0

while(choice != 6):
    print("\n******FRIEND PHONEBOOK*****")
    print("1. Read friend name and mobile detail")
    print("2. Display Friend Detail")
    print("3. Search friend name using Binary Search")
    print("4. Search friend name using Fibonacci search")
    print("5. Insert new friend detail")
    print("6. Exit Application")
    choice=int(input("What operation::"))
    
    if (choice ==1):
        
        n=int(input("Enter number of friends::"))
        frn.getFriendDetails(n)
    elif (choice ==2):
        frn.displayFriendList()
    elif (choice ==3):
    	print("1.Search by Non Recursive:")
    	print("2.Search by Recursive:")
    	choice1=int(input("Enter the choice::"))
    	if(choice1==1):
    		name=input("Enter Name to be searched::")
    		frn.bubbleSort()
    		frn.binarySearchNonrecursive(name)
    	elif(choice1==2):
    		name=input("Enter Name to be searched::")
    		frn.bubbleSort()
    		frn.binarySearchrecursive(0,frn.N-1,name)
        	
    elif (choice ==4):
        key=input("enter the element you want to search::")
        frn.bubbleSort()
        n=frn.fibonacci_search(key) 
        if(n != None):
            print("No. found at location ",n)
    elif (choice ==5):
        pass
    elif (choice ==6):
        print("Good By")
        break
    else:
        print("Wrong Choice!!")
