# system_performance_simulation.py

"""
System Performance Simulation
Author: Daniel J. Farley
Purpose: Demonstrates simple system modeling and performance simulation.
Generates plots and logs for two input scenarios.
"""

import os
import sys
import numpy as np

# Attempt to import matplotlib and provide clear instructions if missing
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: matplotlib is not installed. Please run 'pip install matplotlib'")
    sys.exit(1)

# -----------------------------
# System Model Definition
# -----------------------------
def system_model(input_signal, gain=1.0, decay=0.1):
    """
    Simple first-order discrete-time system simulation.
    
    Args:
        input_signal (numpy array): Input signal array.
        gain (float): System gain factor.
        decay (float): System decay factor.

    Returns:
        numpy array: Output signal of the system.
    """
    output = np.zeros_like(input_signal)
    for t in range(1, len(input_signal)):
        output[t] = output[t-1] + gain * (input_signal[t] - output[t-1]) * decay
    return output

# -----------------------------
# Main Simulation Function
# -----------------------------
def run_simulation():
    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Define input scenarios
    time = np.linspace(0, 10, 500)  # 10 seconds, 500 points
    input_scenario1 = np.sin(time)          # Sinusoidal input
    input_scenario2 = np.ones_like(time)    # Step input

    # Run system model
    output1 = system_model(input_scenario1)
    output2 = system_model(input_scenario2, gain=0.5, decay=0.05)

    # -----------------------------
    # Generate and save plots
    # -----------------------------
    try:
        plt.figure()
        plt.plot(time, input_scenario1, label="Input")
        plt.plot(time, output1, label="Output")
        plt.title("Scenario 1: Sinusoidal Input")
        plt.xlabel("Time")
        plt.ylabel("System Response")
        plt.legend()
        plt.savefig("outputs/scenario1.png")
        plt.close()

        plt.figure()
        plt.plot(time, input_scenario2, label="Input")
        plt.plot(time, output2, label="Output")
        plt.title("Scenario 2: Step Input")
        plt.xlabel("Time")
        plt.ylabel("System Response")
        plt.legend()
        plt.savefig("outputs/scenario2.png")
        plt.close()
    except Exception as e:
        print(f"Error generating plots: {e}")
        sys.exit(1)

    # -----------------------------
    # Save logs
    # -----------------------------
    try:
        with open("outputs/logs.txt", "w") as f:
            f.write("Simulation completed successfully.\n")
            f.write(f"Scenario 1 output mean: {np.mean(output1):.3f}\n")
            f.write(f"Scenario 2 output mean: {np.mean(output2):.3f}\n")
            f.write(f"Scenario 1 max: {np.max(output1):.3f}, min: {np.min(output1):.3f}\n")
            f.write(f"Scenario 2 max: {np.max(output2):.3f}, min: {np.min(output2):.3f}\n")
    except Exception as e:
        print(f"Error writing logs: {e}")
        sys.exit(1)

    print("Simulation completed successfully. Outputs saved in 'outputs/' folder.")

# -----------------------------
# Run Script
# -----------------------------
if __name__ == "__main__":
    run_simulation()
