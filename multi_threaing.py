from concurrent.futures import ThreadPoolExecutor
import threading
from time import sleep
import time
from colorama import Fore, Style, init
import questionary
import sys
import os
import subprocess
import multi_main

# Initialize a lock for the critical section
lock = threading.Lock()
account_lock = threading.Lock()


def concurrent_run_instances(count_instances, cities_list, index_list):
    def perform_task(cities, index):
        multi_main.run(cities, index)

    with ThreadPoolExecutor(max_workers=count_instances) as executor:
        executor.map(perform_task, cities_list, index_list)

# Initialize colorama
init()

thread_number = int(input("Please enter a number of thread: "))
print("You entered the number:", thread_number)


def chunk_list(data, num_chunks):
    avg_chunk_size = len(data) // num_chunks
    chunks = [data[i * avg_chunk_size: (i + 1) * avg_chunk_size] for i in range(num_chunks)]
    remainder = len(data) % num_chunks

    # Distribute remainder elements among chunks
    for i in range(remainder):
        chunks[i].append(data[num_chunks * avg_chunk_size + i])

    return chunks

with open("us_cities.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
us_cities = [line.strip().replace(" ", "+") for line in lines]

cities_list = chunk_list(us_cities, thread_number)
# for i, sublist in enumerate(cities_list):
#     print(f"Thread {i+1} will process: {sublist}")

index_list = []
index = 1
for _ in range(thread_number):
    index_list.append(index)
    index += 1

concurrent_run_instances(thread_number, cities_list, index_list)