# Thermal Dynamics: Lumped Capacitance Model

This document outlines the first-principles derivation of the transient thermal behavior for a lumped solid system, which serves as the basis for our digital control implementation.

## 1. First-Principles Energy Balance

For a lumped solid system (where internal temperature gradients are negligible, i.e., $Bi < 0.1$), the rate of change of energy storage is equal to the heat input minus the heat losses.

The governing ordinary differential equation (ODE) is:

$$m c_p \frac{dT}{dt} = Q_{in} - hA(T - T_{amb})$$

Where:
- $m$: Mass of the solid $[kg]$
- $c_p$: Specific heat capacity $[J/kg \cdot K]$
- $T$: Temperature of the solid $[K]$ or $[^\circ C]$
- $t$: Time $[s]$
- $Q_{in}$: Power input (e.g., resistive heating) $[W]$
- $h$: Convective heat transfer coefficient $[W/m^2 \cdot K]$
- $A$: Surface area $[m^2]$
- $T_{amb}$: Ambient temperature $[K]$ or $[^\circ C]$

## 2. Steady-State Temperature ($T_{ss}$)

At steady state, the temperature is constant, so $\frac{dT}{dt} = 0$:

$$0 = Q_{in} - hA(T_{ss} - T_{amb})$$
$$T_{ss} = T_{amb} + \frac{Q_{in}}{hA}$$

## 3. System Time Constant ($\tau$)

Rearranging the ODE into standard form:

$$\frac{m c_p}{hA} \frac{dT}{dt} + T = T_{amb} + \frac{Q_{in}}{hA}$$

Thus, the thermal time constant is:

$$\tau = \frac{m c_p}{hA}$$

The equation becomes:

$$\tau \frac{dT}{dt} + T = T_{ss}$$

## 4. Discrete-Time Euler Formulation

To implement this on a digital system (like an FPGA or MCU), we discretize the derivative using the Forward Euler method:

$$\frac{dT}{dt} \approx \frac{T[n+1] - T[n]}{\Delta t}$$

Substituting into the normalized ODE:

$$\tau \frac{T[n+1] - T[n]}{\Delta t} + T[n] = T_{ss}$$

Solving for $T[n+1]$:

$$T[n+1] = T[n] + \frac{\Delta t}{\tau} (T_{ss} - T[n])$$

## 5. Example Case: 75 x 75 x 50 mm 1100 Aluminum Block

Based on the specified hardware dimensions:
- **Dimensions**: $0.075 \times 0.075 \times 0.050$ m
- **Material**: 1100 Aluminum ($\rho \approx 2700$ kg/m$^3$, $c_p \approx 900$ J/kg·K)
- **Mass ($m$)**: $\approx 0.759$ kg
- **Surface Area ($A$)**: $\approx 0.02625$ m$^2$
- **Time Constant ($\tau$)**: With a typical natural convection $h=10$ W/m$^2$·K, $\tau = \frac{m c_p}{hA} \approx 2600$ seconds.

This large time constant indicates a slow thermal response, which simplifies the digital control requirements as the update frequency can be relatively low while maintaining high stability.
