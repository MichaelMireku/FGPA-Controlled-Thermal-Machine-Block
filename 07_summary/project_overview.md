# Engineering Project: FGPA-Controlled Thermal Machine Block

## Project Overview
This project demonstrates a complete engineering workflow for the digital control of a thermal system (centered on a 1100 Aluminum block), bridging first-principles physics with real-time digital design (RTL) intended for future hardware deployment.

## Key Outcomes

### 1. Mathematical Modeling
- Successfully derived the **Lumped Capacitance Model** using energy balances.
- Identified the system time constant $\tau = \frac{m c_p}{hA}$, providing a fundamental metric for control responsiveness.
- Discretized the continuous ODE using the **Forward Euler** method, yielding a recursive algorithm suitable for digital logic.

### 2. Validation & Simulation
- Implemented a high-fidelity Python simulation to validate the step response.
- Performed **Numerical Stability Analysis**, establishing the critical constraint $\Delta t < 2\tau$ for the Euler solver.
- Confirmed that choosing $\Delta t \ll \tau$ eliminates oscillations and matches analytical solutions.

### 3. Hardware-Oriented Design
- Translated the mathematical model into **Verilog RTL**, optimized for FPGA resources.
- Leveraged fixed-point arithmetic and bit-shifting to implement the thermal dynamics without floating-point units or dividers.
- Integrated a PWM control scheme to manage power delivery to the physical plant.

## Conclusion
The resulting system provides a robust platform for high-performance temperature monitoring and control. By anchoring the digital implementation in rigorous physical modeling, we ensure both accuracy and deterministic behavior essential for industrial and scientific applications.
