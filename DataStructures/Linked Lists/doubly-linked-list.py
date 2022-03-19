class Node:
   def __init__(self, value):
       self.value = value
       self.next = None
       self.prev = None
       
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
      
      
    def append(self, value):
      # We create a new node dict with the properties
      newNode = Node(value)
      # The last item will be the new Node element
      self.tail.next = newNode
      prev_node = self.tail
      self.tail = newNode
      self.tail.prev = prev_node
      self.length += 1
      return self
    
    def prepend(self, value):
      # We create a new node dict with the properties
      newNode = Node(value)
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
      self.length += 1
      return self
    

    def nodeTraversal(self, index):
      # We take the head element to travers into it
      if index >= self.length:
        raise IndexError("Index out of bounds!")
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
      
      elif index >= self.length:
        raise IndexError(f'Index out of range it should be between 0 to {self.length-1}')
      
      # If the index is inside the length we create a new Node with the value
      new_node = Node(value)
      
      prev_node = self.nodeTraversal(index)
      
      
      # After the node is attached we insert the next value in the new node.
      new_node.next = prev_node.next
      new_node.prev = prev_node
      prev_node.next.prev = new_node
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
        self.head.prev = None
        return self
      
      prev_node = self.nodeTraversal(index)
      
      

      if prev_node.next.next == None:
        self.tail = prev_node
        prev_node.next = None
        self.length -= 1
        return self
      
      
      next_node = prev_node.next.next
      prev_node.next = next_node
      next_node.prev = prev_node.prev
      self.length -= 1
      return self
    
    # TODO REVERSE DOUBLY LINKED LIST
    def reverse(self):
      node = self.head
      while node.prev != None:
        next = node.next
        prev = node.prev
        node.next = prev
        node.prev = next
        print(node, node.prev)
        node = node.prev
        
        
      tail = self.tail
      head = self.head
      self.tail = head
      self.head = tail
        
        
         
      
      
    def nodes(self):
      node = self.head
      values = []
      
      while node.next != None:
        values.append(node)
        node = node.next
        
      
      values.append(self.tail)
      return values
    
    def printList(self):
      values = []
      for node in self.nodes():
        values.append(node.value)
        
      print(values)
        
      
      
      
      
      
      
      

myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(7)
myLinkedList.insert(1, 8)
myLinkedList.prepend(1)
myLinkedList.remove(2)
print("Original List:")
myLinkedList.printList()
myLinkedList.reverse()
print("Reversed:")
myLinkedList.printList()


  
     
      
    
  