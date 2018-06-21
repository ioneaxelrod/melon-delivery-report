def read_melon_report(filename):
    """ Prints count, name, and dollar amount of melon deliveries
    :param filename: string
    :return: None
    """
    # Open file
    the_file = open(filename)
    # Iterate through every line in the file, split, and convert into individual strings
    for line in the_file:
        line = line.rstrip()
        words = line.split("|")

        melon = words[0]
        count = words[1]
        amount = words[2]

        # Print info about deliveries
        print("Delivered {} {}s for total of ${}".format(count, melon, amount))
    the_file.close()

# Display the three days of reports
print("Day 1")
print()
read_melon_report("um-deliveries-20140519.txt")
print()

print("Day 2")
print()
read_melon_report("um-deliveries-20140520.txt")
print()

print("Day 3")
print()
read_melon_report("um-deliveries-20140521.txt")
print()
