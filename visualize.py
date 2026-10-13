import matplotlib.pyplot as plt

def plot_task_allocation(allocation_count):
    uav_ids = list(allocation_count.keys())
    task_counts = list(allocation_count.values())

    plt.figure(figsize=(8, 5))

    plt.bar(uav_ids, task_counts, color='skyblue')

    plt.xlabel('UAV ID')
    plt.ylabel('Number of Tasks Allocated')
    plt.title('Task Allocation per UAV')

    plt.xticks(uav_ids)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("task_allocation.png")
    plt.show()


def plot_battery_levels(initial_battery,remaining_battery):
    uav_ids = list(initial_battery.keys())

    initial_values = [initial_battery[uav_id] for uav_id in uav_ids]
    remaining_values = [remaining_battery[uav_id] for uav_id in uav_ids]

    x = range(len(uav_ids))
    width = 0.35

    plt.figure(figsize=(8,5))

    plt.bar([i - width / 2 for i in x], initial_values, width=width, label='Initial Battery', color='lightgreen', align='center')
    plt.bar([i + width for i in x], remaining_values, width=width, label='Remaining Battery', color='salmon', align='center')

    plt.xlabel('UAV ID')
    plt.ylabel('Battery Level (%)')
    plt.title('Initial vs Remaining Battery Levels of UAVs')

    plt.xticks(list(x), [f"UAV {uav_id}" for uav_id in uav_ids])
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("battery_levels.png")
    plt.show()


def plot_success_rate(allocated_tasks, failed_tasks):
    labels = ["Successfully Allocated", "Failed"]
    values = [allocated_tasks, failed_tasks]

    plt.figure(figsize=(7, 5))
    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Task Allocation Success Rate")
    plt.tight_layout()
    plt.savefig("success_rate.png")
    plt.show()