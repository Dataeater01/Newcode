import csv

# Open the filter log file for reading
with open('filter.log', 'r') as log_file:

    # Create a list to store the modified data
    modified_data = []

    # Loop through each line in the filter log file
    for line in log_file:

        # Modify the data as required using string manipulation or regular expressions
        modified_line = line.replace('ERROR', 'WARNING')

        # Append the modified data to the list
        modified_data.append(modified_line)

    # Close the filter log file
    log_file.close()

# Open a new CSV file for writing
with open('modified_log.csv', 'w', newline='') as csv_file:

    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the modified data to the CSV file
    for line in modified_data:
        csv_writer.writerow([line])

    # Close the CSV file
    csv_file.close()
