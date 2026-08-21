# Define sample data
text = "Python"
num_int = 42
num_float = 3.14159

# Define a fixed column width
width = 15

print("--- METHOD 1: Using Modern f-strings ---")
# < Left align, > Right align, ^ Center align

print(f"Left Aligned Text:   |{text:<{width}}|")
print(f"Right Aligned Text:  |{text:>{width}}|")
print(f"Centered Text:       |{text:^{width}}|")

print("\n--- Formatting Numbers ---")
# Right align an integer with space padding (Default for numbers)
print(f"Right Aligned Int:   |{num_int:>{width}}|")
# Zero-pad an integer to a fixed width
print(f"Zero-Padded Int:     |{num_int:0{width}}|")
# Format float with fixed width and 2 decimal places
print(f"Formatted Float:     |{num_float:>{width}.2f}|")

print("\n--- Custom Padding Characters ---")
# Place the fill character right before the alignment symbol
print(f"Dashed Center:       |{text:-^{width}}|")
print(f"Star Left Align:     |{text:*<{width}}|")

print("\n--- METHOD 2: Using String Methods ---")
# Alternative approach using built-in methods
print(f"Methods Left:        |{text.ljust(width)}|")
print(f"Methods Right:       |{text.rjust(width)}|")
print(f"Methods Center:      |{text.center(width, '_')}|")
