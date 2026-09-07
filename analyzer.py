f = open("log.txt", "r")
lines = f.readlines()

counts = {}

for line in lines:
    if "Failed" in line:
        parts = line.split()
        ip = parts[3]
        counts[ip] = counts.get(ip, 0) + 1
        print(counts)

THRESHOLD = 3

for ip, count in counts.items():
    if count >= THRESHOLD:
        print("alert : Bruce force susepected", ip)
    else:
        print("Ok", ip, "-only", count, "faliures(s), igrone")
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse="True")
print("\n===TRIAGEQUEUE===")
for ip, count in sorted_counts:
    print(ip, "→", count, "failed logins")
