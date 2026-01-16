import numpy as np
import matplotlib.pyplot as plt

def simulate_thermal_block():
    #Physical Parameters (75 x 75 x 50 mm 1100 Aluminum Block)
    rho = 2700          # kg/m^3 (Standard density for 1100 Aluminum)
    L, W, H = 0.075, 0.075, 0.050  # meters
    volume = L * W * H
    mass = rho * volume # ~0.759 kg
    cp = 904            # J/(kg*K) (Specific heat of Aluminum)
    h = 10              # W/(m^2*K) (Natural convection)
    area = 2 * (L*W + L*H + W*H) # ~0.02625 m^2
    t_amb = 25.0        # degC (Ambient temperature)
    q_in = 50.0         # W (Step power input)

    # Derived constants
    tau = (mass * cp) / (h * area)
    t_ss = t_amb + (q_in / (h * area))

    print(f"System Time Constant (tau): {tau:.2f} s")
    print(f"Steady-State Temperature (T_ss): {t_ss:.2f} °C")

    # Simulation Setup 
    dt = 1.0            # s (Time step) - Stability: dt < tau
    total_time = 3000   # s (Total sim duration)
    steps = int(total_time / dt)

    t = np.linspace(0, total_time, steps)
    temp_sim = np.zeros(steps)
    temp_sim[0] = t_amb

    # Discrete-Time Euler Simulation
    for n in range(steps - 1):
        # Forward Euler: T[n+1] = T[n] + (dt/tau) * (T_ss - T[n])
        temp_sim[n+1] = temp_sim[n] + (dt / tau) * (t_ss - temp_sim[n])

    # Analytical Solution for Comparison 
    # T(t) = T_ss + (T_initial - T_ss) * exp(-t / tau)
    temp_analyt = t_ss + (t_amb - t_ss) * np.exp(-t / tau)

    # Plotting 
    plt.figure(figsize=(10, 6))
    plt.plot(t, temp_sim, 'r--', label='Numerical (Euler)')
    plt.plot(t, temp_analyt, 'b-', alpha=0.5, label='Analytical')
    plt.axhline(y=t_ss, color='g', linestyle=':', label='Steady-State')
    plt.title('Transient Thermal Step Response')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)

    plt.savefig('thermal_response.png')

if __name__ == "__main__":
    simulate_thermal_block()
