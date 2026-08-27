import math


class PriorityAllocator:

    def calculate_transmission_delay(self, task , throughput):

        if throughput <= 0:
            return float("inf")

        delay = (task.size_mb * 8) / throughput

        return delay

    def calculate_computation_delay(self, task , uav):
        cpu_frequency = uav.cpu * 1000 #GHz to MHz 

        delay = task.cpu_cycles / cpu_frequency

        return delay


    def calculate_delay(self, task, uav, throughput):

        transmission_delay = self.calculate_transmission_delay(task , throughput)

        computation_delay = self.calculate_computation_delay(task , uav)

        total_delay = transmission_delay + computation_delay

        return total_delay
    

    

    def calculate_distance(self, uav, user_x, user_y):
        distance = math.sqrt(
            (uav.x - user_x) ** 2 +
            (uav.y - user_y) ** 2
        )
        return distance

    def calculate_path_loss(self, distance):
        path_loss_exponent = 2.5
        reference_distance = 10

        if distance < reference_distance:
            distance = reference_distance

        path_loss = (distance / reference_distance) ** path_loss_exponent

        return path_loss

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
    def calculate_utility(self, uav, distance, task):

        throughput = self.calculate_throughput(
            uav, distance
        )

        delay = self.calculate_delay(task , uav , throughput)

        if delay > task.deadline:
            return float("-inf")

        #weights for throughput and delay
        w1 = 0.7
        w2 = 0.3

        #maximum acceptable delay
        max_delay = task.deadline


        # Temporary utility
        utility = (w1 * throughput - w2 * (delay / max_delay))

        return utility

    def allocate(self, uavs , task):

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

            delay = self.calculate_delay(
                task ,
                uav,
                throughput
            )

            utility = self.calculate_utility(
                uav,
                distance,
                task
            )

            print(
                f"UAV {uav.id} -> "
                f"Throughput: {throughput:.2f} Mbps, "
                f"Distance: {distance:.2f} m, "
                f"Delay: {delay:.2f} s, "
                f"Utility: {utility:.4f}"
            )

            if utility > best_utility:
                best_utility = utility
                best_uav = uav

        return best_uav