# Custom function to insert nodes into a sorted list (priority queue)
def insert_sorted(queue, node):
    """Insert node into queue while maintaining sorted order based on frequency."""
    queue.append(node)
    
    # Manual sorting based on frequency
    for i in range(len(queue) - 1, 0, -1):
        if queue[i]["freq"] < queue[i - 1]["freq"]:
            queue[i], queue[i - 1] = queue[i - 1], queue[i]
        else:
            break

# Function to build the Huffman tree using dictionaries
def build_huffman_tree(frequencies):
    priority_queue = []  # Initialize empty priority queue
    for char, freq in frequencies:
        node = {"char": char, "freq": freq, "left": None, "right": None}
        priority_queue.append(node)  # Append each character node

    # Sort initially based on frequency
    priority_queue.sort(key=lambda x: x["freq"])

    while len(priority_queue) > 1:
        left = priority_queue.pop(0)  # Remove first (lowest frequency)
        right = priority_queue.pop(0) # Remove second (next lowest frequency)

        # Create new internal node as a dictionary
        merged = {"char": None, "freq": left["freq"] + right["freq"], "left": left, "right": right}

        # Insert back into priority queue while maintaining order
        insert_sorted(priority_queue, merged)

    return priority_queue[0]  # Root node

# Function to generate Huffman codes
def generate_codes(node, prefix="", huffman_codes={}):
    if node is not None:
        if node["char"] is not None:  # Leaf node
            huffman_codes[node["char"]] = prefix
        generate_codes(node["left"], prefix + "0", huffman_codes)
        generate_codes(node["right"], prefix + "1", huffman_codes)
    return huffman_codes

# Given character frequencies
frequencies = [('A', 5), ('B', 3), ('C', 2)]
root = build_huffman_tree(frequencies)
huffman_codes = generate_codes(root)

# Print Huffman codes
print("Huffman Codes:", huffman_codes)
