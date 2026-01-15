# FPGA-Controlled Thermal Machine Block
January 2026
This is an engineering project that implements real-time thermal control using FPGA-based digital signal processing. This project demonstrates thermal modeling, hardware implementation, and closed-loop control of a thermal system.

This project implements a discrete-time thermal model for a 75×75×50 mm 6061-T6511 aluminum block using FPGA hardware. The system uses a lumped capacitance model with explicit Euler integration to predict and control temperature dynamics in real-time.

## Project Structure

```
├── 01_theory/          # First-principles thermal dynamics derivation
├── 02_hardware/        # Physical hardware specifications and setup
├── 03_fgpa/           # FPGA implementation and Verilog code
├── 04_data/           # Experimental data and measurements
├── 05_analysis/       # Data analysis and validation results
├── 06_validation/     # Model validation and testing
├── 07_summary/        # Project summary and conclusions
├── 08_cad/            # CAD files for mechanical design
└── 09_drafts/         # Work-in-progress documentation
```

## Key Features

- **Deterministic Thermal Modeling**: Fixed-point arithmetic implementation of the thermal differential equation
- **Real-Time Control**: FPGA-based parallel processing for low-latency temperature prediction
- **PWM Power Control**: High-frequency PWM modulation for precise power input control
- **Hardware-Efficient Design**: Bit-shift based calculations avoid expensive division operations

## Technical Details

### Thermal Model
The system implements the lumped capacitance model:

```
m * cp * dT/dt = Qin - hA(T - Tamb)
```

Discretized using Forward Euler method:

```
T[n+1] = T[n] + (Δt/τ) * (Tss - T[n])
```

Where:
- τ = m*cp/(hA) ≈ 2600 seconds (thermal time constant)
- Tss = Tamb + Qin/(hA) (steady-state temperature)

### FPGA Implementation
- **Fixed-point arithmetic**: 16-bit signed precision
- **Efficient alpha calculation**: α = Δt/τ = 2^(-k) using bit shifts
- **PWM frequency**: fpwm ≫ 1/τ for effective filtering
- **Update cycle**: Deterministic temperature updates using enable pulses

## Hardware Specifications

- **Target Block**: 75×75×50 mm 6061-T6511 Aluminum
- **Mass**: ~0.759 kg
- **Surface Area**: ~0.02625 m²
- **Material Properties**: ρ ≈ 2700 kg/m³, cp ≈ 900 J/kg·K
- **Natural Convection**: h ≈ 10 W/m²·K

- **Hardware**
I am in the process of acquiring the following to build the hardware model;
PGA board: Digilent Arty A7-35T (Artix-7)
(With the following ports/connectors;
USB-A 
Micro-USB 
USB-C)

-Thermal / Mechanical
Cartridge heater: 12 V 40–60 W Cartridge Heater, 6 mm × 20–30 mm
(example: Uxcell 12V 40W 6×20mm)
Thermal paste: Arctic MX-4
Heat sink: Aluminum CPU heatsink (passive or fan-mounted)
Cooling fan: 12 V 80 mm DC fan (e.g. Noctua NF-A8 12V)

Sensors
Temperature sensor: DS18B20 waterproof digital sensor
MCP9808 I²C temperature sensor breakout

Power Electronics
Logic-level MOSFET
Flyback diode
Gate resistor: 100 Ω
Pull-down resistor: 10 kΩ
Solid-state relay: Fotek SSR-25DD
Terminal blocks: 2-pin screw terminals

-Power
12 V 5 A DC power supply (desktop brick)

-Prototyping / Wiring
Breadboard or perfboard
Male–female jumper wires
Silicone-insulated hookup wire (18–22 AWG)

-Cooling
Corrosion inhibitor 
Pump: JT-180A 12 V DC micro pump
Tubing: 6 mm ID silicone tubing
Radiator: 120 mm PC liquid-cooling radiator
Flow sensor: YF-S201

Data / Interface
UART-USB: CP2102 USB-to-TTL module
Display: 0.96" OLED I²C (SSD1306)

-Tools
Drill + metal drill bits (6 mm for heater)
Multimeter
Thermal epoxy 

## Getting Started

### Prerequisites
- FPGA development environment (Xilinx Vivado, Intel Quartus, or similar)
- Verilog synthesis tools
- Hardware setup with temperature sensors and power control
- CAD software for mechanical design (FreeCAD files provided)


### Current Usage
1. Synthesize the Verilog modules in `03_fgpa/verilog/`
2. Configure the PWM and thermal block parameters
3. Deploy to FPGA hardware
4. Monitor temperature predictions and control performance

## Core Modules

### thermal_block.v
Implements the discrete-time thermal model:
- Fixed-point temperature calculations
- Configurable time constant via ALPHA_SHIFT
- Deterministic update cycles

### pwm.v
High-frequency PWM controller:
- Modulates power input (Qin)
- Frequency ≫ 1/τ for effective thermal filtering
- Drives the steady-state temperature parameter

## Validation and Analysis

The project includes comprehensive validation:
- **Model Validation**: Comparison between predicted and measured temperatures
- **Performance Analysis**: Control system response and stability
- **Error Analysis**: Accuracy of the lumped capacitance approximation

## CAD Files

Mechanical design files are provided in `08_cad/`:

(Requires FreeCAD to view and modify)

## Contributing

This project serves as both a practical implementation and educational resource for:
- Digital signal processing in FPGAs
- Thermal system modeling and control
- Hardware-software co-design
- Real-time embedded systems


## Acknowledgments

This project demonstrates the integration of theoretical thermal dynamics with practical FPGA implementation, showcasing the power of first-principles engineering in modern digital control systems. The current software components are functional.
