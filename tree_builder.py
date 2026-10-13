class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
class TeamTree:
    def __init__(self):
        self.root = None
    def insert(self, manager_name, employee_name, side, current_node=None):
        # Start searching at the root.
        if current_node is None:
            current_node = self.root

        # The company must have a team lead first.
        if current_node is None:
            print("Error: Add a team lead first.")
            return False

        # Check whether this is the correct manager.
        if current_node.name == manager_name:
            side = side.lower()

            if side == "left":
                if current_node.left is not None:
                    print("Error: The left side is already occupied.")
                    return False
                current_node.left = EmployeeNode(employee_name)

            elif side == "right":
                if current_node.right is not None:
                    print("Error: The right side is already occupied.")
                    return False
                current_node.right = EmployeeNode(employee_name)

            else:
                print("Error: Side must be left or right.")
                return False

            return True

        # Search the left and right branches recursively.
        found = self._insert_search(
            current_node.left, manager_name, employee_name, side
        )
        if found:
            return True

        found = self._insert_search(
            current_node.right, manager_name, employee_name, side
        )
        if found:
            return True

        print(f"Error: Manager '{manager_name}' was not found.")
        return False

    def _insert_search(self, node, manager_name, employee_name, side):
        # Stop if this branch is empty.
        if node is None:
            return False

        # Insert if we found the manager.
        if node.name == manager_name:
            side = side.lower()

            if side == "left":
                if node.left is not None:
                    print("Error: The left side is already occupied.")
                    return False
                node.left = EmployeeNode(employee_name)

            elif side == "right":
                if node.right is not None:
                    print("Error: The right side is already occupied.")
                    return False
                node.right = EmployeeNode(employee_name)

            else:
                print("Error: Side must be left or right.")
                return False

            return True

        # Keep searching both branches.
        if self._insert_search(
            node.left, manager_name, employee_name, side
        ):
            return True

        return self._insert_search(
            node.right, manager_name, employee_name, side
        )
# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


    def print_tree(self, node=None, level=0):
        # Start at the root when called normally.
        if level == 0:
            node = self.root

        # Stop when a branch is empty.
        if node is None:
            return

        # Print the employee with indentation.
        print("  " * level + "- " + node.name)

        # Print the left and right branches.
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)
