/* 
 * Thermal Block: Discrete-Time Euler Model implementation
 * 
 * Formula: T[n+1] = T[n] + (alpha * (T_steady - T[n]))
 * Where alpha = dt / tau (pre-calculated or parameterized)
 */

module thermal_block #(
    parameter WIDTH = 16,        // Fixed-point bit width
    parameter ALPHA_SHIFT = 8    // Alpha = 2^-ALPHA_SHIFT for efficient implementation
)(
    input  logic              clk,
    input  logic              rstN,
    input  logic              update_en, // Pulse to trigger dT update (dt)
    input  logic [WIDTH-1:0]  T_steady,   // Current steady-state target based on power
    output logic [WIDTH-1:0]  T_current   // Current predicted temperature
);

    logic [WIDTH-1:0] T_reg;
    logic [WIDTH-1:0] delta_T;

    always_ff @(posedge clk or negedge rstN) begin
        if (!rstN) begin
            T_reg <= '0; // Initial temperature (can be T_amb)
        end else if (update_en) begin
            // delta_T = (T_steady - T_reg) >> ALPHA_SHIFT
            // Implementing T[n+1] = T[n] + ((T_steady - T[n]) >>> ALPHA_SHIFT)
            T_reg <= T_reg + ($signed(T_steady - T_reg) >>> ALPHA_SHIFT);
        end
    end

    assign T_current = T_reg;

endmodule
