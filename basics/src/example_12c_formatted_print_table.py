def create_table(headers, data):
    def format_value(value):
        if isinstance(value, float):
            return f"{value:,.2f}"
        return str(value)

    # Calculate column widths based on displayed values
    col_widths = []

    for i, header in enumerate(headers):
        max_len = len(str(header))

        for row in data:
            value = format_value(row[i])
            max_len = max(max_len, len(value))

        col_widths.append(max_len + 2)

    # ─────────────────────────────────────────────
    # Border characters
    # ─────────────────────────────────────────────

    # Double outer border
    top_left = "╔"
    top_mid = "╤"
    top_right = "╗"

    bot_left = "╚"
    bot_mid = "╧"
    bot_right = "╝"

    outer_vert = "║"
    outer_horiz = "═"

    # Single internal/header border
    mid_left = "╟"
    mid_mid = "┼"
    mid_right = "╢"

    inner_horiz = "─"
    inner_vert = "│"

    # ─────────────────────────────────────────────
    # Top border
    # ─────────────────────────────────────────────

    def make_top_border():
        return (
            top_left
            + top_mid.join(outer_horiz * width for width in col_widths)
            + top_right
        )

    # ─────────────────────────────────────────────
    # Header separator
    # ─────────────────────────────────────────────

    def make_middle_border():
        return (
            mid_left
            + mid_mid.join(inner_horiz * width for width in col_widths)
            + mid_right
        )

    # ─────────────────────────────────────────────
    # Bottom border
    # ─────────────────────────────────────────────

    def make_bottom_border():
        return (
            bot_left
            + bot_mid.join(outer_horiz * width for width in col_widths)
            + bot_right
        )

    # Top border
    print(make_top_border())

    # Header
    header_cells = []

    for i, header in enumerate(headers):
        cell = f" {str(header):^{col_widths[i] - 2}} "
        header_cells.append(cell)

    print(
        outer_vert
        + inner_vert.join(header_cells)
        + outer_vert
    )

    # Header separator
    print(make_middle_border())

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

        print(
            outer_vert
            + inner_vert.join(row_cells)
            + outer_vert
        )

    # Bottom border
    print(make_bottom_border())


# Example
if __name__ == "__main__":
    table_headers = [
        "ID",
        "Employee Name",
        "Department",
        "Salary"
    ]

    table_data = [
        (101, "Alice Smith", "Engineering", 75000.50),
        (102, "Bob Jones", "Marketing", 62000.00),
        (103, "Charlie Brown", "HR", 54500.75),
        (104, "Diana Prince", "R&D", 115000.00)
    ]

    create_table(table_headers, table_data)