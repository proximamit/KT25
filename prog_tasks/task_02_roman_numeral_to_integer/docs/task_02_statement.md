# Roman numeral to Integer conversion

Given a Roman numeral, convert it to an Integer

Roman numerals are represented by seven different symbols:   
I, V, X, L, C, D and M.

| Symbol      | Value |
| ----------- | ----- |
|I            | 1     |
|V            | 5     |
|X            | 10    |
|L            | 50    |
|C            | 100   |
|D            | 500   |
|M            | 1000  |

There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9
- X can be placed before L (50) and C (100) to make 40 and 90
- C can be placed before D (500) and M (1000) to make 400 and 900

### Validating Roman Numerals

Roman numeral parser should:

- Validate the numeral strictly before conversion
- Reject invalid repetitions (VV, IIII)
- Reject invalid subtractive patterns (IIX, VX, IC)
- Provide clear exceptions/messages
- Be testable and maintainable
- Support standard Roman numeral rules (typically 1–3999)

