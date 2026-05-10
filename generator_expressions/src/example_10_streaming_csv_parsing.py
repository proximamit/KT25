rows = [
    "1,Alice,5000",
    "2,Bob,7000",
    "3,Eve,6500"
]

salaries = (
    int(row.split(",")[2])
    for row in rows
)

print(sum(salaries))
