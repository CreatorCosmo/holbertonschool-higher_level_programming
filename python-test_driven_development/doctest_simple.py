import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Assuming "0-add_integer.py" is located in the same directory as this script
add_integer_path = os.path.join(current_dir, "0-add_integer.py")

print("Path to add_integer.py:", add_integer_path)
