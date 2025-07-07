class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_position(self, index, data):
        """Insert a new node at the specified position (0-indexed)"""
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        if index == 0:
            self.prepend(data)
            return
        
        if index >= self.size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Traverse to the position before where we want to insert
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_position(self, index):
        """Delete the node at the specified position (0-indexed)"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of range. List size is {self.size}")
        
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        # If deleting the head node
        if index == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return deleted_data
        
        # Traverse to the node before the one to delete
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data
    
    def delete_by_value(self, value):
        """Delete the first occurrence of the specified value"""
        if not self.head:
            return False
        
        # If the head node contains the value
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value):
        """Find the index of the first occurrence of the value"""
        current = self.head
        index = 0
        
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        
        return -1  # Not found
    
    def get(self, index):
        """Get the value at the specified index"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of range. List size is {self.size}")
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.data
    
    def update(self, index, new_value):
        """Update the value at the specified index"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of range. List size is {self.size}")
        
        current = self.head
        for i in range(index):
            current = current.next
        
        old_value = current.data
        current.data = new_value
        return old_value
    
    def reverse(self):
        """Reverse the linked list in place"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def clear(self):
        """Remove all elements from the list"""
        self.head = None
        self.size = 0
    
    def to_list(self):
        """Convert linked list to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def from_list(self, python_list):
        """Create linked list from Python list"""
        self.clear()
        for item in python_list:
            self.append(item)
    
    # Different Display Methods
    
    def display(self):
        """Basic display method - prints each element"""
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()  # New line at the end
    
    def display_detailed(self):
        """Detailed display showing node addresses and connections"""
        if not self.head:
            print("List is empty")
            return
        
        print("Linked List Structure:")
        current = self.head
        index = 0
        
        while current:
            print(f"Node {index}:")
            print(f"  Data: {current.data}")
            print(f"  Address: {id(current)}")
            print(f"  Next: {id(current.next) if current.next else 'None'}")
            
            if current.next:
                print("  ↓")
            else:
                print("  ↓")
                print("None (End of list)")
            
            current = current.next
            index += 1
    
    def display_horizontal(self):
        """Display in horizontal format with boxes"""
        if not self.head:
            print("[ Empty List ]")
            return
        
        # Top border
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        
        # Calculate box width based on longest data
        max_width = max(len(node) for node in nodes)
        box_width = max(max_width + 2, 5)  # Minimum width of 5
        
        # Top border
        print("┌" + "─" * box_width + "┐", end="")
        for i in range(len(nodes) - 1):
            print("    ┌" + "─" * box_width + "┐", end="")
        print()
        
        # Data row
        for i, node in enumerate(nodes):
            data_str = str(node).center(box_width)
            print(f"│{data_str}│", end="")
            if i < len(nodes) - 1:
                print(" -> ", end="")
        print()
        
        # Bottom border
        print("└" + "─" * box_width + "┘", end="")
        for i in range(len(nodes) - 1):
            print("    └" + "─" * box_width + "┘", end="")
        print()
    
    def display_with_indices(self):
        """Display with index numbers"""
        if not self.head:
            print("List is empty")
            return
        
        print("Index: ", end="")
        current = self.head
        index = 0
        indices = []
        values = []
        
        while current:
            indices.append(f"[{index}]")
            values.append(str(current.data))
            current = current.next
            index += 1
        
        # Print indices
        for i, idx in enumerate(indices):
            print(f"{idx:>6}", end="")
            if i < len(indices) - 1:
                print("    ", end="")
        print()
        
        # Print values
        print("Value: ", end="")
        for i, val in enumerate(values):
            print(f"{val:>6}", end="")
            if i < len(values) - 1:
                print(" -> ", end="")
        print()
    
    def display_vertical(self):
        """Display in vertical format"""
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        index = 0
        
        print("HEAD")
        print("  ↓")
        
        while current:
            print(f"┌─────┐")
            print(f"│ {str(current.data):^3} │ (Index: {index})")
            print(f"└─────┘")
            
            if current.next:
                print("  ↓")
            else:
                print("  ↓")
                print("NULL")
            
            current = current.next
            index += 1
    
    def __str__(self):
        """String representation using arrow notation"""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
    
    def __repr__(self):
        return f"LinkedList({str(self)})"

def main():
    """Interactive main function to play with the LinkedList"""
    ll = LinkedList()
    
    print("🔗 Welcome to the Interactive Linked List Playground! 🔗")
    print("=" * 50)
    
    while True:
        print("\n📋 MENU OPTIONS:")
        print("1️⃣  Append element")
        print("2️⃣  Prepend element")
        print("3️⃣  Insert element at position")
        print("4️⃣  Delete element at position")
        print("5️⃣  Delete element by value")
        print("6️⃣  Find element index")
        print("7️⃣  Get element at index")
        print("8️⃣  Update element at index")
        print("9️⃣  Reverse list")
        print("🔟  Display (basic)")
        print("1️⃣1️⃣  Display detailed")
        print("1️⃣2️⃣  Display horizontal")
        print("1️⃣3️⃣  Display with indices")
        print("1️⃣4️⃣  Display vertical")
        print("1️⃣5️⃣  Show current size")
        print("1️⃣6️⃣  Clear list")
        print("1️⃣7️⃣  Demo with sample data")
        print("1️⃣8️⃣  Convert to Python list")
        print("1️⃣9️⃣  Create from Python list")
        print("0️⃣  Exit")
        print("-" * 40)
        
        try:
            choice = input("Enter your choice (0-19): ").strip()
            
            if choice == '1':
                data = input("Enter element to append: ")
                # Try to convert to int if possible, otherwise keep as string
                try:
                    data = int(data)
                except ValueError:
                    pass
                ll.append(data)
                print(f"✅ Added '{data}' to the end of the list")
                print(f"Current list: {ll}")
                
            elif choice == '2':
                data = input("Enter element to prepend: ")
                try:
                    data = int(data)
                except ValueError:
                    pass
                ll.prepend(data)
                print(f"✅ Added '{data}' to the beginning of the list")
                print(f"Current list: {ll}")
                
            elif choice == '3':
                index = int(input("Enter position to insert at (0-indexed): "))
                data = input("Enter element to insert: ")
                try:
                    data = int(data)
                except ValueError:
                    pass
                ll.insert_at_position(index, data)
                print(f"✅ Inserted '{data}' at position {index}")
                print(f"Current list: {ll}")
                
            elif choice == '4':
                index = int(input("Enter position to delete from (0-indexed): "))
                deleted_data = ll.delete_at_position(index)
                print(f"✅ Deleted element '{deleted_data}' at position {index}")
                print(f"Current list: {ll}")
                
            elif choice == '5':
                value = input("Enter value to delete: ")
                # Try to convert to int if possible, otherwise keep as string
                try:
                    value = int(value)
                except ValueError:
                    pass
                if ll.delete_by_value(value):
                    print(f"✅ Deleted element with value '{value}'")
                else:
                    print(f"❌ Value '{value}' not found in the list")
                print(f"Current list: {ll}")
                
            elif choice == '6':
                value = input("Enter value to find: ")
                try:
                    value = int(value)
                except ValueError:
                    pass
                index = ll.find(value)
                if index != -1:
                    print(f"✅ Value '{value}' found at index {index}")
                else:
                    print(f"❌ Value '{value}' not found in the list")
                
            elif choice == '7':
                index = int(input("Enter index to get value from: "))
                try:
                    value = ll.get(index)
                    print(f"Value at index {index} is: {value}")
                except IndexError as e:
                    print(f"❌ {e}")
                
            elif choice == '8':
                index = int(input("Enter index to update: "))
                new_value = input("Enter new value: ")
                try:
                    old_value = ll.update(index, new_value)
                    print(f"✅ Updated index {index} from {old_value} to {new_value}")
                except IndexError as e:
                    print(f"❌ {e}")
                
            elif choice == '9':
                ll.reverse()
                print("🔄 List reversed")
                print(f"Current list: {ll}")
                
            elif choice == '10':
                print("\n🔍 Basic Display:")
                ll.display()
                
            elif choice == '11':
                print("\n🔍 Detailed Display:")
                ll.display_detailed()
                
            elif choice == '12':
                print("\n🔍 Horizontal Display:")
                ll.display_horizontal()
                
            elif choice == '13':
                print("\n🔍 Display with Indices:")
                ll.display_with_indices()
                
            elif choice == '14':
                print("\n🔍 Vertical Display:")
                ll.display_vertical()
                
            elif choice == '15':
                print(f"\n📏 Current list size: {ll.size}")
                print(f"List contents: {ll}")
                
            elif choice == '16':
                ll = LinkedList()  # Create a new empty list
                print("🗑️ List cleared!")
                
            elif choice == '17':
                print("\n🎭 Loading demo data...")
                ll = LinkedList()  # Start fresh
                demo_data = [10, 20, 30, 40, 50]
                for item in demo_data:
                    ll.append(item)
                print(f"✅ Demo list created: {ll}")
                print("\nTry different display options to see how it looks!")
                
            elif choice == '18':
                python_list = ll.to_list()
                print(f"📋 Linked list as Python list: {python_list}")
                
            elif choice == '19':
                list_input = input("Enter elements separated by commas (e.g., 1,2,3): ")
                try:
                    python_list = [item.strip() for item in list_input.split(',')]
                    # Try to convert to numbers if possible
                    converted_list = []
                    for item in python_list:
                        try:
                            converted_list.append(int(item))
                        except ValueError:
                            try:
                                converted_list.append(float(item))
                            except ValueError:
                                converted_list.append(item)
                    ll.from_list(converted_list)
                    print(f"✅ Created linked list from: {converted_list}")
                    print(f"Current list: {ll}")
                except Exception as e:
                    print(f"❌ Error creating list: {e}")
                
            elif choice == '0':
                print("\n👋 Thanks for playing with the Linked List! Goodbye!")
                break
                
            else:
                print("❌ Invalid choice! Please enter a number between 0-19.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()