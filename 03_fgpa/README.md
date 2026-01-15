# FPGA Thermal Control Implementation

This FPGA project implements a hardware-parallel discrete-time thermal model using explicit Euler integration for real-time monitoring and control.

## Key Features
- **Deterministic Update Cycle**: Temperature dynamics are updated at a fixed timestep ($\Delta t$) using an `update_en` pulse.
- **Efficient Arithmetic**: The model uses signed fixed-point arithmetic. The time constant $\tau$ is implemented as a bit-shift (`ALPHA_SHIFT`), where $\alpha = \Delta t / \tau = 2^{-k}$. This avoids expensive division in hardware.
- **PWM Integration**: A High-frequency PWM [pwm.v] modulates the power input $Q_{in}$, effectively driving the $T_{ss}$ parameter of the [thermal_block.v].

## Design Philosophy
The PWM frequency is selected to be $f_{pwm} \gg 1/\tau$, ensuring the thermal mass effectively filters the power switching. This allows the system to be modeled linearly despite the discontinuous power input.