import csv
import math

def read_beam_data(filename):
    """
    Read beam data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    tuple: (length, width, height, elastic_modulus, loads)
    where loads is a list of tuples (position, magnitude)
    """
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        
        header = next(csv_reader)
        length, width, height, elastic_modulus = map(float, next(csv_reader))  

        loads = []

        next(csv_reader)  

        for row in csv_reader:
            position = float(row[0])
            magnitude = float(row[1])
            loads.append((position, magnitude))

    return length, width, height, elastic_modulus, loads

def calculate_bending_moment(length, loads):
    """
    Calculate the maximum bending moment in the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    
    Returns:
    float: Maximum bending moment
    """
    positions = [0] + [position for position, magnitude in loads] + [length]

    max_bending_moment = 0

    for x in positions:
        bending_moment = 0  
        for load_position, load_magnitude in loads:
            if load_position <= x:
                bending_moment += load_magnitude * (x - load_position)
        
        max_bending_moment = max(max_bending_moment, abs(bending_moment))

    return max_bending_moment

def calculate_shear_force(length, loads):
    """
    Calculate the maximum shear force in the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    
    Returns:
    float: Maximum shear force
    """
    positions = [0] + [position for position, magnitude in loads] + [length]

    current_shear_force = 0
    max_shear_force = 0

    loads.sort(key=lambda x: x[0]) 

    for x in positions:
        for load_position, load_magnitude in loads:
            if load_position <= x:
                current_shear_force += load_magnitude

        max_shear_force = max(max_shear_force, abs(current_shear_force))

    return max_shear_force

def calculate_max_bending_stress(max_moment, moment_of_inertia, y_max):
    """
    Calculate the maximum bending stress in the beam.
    
    Args:
    max_moment (float): Maximum bending moment
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    y_max (float): Distance from neutral axis to extreme fiber
    
    Returns:
    float: Maximum bending stress
    """
    if moment_of_inertia == 0:
        raise ValueError("Moment of inertia cannot be zero.")

    max_bending_stress = (max_moment * y_max) / moment_of_inertia

    return max_bending_stress

def calculate_max_shear_stress(max_shear, first_moment, moment_of_inertia, width):
    """
    Calculate the maximum shear stress in the beam.
    
    Args:
    max_shear (float): Maximum shear force
    first_moment (float): First moment of area of the beam cross-section
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    width (float): Width of the beam at the neutral axis
    
    Returns:
    float: Maximum shear stress
    """
    if moment_of_inertia == 0:
        raise ValueError("Moment of inertia cannot be zero.")
    if width == 0:
        raise ValueError("Width cannot be zero.")

    max_shear_stress = (max_shear * first_moment) / (moment_of_inertia * width)

    return max_shear_stress

def calculate_max_deflection(length, loads, elastic_modulus, moment_of_inertia):
    """
    Calculate the maximum deflection of the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    elastic_modulus (float): Elastic modulus of the beam material
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    
    Returns:
    float: Maximum deflection
    """
    max_deflection = 0

    for position, magnitude in loads:
        a = position  
        F = magnitude  
        L = length  
        E = elastic_modulus 
        I = moment_of_inertia  

        deflection = (F * a * (L**2 - a**2)) / (6 * E * I)

        max_deflection = max(max_deflection, abs(deflection))

    return max_deflection

def write_results(filename, results_data):
    """
    Write calculation results to a CSV file.
    
    Args:
    filename (str): Name of the output CSV file
    results_data (dict): Dictionary containing results to be written
    """
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for key, value in results_data.items():
                writer.writerow([key.capitalize() + " Data"])

                if isinstance(value, list) and all(isinstance(item, tuple) for item in value):
                    if key == "velocity":
                        writer.writerow(["Time (s)", "Velocity (m/s)"])
                    elif key == "acceleration":
                        writer.writerow(["Time (s)", "Acceleration (m/s^2)"])
                    elif key == "loads":
                        writer.writerow(["Position (m)", "Load (N)"])

                    for item in value:
                        writer.writerow(item)

                elif isinstance(value, tuple) and len(value) == 2:
                    writer.writerow(["Time (s)", "Value"])
                    writer.writerow(value)

                else:
                    writer.writerow([str(value)])

                writer.writerow([])

        print(f"Results successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing results: {e}")

def main():
    input_file = "beam_data.csv"
    output_file = "beam_analysis_results.csv"

    try:
        # Read beam data
        length, width, height, elastic_modulus, loads = read_beam_data(input_file)

        # Calculate beam properties
        moment_of_inertia = (width * height**3) / 12
        y_max = height / 2
        first_moment = (width * height**2) / 8

        # Perform calculations
        max_moment = calculate_bending_moment(length, loads)
        max_shear = calculate_shear_force(length, loads)
        max_bending_stress = calculate_max_bending_stress(max_moment, moment_of_inertia, y_max)
        max_shear_stress = calculate_max_shear_stress(max_shear, first_moment, moment_of_inertia, width)
        max_deflection = calculate_max_deflection(length, loads, elastic_modulus, moment_of_inertia)

        # Prepare results
        results = {
            "max_bending_stress": max_bending_stress,
            "max_shear_stress": max_shear_stress,
            "max_deflection": max_deflection
        }

        # Write results to file
        write_results(output_file, results)
        print(f"Results written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()