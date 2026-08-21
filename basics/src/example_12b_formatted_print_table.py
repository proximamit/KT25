def create_table(headers, data):
    def format_value(value):
        if isinstance(value, float):
            return f"{value:,.2f}"
        return str(value)

    # Calculate column widths based on the ACTUAL displayed values
    col_widths = []

    for i, header in enumerate(headers):
        max_len = len(str(header))

        for row in data:
            value = format_value(row[i])
            max_len = max(max_len, len(value))

        # 2 spaces for padding: one on each side
        col_widths.append(max_len + 2)

    # Unicode Box-drawing characters
    top_left, top_mid, top_right = "┌", "┬", "┐"
    mid_left, mid_mid, mid_right = "├", "┼", "┤"
    bot_left, bot_mid, bot_right = "└", "┴", "┘"
    horiz, vert = "─", "│"

    def make_border(left, mid, right):
        return left + mid.join(
            horiz * width for width in col_widths
        ) + right

    # Top border
    print(make_border(top_left, top_mid, top_right))

    # Header
    header_cells = []

    for i, header in enumerate(headers):
        cell = f" {str(header):^{col_widths[i] - 2}} "
        header_cells.append(cell)

    print(vert + vert.join(header_cells) + vert)

    # Header separator
    print(make_border(mid_left, mid_mid, mid_right))

    # Data rows
    for row in data:
        row_cells = []

        for i, value in enumerate(row):
            value_str = format_value(value)

            if isinstance(value, (int, float)):
                # Right-align numbers
                cell = f" {value_str:>{col_widths[i] - 2}} "
            else:
                # Left-align text
                cell = f" {value_str:<{col_widths[i] - 2}} "

            row_cells.append(cell)

        print(vert + vert.join(row_cells) + vert)

    # Bottom border
    print(make_border(bot_left, bot_mid, bot_right))


# Example
if __name__ == "__main__":
    table_headers = ["ID", "Employee Name", "Department", "Salary"]

    table_data = [
        (101, "Alice Smith", "Engineering", 75000.50),
        (102, "Bob Jones", "Marketing", 62000.00),
        (103, "Charlie Brown", "HR", 54500.75),
        (104, "Diana Prince", "R&D", 115000.00)
    ]

    create_table(table_headers, table_data)