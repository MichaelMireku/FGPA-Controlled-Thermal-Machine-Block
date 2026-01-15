module PWM #(
	parameter DataWidth = 10
) (
	input logic							clk,
  input logic							rstN,
  input logic [DataWidth-1:0]	treshold,
  output logic								pwm
);

	logic [DataWidth-1:0] counter, counterNext;
  logic pwmNext;
  
  //Combinatorial logic
  always_comb begin
  	counterNext = counter + 1;
    
    if (counter >= treshold) begin
      pwmNext = 1'b1;
    end else begin
    	pwmNext = 1'b0;
    end
  end
  
  //sequential logic
  always_ff @(posedge clk or negedge rstN) begin
    	if (!rstN) begin
      	counter <= '0;
        pwm <= 1'b0;
      end else begin
       	counter <= counterNext;
       	pwm <= pwmNext;
       end
     end
endmodule