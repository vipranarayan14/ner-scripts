import csv
import sys

list_file_path = "list.csv"

list_file = open(list_file_path)
reader = csv.DictReader(list_file)

if len(sys.argv) < 2:
    print("Query required.")
    exit(1)

if len(sys.argv) < 3:
    print("Output file path required.")
    exit(1)

query = sys.argv[1]
out_file_path = sys.argv[2]

keywords = query.split("|")

print("Query: " + query)
print("Keywords: " + ", ".join(keywords))

results = []
total_rows = 0

for row in reader:
    total_rows += 1

    category = row["Catagory"]

    for keyword in keywords:
        if keyword in category:
            results.append(row)

with open(out_file_path, mode="w") as out_file:
    csv_writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(results)

print(f"Matches found: {len(results)} out of {total_rows}")
