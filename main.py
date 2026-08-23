from uav import UAV , save_uavs_to_csv
from task import Task , save_tasks_to_csv




def main():
    uavs = [

        UAV(1, 100, 200, 90, 2.5),
        UAV(2, 250, 180, 75, 2.0),
        UAV(3, 320, 90, 60, 1.8),
        UAV(4, 150, 300, 95, 3.0),
        UAV(5, 400, 250, 50, 1.5)

    ]

    
    print("====== UAV NETWORK ======")
    for uav in uavs:
        uav.display()
        print()
        
        
    save_uavs_to_csv(uavs)
    
    tasks = Task.generate_tasks(10)

    save_tasks_to_csv(tasks)

    print("\n====== TASKS ======\n")

    for task in tasks:
        task.display()
        print()

if __name__ == "__main__":
    main()