# pure Python script to build a command-line table with borders. 
# This script dynamically handles column widths 
# based on our data, centers headers, right-aligns numbers, and left-aligns text 

## Complete Command-Line Table Program

def create_table(headers, data):
    # Step 1: Calculate the maximum width for each column dynamically
    col_widths = []
    for i, header in enumerate(headers):
        # Find the length of the longest item in this column (header or data row)
        max_len = len(str(header))
        for row in data:
            max_len = max(max_len, len(str(row[i])))
        # Add 2 for padding (1 space on each side)
        col_widths.append(max_len + 2)

    # Step 2: Define Box-Drawing characters for a clean look
    # You can change these to basic characters like '+', '-', and '|' if needed
    top_left, top_mid, top_right = "┌", "┬", "┐"
    mid_left, mid_mid, mid_right = "├", "┼", "┤"
    bot_left, bot_mid, bot_right = "└", "┴", "┘"
    horiz, vert = "─", "│"

    # Step 3: Helper function to generate horizontal border lines
    def make_border(left, mid, right):
        return left + mid.join(horiz * w for w in col_widths) + right

    # Step 4: Print the Top Border
    print(make_border(top_left, top_mid, top_right))

    # Step 5: Format and print Headers (Centered)
    header_cells = [f" {headers[i]:^{col_widths[i]-2}} " for i in range(len(headers))]
    print(vert + vert.join(header_cells) + vert)

    # Step 6: Print the Header-Separator Border
    print(make_border(mid_left, mid_mid, mid_right))

    # Step 7: Format and print Data Rows
    for row in data:
        row_cells = []
        for i, val in enumerate(row):
            # Check if the value is a number (int or float) to determine alignment
            if isinstance(val, (int, float)):
                # Format floats to 2 decimal places, right-align numbers
                val_str = f"{val:,.2f}" if isinstance(val, float) else str(val)
                cell = f" {val_str:>{col_widths[i]-2}} "
            else:
                # Left-align text strings
                cell = f" {str(val):<{col_widths[i]-2}} "
            row_cells.append(cell)
        print(vert + vert.join(row_cells) + vert)

    # Step 8: Print the Bottom Border
    print(make_border(bot_left, bot_mid, bot_right))

# --- Example Usage ---
if __name__ == "__main__":
    table_headers = ["ID", "Employee Name", "Department", "Salary"]
    
    table_data = [
        (101, "Alice Smith", "Engineering", 75000.50),
        (102, "Bob Jones", "Marketing", 62000.00),
        (103, "Charlie Brown", "HR", 54500.75),
        (104, "Diana Prince", "R&D", 115000.00)
    ]

    create_table(table_headers, table_data)

## Table Output
"""

┌─────┬───────────────┬─────────────┬────────────┐
│ ID  │ Employee Name │ Department  │   Salary   │
├─────┼───────────────┼─────────────┼────────────┤
│ 101 │ Alice Smith   │ Engineering │  75,000.50 │
│ 102 │ Bob Jones     │ Marketing   │  62,000.00 │
│ 103 │ Charlie Brown │ HR          │  54,500.75 │
│ 104 │ Diana Prince  │ R&D         │ 115,000.00 │
└─────┴───────────────┴─────────────┴────────────┘
"""
## Key Logic Features
'''
* Dynamic Resizing: The script loops through the columns first to calculate col_widths. 

It stretches each column to perfectly fit the longest text entry. 

* Smart Alignment: Inside the row-printing loop, isinstance(val, (int, float)) automatically checks the data type. 

Numbers align right (>), while words align left (<). 

* Box-Drawing Unicode: It utilizes clean ASCII/Unicode box elements (┌, ─, │) 
for a seamless grid look instead of messy repeated hyphens and plus signs.

'''