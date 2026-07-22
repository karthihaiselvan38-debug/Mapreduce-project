import multiprocessing
import os

from mapper import mapper
from reducer import reducer
from partitioner import partition

NUMBER_OF_REDUCERS = 2


# -------------------------
# Mapper Process
# -------------------------
def mapper_worker(lines):
    """
    Runs inside one mapper process. Takes a chunk of lines,
    runs mapper() on each one, and collects all the resulting
    (word, 1) pairs into a single list.
    """
    result = []
    for line in lines:
        mapped_values = mapper(line)
        result.extend(mapped_values)
    return result


# -------------------------
# Partitioning
# -------------------------
def create_partitions(mapped_data):
    """
    Takes the full list of (key, value) pairs produced by all mappers,
    and routes each pair to the correct reducer's partition file,
    using partition() to decide the destination.

    Should end up writing files like:
        intermediate/partition_0.txt
        intermediate/partition_1.txt
    each containing lines of the form: "<key> <value>"
    """
    partitions = {}

    for key, value in mapped_data:
        reducer_id = partition(key, NUMBER_OF_REDUCERS)

        if reducer_id not in partitions:
            partitions[reducer_id] = []

        partitions[reducer_id].append((key, value))

    os.makedirs("intermediate", exist_ok=True)

    for reducer_id, data in partitions.items():
        filename = f"intermediate/partition_{reducer_id}.txt"
        with open(filename, "w") as file:
            for key, value in data:
                file.write(f"{key} {value}\n")


# -------------------------
# Reducer Process
# -------------------------
def reducer_worker(reducer_id):
    """
    Runs inside one reducer process. Reads its partition file,
    groups all values by key, then calls reducer() on each key
    to get the final aggregated result.
    """
    filename = f"intermediate/partition_{reducer_id}.txt"
    grouped = {}

    with open(filename) as file:
        for line in file:
            key, value = line.split()
            value = int(value)

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(value)

    output = []
    for key, values in grouped.items():
        output.append(reducer(key, values))

    return output


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    # Split input among mappers
    chunks = []
    size = 3
    for i in range(0, len(lines), size):
        chunks.append(lines[i:i + size])
    print("Input Split Completed")

    # Start Mapper Processes
    pool = multiprocessing.Pool(processes=len(chunks))
    mapper_results = pool.map(mapper_worker, chunks)
    pool.close()
    print("Mapper Completed")

    # Combine mapper outputs
    intermediate = []
    for result in mapper_results:
        intermediate.extend(result)
    print("Intermediate Data:")
    print(intermediate)

    # Partition
    create_partitions(intermediate)
    print("Partitioning Completed")

    # Start Reducers
    reducer_pool = multiprocessing.Pool(NUMBER_OF_REDUCERS)
    final_output = reducer_pool.map(reducer_worker, range(NUMBER_OF_REDUCERS))
    reducer_pool.close()

    print("\nFinal Output")
    for result in final_output:
        print(result)