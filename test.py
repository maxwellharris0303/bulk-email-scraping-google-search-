# Function to split us_cities into chunks
def chunk_list(data, num_chunks):
    avg_chunk_size = len(data) // num_chunks
    chunks = [data[i * avg_chunk_size: (i + 1) * avg_chunk_size] for i in range(num_chunks)]
    remainder = len(data) % num_chunks

    # Distribute remainder elements among chunks
    for i in range(remainder):
        chunks[i].append(data[num_chunks * avg_chunk_size + i])

    return chunks

# Generate the cities_list with the specified number of chunks (equal to the number of threads)
cities_list = chunk_list(us_cities, thread_number)

# Verify the split by printing the cities_list
for i, sublist in enumerate(cities_list):
    print(f"Thread {i+1} will process: {sublist}")
