from uav import UAV , save_uavs_to_csv
from task import Task , save_tasks_to_csv

from priority_allocator import PriorityAllocator




def main():
    uavs = [

        UAV(1, 100, 200, 90, 2.5 ,10 ,0.5,0.01),
        UAV(2, 250, 180, 75, 2.0 ,8 ,0.4,0.02),
        UAV(3, 320, 90, 60, 1.8 ,12 ,0.3,0.03),
        UAV(4, 150, 300, 95, 3.0 ,20 ,0.6,0.04),
        UAV(5, 400, 250, 50, 1.5 ,6 ,0.2,0.05)

    ]

    
    
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
    

    
    print(f"\n====== TAKS ALLOCATION ======\n")

    for task in tasks:

        print(f"--- Task {task.task_id} ---")

        selected_uav = allocator.allocate(uavs, task)

        if selected_uav is not None:
            print(
                f"\nTask {task.task_id} allocated "
                f"to UAV {selected_uav.id}"
                )
        else:
            print(
                f"\nTask {task.task_id} could not be allocated "
                f"because no UAV meets the deadline."
            )
    

    print("\n====== TASKS ======\n")

    for task in tasks:
        task.display()
        print()

if __name__ == "__main__":
    main()