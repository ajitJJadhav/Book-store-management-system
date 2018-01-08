import os
import pickle

def createList():
	f = open("books.txt")
	
	L = []
	for i in f:
		L.append( i.strip().split(',') )
	
	for i in range( len(L) ):
		L[i][5] = int( L[i][5] )
		L[i][6] = float( L[i][6] )
		L[i][7] = int( L[i][7] )
		L[i][8] = int( L[i][8] )
		
	f.close()
	return L	


def updateStock(L):
	f = open("books.txt","w")

	for i in range( len(L) ):
		L[i][5] = str( L[i][5] )
		L[i][6] = str( L[i][6] )
		L[i][7] = str( L[i][7] )
		L[i][8] = str( L[i][8] )
	
	for i in L:
		f.write( ','.join(i) + '\n' )
	
		
	f.close()	
	
class admin:
   p=open("password.txt",'rb')
   password= pickle.loads( p.read() )
   p.close()
   def addToInventory(self,a,L):
       L.append(a.split(','))
       updateStock(L)
       # print(L)
       print("THE BOOK DETAILS ARE ADDED")

       
   def removeFromInventory(self,a,L):
        
        #print(L)
        flag=0
        for i in range(len(L)):
                if(L[i][8]==a):
                   del(L[i])
                   updateStock(L)
                   print("THE BOOK IS REMOVED FROM INVENTORY")
                   flag=1
                   break
        if(flag==0):
            print("ENTER A VALID BOOK CODE!!!!")      
       
       
   def modifyARecord(self,a,L):
           print("\n\t\t1)Change Price\n\t\t2)Change Discount\n\t\t3)Change Quantity")
           b=input()
           a=int(a)
           if(b=='1'):
              for i in range(len(L)):
                  if(L[i][8]==a):
                          L[i][5]=int(input())
                         # print(L[i])
           elif(b=='2'):
              for i in range(len(L)):
                  if(L[i][8]==a):
                          L[i][6]=float(input())
                         # print(L[i])
           elif(b=='3'):
              for i in range(len(L)):
                  if(L[i][8]==a):
                          L[i][7]=int(input())
                         # print(L[i])
           print("THE CHANGES ARE MADE")
           updateStock(L)
       
   
   def modifyPassword(self):
        print("Enter old password")
        if(self.password==input()):
           print("Enter New Password\n")
           self.password=input()
           p=open("password.txt","wb")
           p.write( pickle.dumps(self.password) )
           p.close()
           print("Password changed succesfully\n")
        else:
           print("Wrong Password....Aborting\n")
	
   def displayInventory(self,L):
       for i in L:
          print( "ISBN Code : " + str(i[0]),
					"Book Name : " +  str( i[1] ),
					"Author : " +  str( i[2] ),
					 "Publisher : " + str( i[3] ),
					  "Genre : " + str( i[4] ),
					  "Cost : " + str( i[5] ),
					  "Discounted Cost : " +str( i[5] - (i[5]/100 * i[6]) ),
					  "Book Code : " + str( i[8] ),sep="\n" ) 
			
        
          print()
	
	

x=admin()              #class variable with global scope
def adminLogin():
        print("Welcome Admin what will you like to do\n\t\t1)ADD TO INVENTORY\n\t\t2)REMOVE FROM INVENTORY\n\t\t3)MODIFY A RECORD\n\t\t4)CHANGE PASSWORD\n\t\t5)VIEW THE INVENTORY\n\t\t6)EXIT")
        choice=input()
        
       
        #print(L)
        while(choice!='6'):
         L=createList()
         if(choice=='1'):
                print("Enter the details of the book to be added\n")
                x.addToInventory(input(),L)
         elif(choice=='2'):
                print("Enter the code of the book to be deleted\n")
                #print(','.join(L))
                x.removeFromInventory(int(input()),L)
         elif(choice=='3'):
                print("Enter the code of the book to be modified\n")
                x.modifyARecord(input(),L)
         elif(choice=='4'):
                x.modifyPassword()
         elif(choice == '5'):
             x.displayInventory(L)
         
         else:
               exit() 
         choice=input("Enter any of the choices to continue(1-6) : ")



def check(paswrd,count):
    if(count==2):
        print("Credentials didn't match -----re-directing to Home page------\n")
        return;
    
    if(x.password==paswrd):
        print("successfull")
        adminLogin()
        
    else:
        print("Credentials do not match Re-enter   ",end='')
        print("TRIES REMAINING",2-count,sep=" ")
        paswrd=input()
        check(paswrd,count+1)

#customer
def customer_operations(L):
	os.system('clear')
	
	total_cost = 0
	customer = Customer()
	
	flag = 0
	L1 = [] #bought books list	
	while flag == 0:
		print("1 - Display, 2 - Add to Cart,3 - buy and pay")
		
		op1 = int( input() )
		
		os.system('clear')
		
		if op1 == 1:
			back1 = 0
			while back1 == 0:
				
				print("1 - Display All,2 - Book Name,3- Author,4 - Genre,5 - Back")
				display = int( input() )
				
				if display == 1:
					os.system('clear')
					customer.displayAll(L)
					
				elif display == 2:
					os.system('clear')
					customer.displayByBookName( L, input("Enter Name Of Book : ") )
					
				elif display == 3:
					os.system('clear')
					customer.displayByAuthor( L, input("Enter Name Of Author : ") )
					
				elif display == 4:
					os.system('clear')
					customer.displayByGenre( L, input("Enter Name Of Genre : ") )
				
				elif display == 5:
					os.system('clear')
					back1 = 1
					  		
		elif op1 == 2:
			op2 = 0
			while op2 == 0:
				bookCode = int( input("Enter the book code : ") )
				quantity = int( input("Enter quantity : ") )
				
				os.system('clear')
				
				total_cost += customer.addToCart(L,L1,bookCode,quantity)
				
				print("Your total cost is ",total_cost)
				op2 = ( int( input("1 - Buy more books,2 - go back : ") ) + 1 ) % 2
				
			os.system('clear')	
		
		elif op1 == 3:
			os.system('clear')			
			
			updateStock(L)
			customer.displayBill(L1)

			discount = 0
			print()
			x = int( input("1 - Special Discount,2 - continue to pay : ") )	 			
			if x == 1:
				coupon = input("Enter the special coupon code : ")
			
				f = open("coupons.txt")
				D = {}
				for i in f:
					i = i.strip().split()
					D[ i[0] ] = int( i[1] )
				f.close()
				
				if coupon in D:
					discount = D[coupon] 
				else:
					print(" no such coupon code exists ")
			
			#os.system('clear')
			
			total_cost -= total_cost/100*discount
			
			actual_cost = 0
			for i in L1:
				actual_cost += i[3]*i[-1]
			
			print()	
			print(' '*10+ "Your total bill is ",actual_cost)
			print() 
			flag = 1
		
	return total_cost
	

class Customer:
	def displayAll(self,L):
		for i in L:
			print( "ISBN Code : " + str(i[0]),
					"Book Name : " +  str( i[1] ),
					"Author : " +  str( i[2] ),
					 "Publisher : " + str( i[3] ),
					  "Genre : " + str( i[4] ),
					  "Cost : " + str( i[5] ),
					  "Discounted Cost : " +str( i[5] - (i[5]/100 * i[6]) ),
					  "Book Code : " + str( i[8] ),sep="\n" ) 
			
			print()
	
	def displayByBookName(self,L,name):
		flag = 0
		for i in L:
			if i[1] == name:
				flag = 1
				print( "ISBN Code : " + str(i[0]),
					"Book Name : " +  str( i[1] ),
					"Author : " +  str( i[2] ),
					 "Publisher : " + str( i[3] ),
					  "Genre : " + str( i[4] ),
					  "Cost : " + str( i[5] ),
					  "Discounted Cost : " +str( i[5] - (i[5]/100 * i[6]) ),
					  "Book Code : " + str( i[8] ),sep="\n" ) 
		print()
								
		if(flag == 0):
			print("\nNo Such Book Exists\n")
				
	def displayByAuthor(self,L,author):
		flag = 0
		for i in L:
			if i[2] == author:
				flag = 1
				print( "ISBN Code : " + str(i[0]),
					"Book Name : " +  str( i[1] ),
					"Author : " +  str( i[2] ),
					 "Publisher : " + str( i[3] ),
					  "Genre : " + str( i[4] ),
					  "Cost : " + str( i[5] ),
					  "Discounted Cost : " +str( i[5] - (i[5]/100 * i[6]) ),
					  "Book Code : " + str( i[8] ),sep="\n" ) 
			
				print()
		if(flag == 0):
			print("No Such Book Exists\n")				
	
	def displayByGenre(self,L,name):
		flag = 0
		for i in L:
			if i[4] == name:
				flag = 1
				print( "ISBN Code : " + str(i[0]),
					"Book Name : " +  str( i[1] ),
					"Author : " +  str( i[2] ),
					 "Publisher : " + str( i[3] ),
					  "Genre : " + str( i[4] ),
					  "Cost : " + str( i[5] ),
					  "Discounted Cost : " +str( i[5] - (i[5]/100 * i[6]) ),
					  "Book Code : " + str( i[8] ),sep="\n" ) 
			
				print()				
		if(flag == 0):
			print("No Such Book Exists\n")
				
						   
	def addToCart(self,L,L1,bookCode,quantity):
		cost = 0
		for i in range( len(L) ):
			#print(L[i][8])
			if L[i][8] == bookCode:
				if quantity > L[i][7]:
					print("only",L[i][7], "books are available" )
				
				else:
					L[i][7] -= quantity	
					L1.append( [ L[i][1],L[i][6],L[i][7],L[i][5],L[i][5] - L[i][5]/100 * L[i][6] ,quantity ] )
					cost = L1[-1][-2] * quantity
				break
				
		else:
			print("No such book with this code exists")		
		return cost	
			
	def displayBill(self,L):
		print( 	"Sr. no.\t" ,
					"Book Name" + ' '*(41),
					"Cost" + ' '*6,
					"Discounted cost\t",
					"Quantity")
	
		for i in range( len(L) ):	
			print( 	str(i) + ' '*( 7 - len( str(i) ) ) + '\t',
					L[i][0] + ' '*( 50 - len(L[i][0]) ),
					str(L[i][3]) + ' '*(10 - len( str(L[i][3] ) ) ),
					str(L[i][4]) + ' '*(15 - len( str(L[i][4]) ) ) + '\t' ,
					str(L[i][5]) + ' '*( 8 - len( str(L[i][5]) )  )  )		


#main 
choice='0'
total=-1
while(choice!='3'):
 print("Welcome\n\t\tEnter Your Choice\n\t\t\t1)Admin\n\t\t\t2)customer\n\t\t\t3)EXIT\n")
 choice=input()
 if(choice=='1'):
    print("admin\nPlease Enter Your Password\n")
    paswrd=input()
    check(paswrd,0)
 elif(choice=='2'):
    print("Customer")
    L = createList()
    total=customer_operations(L)
    print(' '*10 +  "Your discounted bill is ", total )
    print()
    
    exit()
 else:
    print("exiting")
    exit()
        
