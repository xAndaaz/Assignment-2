# Singly Linked List - Python Implementation

A clean and robust implementation of a singly linked list data structure using Object-Oriented Programming principles.

## 🚀 Features

- **Complete OOP Implementation** with Node and LinkedList classes
- **Core Operations**: Insert, Display, and Delete with 1-based indexing
- **Robust Exception Handling** for edge cases and invalid operations
- **Interactive Testing** with user input validation
- **Mixed Data Types Support** (strings, integers, etc.)

## 📋 Requirements

- Python 3.x
- No external dependencies required

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/singly-linked-list-python.git
cd singly-linked-list-python
```

2. Run the program:
```bash
python linked_list.py
```

## 💻 Usage

### Basic Operations

```python
from linked_list import LinkedList

# Create a new linked list
my_list = LinkedList()

# Add elements to the end
my_list.insert("First")
my_list.insert(42)
my_list.insert("Last")

# Display the list
my_list.display()
# Output: First -> 42 -> Last -> None

# Delete element at position 2 (1-based indexing)
my_list.delete_n(2)
my_list.display()
# Output: First -> Last -> None
```

### Error Handling

The implementation handles common edge cases:

- **Empty List Deletion**: Prevents deletion from empty lists
- **Out of Range Access**: Validates position bounds
- **Invalid Input**: Handles non-integer input gracefully

## 📚 Learning Objectives

This implementation demonstrates:
- Object-Oriented Programming principles
- Data structure implementation from scratch
- Exception handling best practices
- User input validation
- Clean code organization
