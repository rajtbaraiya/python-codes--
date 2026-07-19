log = "py, PY,excel, py , ,SQL,excel,PY"

parts = log.split(",")
print(parts)

counts = {}
for code in parts:
    code = code.strip()       
    if code == "":            
        continue
    code = code.upper()       
    counts[code] = counts.get(code, 0) + 1

most_frequent = max(counts, key=counts.get)

print(counts, "| Most frequent:", most_frequent)