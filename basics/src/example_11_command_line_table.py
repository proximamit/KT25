# a simple Python script that prints a command-line table with borders:


def print_table(headers, rows):
    # Calculate the width of each column
    widths = [
        max(len(str(headers[i])), *(len(str(row[i])) for row in rows))
        for i in range(len(headers))
    ]

    # Border
    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    # Header
    header = "| " + " | ".join(
        str(headers[i]).ljust(widths[i])
        for i in range(len(headers))
    ) + " |"

    print(border)
    print(header)
    print(border)

    # Rows
    for row in rows:
        print("| " + " | ".join(
            str(row[i]).ljust(widths[i])
            for i in range(len(headers))
        ) + " |")

    print(border)


# Example
headers = ["Name", "Age", "City"]

rows = [
    ["Alice", 25, "London"],
    ["Bob", 30, "New York"],
    ["Charlie", 22, "Tokyo"],
]

print_table(headers, rows)


## Output:

"""
+---------+-----+----------+
| Name    | Age | City     |
+---------+-----+----------+
| Alice   | 25  | London   |
| Bob     | 30  | New York |
| Charlie | 22  | Tokyo    |
+---------+-----+----------+

"""
