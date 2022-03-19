class Node:
   def __init__(self, value):
       self.value = value
       self.next = None
       
   def __str__(self):
        return  f"('value':{self.value}, 'next':{self.next})"

# Linked list implementation

class LinkedList:
  
    def __init__(self, value):
      # First value of the list
      self.head = Node(value)
      
      # Last item
      self.tail = self.head
      
      # length of the linked list
      self.length = 1
      
    def __str__(self):
      return self.head
      
    def append(self, value):
      # We create a new node dict with the properties
      newNode = Node(value)
      # The last item will be the new Node element
      self.tail.next = newNode
      self.tail = newNode
      self.length += 1
      return self
    
    def prepend(self, value):
      # We create a new node dict with the properties
      newNode = Node(value)
      newNode.next = self.head
      self.head = newNode
      self.length += 1
      return self
    
    def nodeTraversal(self, index):
      # We take the head element to travers into it
      prev_node = self.head
      for i in range(0, index-1):
        prev_node = prev_node.next
       
      return prev_node
      
    
    def insert(self, index, value):
      # If the index is out of range return error
      
      if index == 0:
        return self.prepend(value)
        
        
      elif index == self.length-1:
        return self.append(value)
      
      elif index > self.length:
        return IndexError(f'Index out of range it should be between 0 to {self.length-1}')
      
      # If the index is inside the length we create a new Node with the value
      new_node = Node(value)
      
      prev_node = self.nodeTraversal(index)
      
      
      # After the node is attached we insert the next value in the new node.
      new_node.next = prev_node.next
      prev_node.next = new_node
      
      self.length += 1
      return self
      
    def remove(self, index):
      # If index is out of bounds return error
      if index > self.length:
        return IndexError(f'Index out of range it should be between 0 to {self.length-1}')
      
      # If index is 0 then the head is removed and the next element is set as head
      if index == 0:
        self.head = self.head.next
        return self
      
      prev_node = self.nodeTraversal(index)
      
      

      if prev_node.next.next == None:
        self.tail = prev_node
        prev_node.next = None
        self.length -= 1
        return self
      
      
      next_node = prev_node.next.next
      prev_node.next = next_node
      self.length -= 1
      return self
         
      
      
    def printList(self):
      node = self.head
      values = []
      
      while node.next != None:
        values.append(node.value)
        node = node.next
      
      values.append(self.tail.value)
      print(values)
        
      
      
      
      
      
      
      

myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.printList()
myLinkedList.insert(2, 7)
myLinkedList.insert(0, 0)
myLinkedList.printList()
myLinkedList.remove(3)
myLinkedList.printList()
myLinkedList.remove(1)
myLinkedList.printList()
myLinkedList.remove(myLinkedList.length -1)

  
     
      
    
  