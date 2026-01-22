🔹 What is a CSV File?

CSV (Comma Separated Values) is a plain text file format used to store tabular data.

Each line represents a row

Values are separated by commas

Easily readable by humans and machines

Supported by Excel, databases, and programming languages

Example:

id,name,age
1,Manas,22
2,Amit,24

🔹 Why Use CSV in Python?

CSV files are commonly used because they are:

Lightweight and fast

Easy to read and write

Platform independent

Ideal for data exchange

Common Use Cases

Machine Learning datasets

ADAS sensor data logging

User data storage

Reports and analytics

Data migration between systems

🔹 CSV Handling in Python

Python provides a built-in csv module, so no extra installation is required.

Commonly Used Functions

csv.reader()

csv.writer()

csv.DictReader()

csv.DictWriter()

🔹 Reading a CSV File
csv.reader()

Reads CSV data row by row.

Key Points:

Open file in read (r) mode

Each row is returned as a list

Use newline='' to avoid blank lines

🔹 Writing to a CSV File
csv.writer()

Writes data into CSV format.

Key Points:

Open file in write (w) or append (a) mode

writerow() → single row

writerows() → multiple rows

Best when column order is fixed

🔹 Reading CSV as Dictionary
csv.DictReader()

Reads each row as a dictionary.

Advantages:

Column names act as keys

Cleaner and more readable

Easy data access

Example Output:

{'id': '1', 'name': 'Manas', 'age': '22'}

🔹 Writing CSV Using Dictionary
csv.DictWriter()

Writes CSV data using dictionaries.

Steps:

Define column headers using fieldnames

Call writeheader()

Write rows using dictionaries

🔹 Appending Data to CSV

Use append mode (a)

Existing data is preserved

New rows are added at the end

Useful for:

Real-time logging

Sensor data collection

Application logs

🔹 Handling Large CSV Files

Best Practices:

Read data line-by-line

Avoid loading full file into memory

Use generators where possible

Process data in chunks
