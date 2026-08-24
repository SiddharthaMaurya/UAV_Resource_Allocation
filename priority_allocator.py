class PriorityAllocator:

    def calculate_utility(self,uav):

        utility = (uav.battery * 0.5 + uav.cpu * 10)
        return utility

    def allocate(self , uavs):

        best_uav = None
        best_utility = 0

        for uav in uavs:

            utility = self.calculate_utility(uav)

            print(f"UAV {uav.id} -> Utility: {utility:.2f}")

            if utility > best_utility:
                best_utility = utility
                best_uav = uav

        return best_uav