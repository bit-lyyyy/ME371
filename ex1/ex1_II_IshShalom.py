import csv

def read_mechanical_data(filename):
    """
    Read mechanical data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    list of tuples: List of (time, position, force) tuples
    """
    data_tuples = []

    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                time = float(row['time'])
                position = float(row['position'])
                force = float(row['force'])
                
                data_tuple = (time, position, force)
                
                data_tuples.append(data_tuple)
            except ValueError:
                print(f"Skipping row with invalid data: {row}")

    return data_tuples
    

def calculate_velocity(position_data, time_step):
    """
    Calculate velocity from position data.
    
    Args:
    position_data (list of tuples): List of (time, position) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, velocity) tuples
    """
    veloctiy_data = []
    for i in range(1, len(position_data)):
        t = position_data[i][0]
        x1 = position_data[i][1]
        x0 = position_data[i-1][1]

        dx = (x1 - x0)/time_step
        veloctiy_data.append((t, dx))
    return veloctiy_data


def calculate_acceleration(velocity_data, time_step):
    """
    Calculate acceleration from velocity data.
    
    Args:
    velocity_data (list of tuples): List of (time, velocity) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, acceleration) tuples
    """
    acceleration_data = []
    for i in range(1, len(velocity_data)):
        t = velocity_data[i][0]
        v1 = velocity_data[i][1]
        v0 = velocity_data[i-1][1]

        dv = (v1 - v0)/time_step
        acceleration_data.append((t, dv))
    return acceleration_data


def find_max_force(force_data):
    """
    Find the maximum force applied to the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    
    Returns:
    tuple: (time, max_force)
    """
    time_of_max_force, max_force = max(force_data, key=lambda item: item[1])
    
    return time_of_max_force, max_force
    

def calculate_work_done(force_data, position_data):
    """
    Calculate the total work done on the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    position_data (list of tuples): List of (time, position) tuples
    
    Returns:
    float: Total work done
    """
    if len(force_data) != len(position_data):
            raise ValueError("The length of force_data and position_data must be equal.")
    
    work_done = 0
    for i in range(1, len(force_data)):
        x1 = position_data[i][1]
        x0 = position_data[i-1][1]
        F = force_data[i][1]
        work_done += F * (x1-x0)
    return work_done


def write_results(filename, results_data):
    """
    Write calculation results to a CSV file.
    
    Args:
    filename (str): Name of the output CSV file
    results_data (dict): Dictionary containing results to be written
    """
    try:
        # Open the file in write mode
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write headers for each section and then the corresponding data
            
            # Write Velocity Data
            writer.writerow(["Velocity Data"])
            writer.writerow(["Time (s)", "Velocity (m/s)"])
            for time, velocity in results_data["velocity"]:
                writer.writerow([time, velocity])

            writer.writerow([])  # Empty row for separation

            # Write Acceleration Data
            writer.writerow(["Acceleration Data"])
            writer.writerow(["Time (s)", "Acceleration (m/s^2)"])
            for time, acceleration in results_data["acceleration"]:
                writer.writerow([time, acceleration])

            writer.writerow([])  # Empty row for separation

            # Write Maximum Force Data
            writer.writerow(["Maximum Force"])
            writer.writerow(["Time (s)", "Max Force (N)"])
            max_force_time, max_force = results_data["max_force"]
            writer.writerow([max_force_time, max_force])

            writer.writerow([])  # Empty row for separation

            # Write Work Done
            writer.writerow(["Work Done"])
            writer.writerow(["Total Work Done (Joules)"])
            writer.writerow([results_data["work_done"]])

        print(f"Results successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing results: {e}")

def main():
    input_file = "mechanical_data.csv"
    output_file = "analysis_results.csv"
    time_step = 0.1  # s

    try:
        # Read mechanical data
        data = read_mechanical_data(input_file)

        # Extract position and force data
        time_data = [item[0] for item in data]
        position_data = [(item[0], item[1]) for item in data]
        force_data = [(item[0], item[2]) for item in data]

        # Calculate velocity and acceleration
        velocity_data = calculate_velocity(position_data, time_step)
        acceleration_data = calculate_acceleration(velocity_data, time_step)

        # Find maximum force
        max_force_time, max_force = find_max_force(force_data)

        # Calculate work done
        work_done = calculate_work_done(force_data, position_data)

        # Prepare results
        results = {
            "velocity": velocity_data,
            "acceleration": acceleration_data,
            "max_force": (max_force_time, max_force),
            "work_done": work_done
        }

        # Write results to file
        write_results(output_file, results)
        print(f"Results written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()