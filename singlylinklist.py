class Node:
  def __init__(self,x):
    self.data=x
    self.nextt=None
class SLL:
  def __init__(self):
    self.head=None
  def insertAtBeg(self):
    val=int(input("enter a value to insert"))
    NewNode=Node (val)
    NewNode.next=self.head
    self.head=NewNode
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data)
      temp=temp.next 
Sl1=SLL()
ch=0
while ch!=4:
  print("1.Insertion at beg 2.del at beg 3.display 4.search")
  ch=int(input())
  if ch==1:
    Sl1.insertAtBeg()
    Sl1.display()
  elif ch==3:
    Sl1.display()
  else:
    print("invalid choice")  


