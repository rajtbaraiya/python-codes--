invoices = ['RE2026', 'R12026', 'REX206', 'RE20A6', 'RE12345']

for invoice in invoices:

    if len(invoice) != 6:
        print(invoice, "wrong length")
        continue

    letters = invoice[:2]
    digits = invoice[2:]

    if not letters.isalpha():
        print(invoice, "letters part wrong")

    elif not digits.isdigit():
        print(invoice, "digits part wrong")