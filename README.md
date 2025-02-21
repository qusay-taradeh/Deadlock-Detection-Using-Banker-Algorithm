# Deadlock Detection Using Banker Algorithm
 
A system that detects deadlocks in a system with N processes and M resources.

# Summary
Implementation of a system to detect deadlock conditions in a system with N processes and M resources. The system reads input from CSV files representing the allocation matrix, request matrix, and available vector. It then checks the dimensions, detects deadlock conditions, and outputs the results.

# Specifications
This application should be able to perform the following tasks:
1. Read the input files: `Allocation.csv`, `Request.csv`, and `Available.csv`. The user should provide the names of the input files.
2. Check the validity of the dimensions of the matrices (either valid or not).
3. Detect whether there is a deadlock condition.
4. If the system is deadlocked, list the processes that are deadlocked.
5. If the system is not deadlocked, show a series of process executions that are possible without deadlock.
6. Print the results to an output file (`output.txt`), indicating whether each process is deadlocked or not.
7. Exit the program.

# Author
Qusay Taradeh
