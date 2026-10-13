import csv
import os

from uav import UAV , save_uavs_to_csv
from task import Task , save_tasks_to_csv

from priority_allocator import PriorityAllocator

from visualize import plot_task_allocation , plot_battery_levels ,plot_success_rate




def main():
    uavs = [

        UAV(1, 100, 200, 90, 2.5 ,10 ,0.5,0.01),
        UAV(2, 250, 180, 75, 2.0 ,8 ,0.4,0.02),
        UAV(3, 320, 90, 60, 1.8 ,12 ,0.3,0.03),
        UAV(4, 150, 300, 95, 3.0 ,20 ,0.6,0.04),
        UAV(5, 400, 250, 50, 1.5 ,6 ,0.2,0.05)

    ]

    initial_battery = {uav.id: uav.battery for uav in uavs}

    
    
    print("====== UAV NETWORK ======")

    for uav in uavs:
        uav.display()
        print()

    save_uavs_to_csv(uavs)

    #generate tasks and save task
    tasks = Task.generate_tasks(10)

    save_tasks_to_csv(tasks)


    #create allocator object
    allocator = PriorityAllocator()

    total_tasks = len(tasks)
    allocated_tasks = 0
    failed_tasks = 0

    allocation_count = {uav.id: 0 for uav in uavs}
    allocation_results = []
    
    print(f"\n====== TAKS ALLOCATION ======\n")

    for task in tasks:

        print(f"--- Task {task.task_id} ---")

        selected_uav = allocator.allocate(uavs, task)

        if selected_uav is not None:
            allocated_tasks += 1
            allocation_count[selected_uav.id] += 1
        
            allocation_results.append({
                "Task ID": task.task_id,
                "Size (MB)": task.size_mb,
                "CPU Cycles": task.cpu_cycles,
                "Priority": task.priority,
                "Deadline": task.deadline,
                "Allocated UAV": selected_uav.id,
                "Status": "Success"
            })
        
            print(
                f"\nTask {task.task_id} allocated "
                f"to UAV {selected_uav.id}"
            )
    
        else:
            failed_tasks += 1
        
            allocation_results.append({
                "Task ID": task.task_id,
                "Size (MB)": task.size_mb,
                "CPU Cycles": task.cpu_cycles,
                "Priority": task.priority,
                "Deadline": task.deadline,
                "Allocated UAV": "None",
                "Status": "Failed"
            })
        
            print(
                f"\nTask {task.task_id} could not be allocated "
                f"because no feasible UAV was available."
            )

    # save allocation results to csv
    filename = "allocation_results.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "Task ID",
            "Size (MB)",
            "CPU Cycles",
            "Priority",
            "Deadline",
            "Allocated UAV",
            "Status"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(allocation_results)

    print(f"\nAllocation results saved to: {os.path.abspath(filename)}")

    

    print("\n====== TASKS ALLOCATED PER UAV ======")

    for uav_id, count in allocation_count.items():
        print(f"UAV {uav_id}: {count} tasks")

    print("\n====== ALLOCATION STATISTICS ======")

    print(f"Total Tasks: {total_tasks}")
    print(f"Successfully Allocated: {allocated_tasks}")
    print(f"Failed Tasks: {failed_tasks}")
    
    success_rate = (allocated_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    print(f"Allocation Success Rate: {success_rate:.2f}%")

    plot_success_rate(allocated_tasks, failed_tasks)

    remaining_battery = {
        uav.id: uav.battery for uav in uavs
    }
    plot_battery_levels(initial_battery, remaining_battery)


    print("\n====== FINAL UAV STATUS ======")

    for uav in uavs:
        print(f"\nUAV {uav.id}")
        print(f"Remaining Battery: {uav.battery:.2f}%")
        print(f"CPU Load: {uav.current_load:.2e} cycles")

    plot_task_allocation(allocation_count)

    print("\n====== TASKS ======\n")

    for task in tasks:
        task.display()
        print()

    

if __name__ == "__main__":
    main()