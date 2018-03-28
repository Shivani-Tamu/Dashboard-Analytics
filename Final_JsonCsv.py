import csv
import json
import collections

# Below set of code opens the input and output file and creates a writer object to write onto the file
infile = open("more_json_data.json", "r")
data_read = infile.read()
data_parsed = json.loads(data_read)
outfile = open("CSV_file.csv", "w", newline='') # parameter newline avoids the insertion of a line between each row in csv
writer = csv.writer(outfile)

# Initializations of flags, counters, list and default dictionaries
data_inside = collections.defaultdict(dict)
key_value = []
flag = 0
count1 = 0
count = 0

# Below code is to print the header
for row in data_parsed:
    if flag == 0:
        # this loop manages the json keys and excludes nested correlation (dictionary) column
        for x in row.keys():
            if x != 'correlation':
                if count == 0:
                    key_value.append(x)
            else:
                # This code drills down the correlation dictionary to print id, action and parentID headings/columns
                data_inside = (row['correlation'])
                for b in data_inside.keys():
                    if count1 == 0:
                        key_value.append(b)
        writer.writerow(key_value)
        key_value.clear() # clears rhe list key_value for fresh operation
    flag = 1
    count = 1
    count1 = 1
# After headers have been printed, below code prints the values within them
for row in data_parsed:
    for x in row.keys():
        if x != 'correlation':
            if count == 1:
                key_value.append(row[x])
        else:
            data_inside = (row['correlation'])
            for b in data_inside.keys():
                if count1 == 1:
                    key_value.append(data_inside[b])
    writer.writerow(key_value)
    key_value.clear()
outfile.close()