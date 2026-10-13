README.md


UAV Resource Allocation
A Python-based simulation project for task allocation across Unmanned
Aerial Vehicles (UAVs). The simulator evaluates available UAVs and
selects a suitable UAV for each task using a priority-aware utility
function while considering distance, communication throughput, delay,
CPU capacity, and battery availability.

Project type: Academic mini project
Language: Python
Main goal: Simulate and evaluate resource-aware task allocation in
UAV networks.

Features
Generates tasks with different sizes, CPU-cycle requirements,
priorities, and deadlines.

Models multiple UAVs with different positions, CPU capabilities,
bandwidth, transmit power, and battery levels.

Estimates UAV-to-user distance, communication throughput,
transmission delay, computation delay, and energy consumption.

Uses a utility-based allocation strategy that considers throughput,
delay, energy, and task priority.

Checks task deadlines, available CPU capacity, and battery
constraints before allocating a task.

Tracks successful and failed allocations and the number of tasks
assigned to each UAV.

Exports allocation results to allocation_results.csv.

Generates visualizations for:

Task distribution across UAVs

Initial versus remaining UAV battery

Successful versus failed task allocations

How It Works
For each generated task, the allocator evaluates the candidate UAVs:

Check availability: Skip UAVs with no remaining battery.

Check CPU capacity: Verify that the UAV can accommodate the task
under the simulation's CPU-load limit.

Estimate communication and computation: Calculate distance,
throughput, transmission delay, and computation delay.

Check deadline and battery: Reject candidates that cannot meet
the task deadline or do not have enough estimated battery capacity.

Calculate utility: Score eligible UAVs using a weighted utility
function.

Select a UAV: Allocate the task to the eligible UAV with the
highest utility.

Update resources: Increase the selected UAV's current load and
deduct estimated energy use from its battery.

Record results: Save the task outcome and update the simulation
statistics.

The utility model currently rewards throughput and penalizes normalized
delay and energy consumption. Task priority is also included in the
utility calculation.

Important: This is a simulation model. Values and equations are
implementation assumptions and should not be interpreted as measurements
from real UAV hardware. Check the source code and project report for the
exact model used.

Project Structure
UAV_Resource_Allocation/
├── main.py                  # Runs the simulation and reports results
├── uav.py                   # UAV model and UAV data utilities
├── task.py                  # Task model and task generation
├── priority_allocator.py    # Utility calculation and task allocation logic
├── visualize.py             # Plots simulation results
├── allocation_results.csv   # Generated allocation report (after running)
├── task_allocation.png      # Generated task distribution plot
├── battery_levels.png       # Generated battery comparison plot
└── success_rate.png         # Generated success/failure plot
The generated CSV and image files appear after the simulation runs.
Depending on your local setup, your repository may also contain input
datasets or additional helper files.

Requirements
Python 3.10 or later recommended

matplotlib

Install the dependency:

python -m pip install matplotlib
If your project uses a virtual environment, activate it before
installing dependencies or running the program.

Run the Project
Clone your repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>
Move into the project directory:

cd UAV_Resource_Allocation
Install the dependency:

python -m pip install matplotlib
Run the simulation:

python main.py
The program prints allocation decisions and summary statistics in the
terminal. It also writes the allocation report to
allocation_results.csv and opens the result plots. Close each plot
window to continue if the program appears to pause.

Output and Evaluation
1. Allocation results --- allocation_results.csv
The CSV records each task's details and allocation status. Current
columns include:

Task ID

Size (MB)

CPU Cycles

Priority

Deadline

Allocated UAV

Status

2. Task allocation plot --- task_allocation.png
Shows how many tasks were assigned to each UAV.

3. Battery levels plot --- battery_levels.png
Compares each UAV's initial battery level with its remaining battery
after allocation.

4. Success rate plot --- success_rate.png
Shows the proportions of successfully allocated tasks and failed tasks
for the run.

Because tasks are generated randomly, results can vary between runs. Use
the same task set and the same initial UAV state when comparing
allocation strategies.

Current Simulation Considerations
The user location and several radio/resource parameters are
configured in the Python source files.

CPU capacity, energy consumption, and battery capacity are
simplified simulation models.

A task that cannot meet the deadline or resource constraints may
remain unallocated.

The current implementation is intended for academic simulation and
demonstration, not direct deployment on real UAV hardware.

Possible Future Improvements
Compare the priority-based allocator with a baseline strategy using
the same tasks and initial UAV conditions.

Add reproducible random seeds and configurable simulation
parameters.

Improve and validate the communication, energy, and battery models
against the selected research paper.

Evaluate additional metrics such as average delay, total energy
consumption, throughput, and per-priority success rate.

Add more UAVs, user locations, and larger task workloads.

Add automated tests and dependency management with a
requirements.txt file.

Research Reference
If this project is being implemented against the selected base paper,
include the paper's full title, authors, journal, year, and DOI in your
report and verify that the implementation matches the paper's equations.

Base-paper DOI supplied for this project: 10.1109/JIOT.2025.3597502

Author
Siddhartha Maurya
