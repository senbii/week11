email_count = 0

with open("mbox.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith('From '):
            words = line.split()
            if len(words) > 1:
                email_address = words[1]
                print(email_address)
                email_count += 1

print(email_count)
