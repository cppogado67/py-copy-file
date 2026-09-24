def copy_file(command):
    # 1. Split the command to get source and destination
    parts = command.split()
    source = parts[1]
    dest = parts[2]
    
    # 2. Check if they're the same
    if source == dest:
        return
    
    # 3. Copy the content
    with open(source, "r") as f1, open(dest, "w") as f2:
        f2.write(f1.read())
