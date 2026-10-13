import math

import task


class PriorityAllocator:

    def can_handle_task(self ,uav ,task):
        available_time = 10

        max_capaity = uav.cpu * 1_000_000_000 * available_time

        if uav.current_load + task.cpu_cycles <= max_capaity:
            return True
        
        return False

    def calculate_transmission_delay(self, task , throughput):

        if throughput <= 0:
            return float("inf")

        delay = (task.size_mb * 8) / throughput

        return delay

    def calculate_computation_delay(self, task , uav):
        cpu_frequency = uav.cpu * 1_000_000_000 #GHz to MHz 

        delay = task.cpu_cycles / cpu_frequency

        return delay


    def calculate_energy(self, task, uav):

        # Transmission energy
        distance = self.calculate_distance(uav, 200, 200)
        throughput = self.calculate_throughput(uav, distance)
    
        transmission_delay = self.calculate_transmission_delay(
            task, throughput
        )
    
        transmission_energy = (
            uav.transmit_power * transmission_delay
        )
    
        # Computation energy
        computation_energy = (
            task.cpu_cycles * 1e-9
        )
    
        total_energy = (
            transmission_energy + computation_energy
        )
    
        return total_energy

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

        w1 = 0.6
        w2 = 0.2
        w3 = 0.2


        priority_weight = {
            "High": 1.2,
            "Medium": 1.0,
            "Low": 0.8
        }
        
        priority_factor = priority_weight[task.priority]
        priority_weight = {
            "High": 1.2,
            "Medium": 1.0,
            "Low": 0.8
        }

        priority_factor = priority_weight[task.priority]
        
        energy = self.calculate_energy(task, uav)
        
        max_delay = task.deadline
        max_energy = 100
        
        utility = (
            w1 * throughput
            - w2 * (delay / max_delay)
            - w3 * (energy / max_energy)
        ) * priority_factor
        
        return utility

    def allocate(self, uavs , task):

        user_x = 200
        user_y = 200

        best_uav = None
        best_utility = float("-inf")

        for uav in uavs:

            if uav.battery <= 0:
                print(f"UAV {uav.id} -> Insufficient battery")
                continue
        
            if not self.can_handle_task(uav, task):
                print(f"UAV {uav.id} -> Insufficient CPU capacity")
                continue

            energy_required = self.calculate_energy(task, uav)

            battery_capacity = 1000.0
            battery_required_percent = (energy_required / battery_capacity) * 100
        
            if uav.battery < battery_required_percent:
                print(f"UAV {uav.id} -> Insufficient battery")
                continue


        
            if not self.can_handle_task(uav, task):

                print(
                    f"UAV {uav.id} -> "
                    f"Insufficient CPU capacity"
                )

                continue

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

        if best_uav is not None:
            best_uav.current_load += task.cpu_cycles
        
            energy_used = self.calculate_energy(task, best_uav)
        
            battery_capacity = 1000.0
            battery_used_percent = (energy_used / battery_capacity) * 100
        
            best_uav.battery -= battery_used_percent

            print(
                f"UAV {best_uav.id} -> "
                f"Energy used: {energy_used:.4f} J, "
                f"Remaining battery: {best_uav.battery:.2f}%"
            )


        return best_uav