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
        

    allocator = PriorityAllocator()
    
    print("\n====== TIME SLOT ALLOCATION ======\n")
    
    selected_uav = allocator.allocate(uavs)
    
    print(f"\nTime slot allocated to UAV {selected_uav.id}")


    save_uavs_to_csv(uavs)
    
    tasks = Task.generate_tasks(10)

    save_tasks_to_csv(tasks)

    print("\n====== TASKS ======\n")

    for task in tasks:
        task.display()
        print()

if __name__ == "__main__":
    main()