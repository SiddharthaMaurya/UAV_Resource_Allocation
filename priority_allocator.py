import math


class PriorityAllocator:

    def calculate_distance(self, uav, user_x, user_y):
        distance = math.sqrt(
            (uav.x - user_x) ** 2 +
            (uav.y - user_y) ** 2
        )
        return distance

    def calculate_path_loss(self, distance):
        path_loss_exponent = 2.5

        if distance < 1:
            distance = 1

        return distance ** path_loss_exponent

    def calculate_received_power(self, uav, distance):
        path_loss = self.calculate_path_loss(distance)

        return uav.transmit_power / path_loss

    def calculate_throughput(self, uav, distance):

        bandwidth_hz = uav.bandwidth * 1_000_000

        received_power = self.calculate_received_power(
            uav, distance
        )

        snr = received_power / uav.noise

        rate = bandwidth_hz * math.log2(1 + snr)

        return rate / 1_000_000

    # KEEP THIS FUNCTION
    def calculate_utility(self, uav, distance):

        throughput = self.calculate_throughput(
            uav, distance
        )

        # Temporary utility
        utility = throughput

        return utility

    def allocate(self, uavs):

        user_x = 200
        user_y = 200

        best_uav = None
        best_utility = 0

        for uav in uavs:

            distance = self.calculate_distance(
                uav,
                user_x,
                user_y
            )

            throughput = self.calculate_throughput(
                uav,
                distance
            )

            utility = self.calculate_utility(
                uav,
                distance
            )

            print(
                f"UAV {uav.id} -> "
                f"Distance: {distance:.2f} m, "
                f"Throughput: {throughput:.2f} Mbps, "
                f"Utility: {utility:.2f}"
            )

            if utility > best_utility:
                best_utility = utility
                best_uav = uav

        return best_uav