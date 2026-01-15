# Numerical Stability Analysis

To ensure the validity of our digital implementation (Euler formulation), we must analyze the conditions under which the numerical solution remains stable.

## 1. Stability Criterion for Forward Euler

In the discrete-time formulation:

$$T[n+1] = T[n] + \frac{\Delta t}{\tau} (T_{ss} - T[n])$$

We can rewrite this as:

$$T[n+1] = T[n] (1 - \frac{\Delta t}{\tau}) + \frac{\Delta t}{\tau} T_{ss}$$

For the solution to remain bounded and converge to $T_{ss}$ without oscillating or diverging, the coefficient of $T[n]$ must satisfy:

$$|1 - \frac{\Delta t}{\tau}| < 1$$

## 2. Critical Time Step ($\Delta t_{crit}$)

From the inequality above:

$$-1 < 1 - \frac{\Delta t}{\tau} < 1$$

The right side ($1 - \frac{\Delta t}{\tau} < 1$) is always true for $\Delta t > 0$ and $\tau > 0$.
The left side gives the critical constraint:

$$-1 < 1 - \frac{\Delta t}{\tau}$$
$$\frac{\Delta t}{\tau} < 2$$
$$\Delta t < 2\tau$$

However, to avoid non-physical oscillations (where the temperature "overshoots" the steady state in a single step), we typically require:

$$\Delta t < \tau$$

## 3. Simulation Validation

In our simulation (`thermal_simulation.py`):
- $\tau \approx 450$ s
- $\Delta t = 1.0$ s

Since $\Delta t \ll \tau$, the simulation is unconditionally stable and provides high accuracy relative to the analytical solution.

## 4. Hardware Implementation Note

Specifically for FPGA implementations with fixed-point arithmetic, choosing $\Delta t$ as a power of 2 relative to $\tau$ (e.g., $\Delta t/\tau = 2^{-k}$) allows for the division to be replaced by a simple bit-shift, significantly reducing resource utilization.
