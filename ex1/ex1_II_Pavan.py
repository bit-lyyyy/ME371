import csv

def read_mechanical_data(filename):
    mech_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            time = float(row[0])
            position = float(row[1])
            force = float(row[2])
            
            mech_data.append((time, position, force))
    
    return mech_data
    print(mech_data)
    # TODO: Implement reading from CSV file
    pass

def calculate_velocity(position_data, time_step):
    velocity=[]
    velocity_data=[]
    time, position = position_data
    for i in range(1,len(position)):
            delta_p= position[i]-position[i-1]
            velocity.append(delta_p/time_step)
            velocity_data.append([time[i],velocity[i-1]])

    return velocity_data
    

    # TODO: Implement velocity calculation
    pass

  

def calculate_acceleration(velocity_data, time_step):
    acceleration = []
    acceleration_data = []
    time, velocity = velocity_data

    for i in range(1, len(velocity)):
        delta_v = velocity[i] - velocity[i - 1]
        acceleration.append(delta_v / time_step)
        acceleration_data.append([time[i], acceleration[i - 1]])  # Properly create a tuple

    return acceleration_data


    # TODO: Implement acceleration calculation
    pass


def find_max_force(force_data):
    time, force = force_data

    max_force= max(force)
    time_max = time[force.index(max_force)]

    max_force_data= []
    max_force_data.append([time_max,max_force])
    
    return max_force_data
   
    # TODO: Implement maximum force calculation
    pass

def calculate_work_done(force_data, position_data):
    time_f, force = force_data
    time_p, position = position_data

    workdone = 0
    if (len(position) == len(force)):
        for i in range(1, len(position)):
            workdone= workdone + force[i]*(position[i]-position[i-1])


    return workdone
    # TODO: Implement work done calculation
    pass

def write_results(filename, results_data):
    velocity_data, acceleration_data, (max_force_time, max_force), work_done = results_data

    time_v, velocity = velocity_data
    time_a, acceleration = acceleration_data
    max_force_time, max_force = (max_force_time, max_force)
    write_data =[]
    write_data.append(['Max Force Time (s)', 'Max Force (N)'])
    write_data.append([max_force_time,max_force])
    write_data.append([])

    write_data.append(['Work Done (J)'])
    write_data.append([work_done])

    write_data.append([])
    write_data.append(['Time(s)', 'Velocity(m/s)', 'Acceleration(m/s^2)'])
    for i in range(1, len(time_v)):
        write_data.append([time_v[i],velocity[i], acceleration[i] if i<len(acceleration) else ''])

    with open(filename,'w', newline='') as file:
        writer= csv.writer(file)
        writer.writerows(write_data)

    # TODO: Implement writing results to CSV file
    pass

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