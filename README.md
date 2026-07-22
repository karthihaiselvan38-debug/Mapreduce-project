# MapReduce Engine

## Project Overview

This project is a Python implementation of a simple MapReduce Engine. It demonstrates how large datasets can be processed efficiently by dividing the work into multiple stages: splitting, mapping, partitioning, sorting, and reducing.

The engine processes an input text file containing programming language names and calculates the frequency of each language using the MapReduce workflow.

---

## Objective

The objective of this project is to:

- Split a large input file into smaller chunks.
- Execute multiple mapper processes in parallel.
- Generate intermediate key-value pairs.
- Partition data using hash partitioning.
- Sort intermediate data.
- Aggregate the values using reducer processes.
- Produce the final word count.

---

## Input Dataset

The input file (`input.txt`) contains the following data:

```
python java python
java c++ python
c++ javascript python
html java javascript
c++ python java
html html c++
python javascript python
java c++ html
javascript java python
python c++
```

---

## MapReduce Workflow

### Step 1 – Splitting

The input file is divided into smaller chunks and assigned to multiple mapper processes.

### Step 2 – Mapping

Each mapper reads its assigned data and emits a key-value pair for every word.

Example:

```
python java python
```

Mapper Output:

```
python 1
java 1
python 1
```

### Step 3 – Partitioning

The partitioner assigns each key to a reducer using:

```
hash(key) % number_of_reducers
```

This ensures that all occurrences of the same word are processed by the same reducer.

### Step 4 – Sorting

Each partition is sorted so identical keys appear together.

### Step 5 – Reducing

The reducer sums all values for each key.

Example:

```
python 1
python 1
python 1
```

Output:

```
python 3
```

---

## Expected Output

For the given input dataset, the final output is:

```
python 10
java 6
c++ 6
javascript 4
html 4
```

---

## Project Structure

```
MapReduce/
│
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── input.txt
├── partitions/
└── output/
```

---

## Technologies Used

- Python 3
- File Handling
- Multiprocessing
- Hash Partitioning
- Sorting

---

## How to Run

1. Place the dataset in `input.txt`.
2. Open the project folder in VS Code.
3. Run the project:

```
python master.py
```

4. The final output will be generated in the output directory.

---

## Features

- Parallel data processing
- Automatic file splitting
- Intermediate key-value generation
- Hash-based partitioning
- Sorting before reducing
- Final word count generation
- Modular Python implementation

---

## Learning Outcomes

After completing this project, you will understand:

- MapReduce Programming Model
- Parallel Processing
- Data Splitting
- Mapping
- Hash Partitioning
- Sorting
- Reducing
- Word Count using MapReduce

---

## Conclusion

This project demonstrates the complete MapReduce pipeline using a programming language dataset. It shows how large datasets can be processed efficiently by splitting the work across multiple mapper and reducer processes. The implementation provides a clear understanding of the core concepts behind distributed data processing systems such as Apache Hadoop.

---

## Author

**Karthihai Selvan**

BCA - computer application

kamaraj College (face prep)

