module alu #(parameter WIDTH = 16) // is 4 for testing purposes
            (input      [WIDTH-1:0] a, b, // a is Rdest, b is Rsrc
             input      [4:0]    	aluOp, 
				 input c,
             output reg [WIDTH-1:0] result,
				 output reg [4:0] conCodes);
				// output reg codesComputed);

	reg 		[WIDTH-1:0] overflowRes, carryoutRes;

	// arr[4] = negative,  arr[3] = zero,  arr[2] = flag
	// arr[1] = lower,     arr[0] = carry
	
   always@(*)
	begin
		conCodes = 5'b00000;
		//codesComputed = 'd0;
		carryoutRes = 'd0;
		overflowRes = 'd0;
		//codesComputed = 'd1;
		//result = 16'd0;

		
		case(aluOp)
			'd0:									//CMP
					begin
						//codesComputed = 1;
						result = a - b; 	
						if (a == b) begin
							conCodes[3] = 1;					// check zero
						end
						if ($signed(a) < $signed(b) ) begin
							conCodes[4] = 1;					// check negative
						end
						if (a < b ) begin						// check Lower
							conCodes[1] = 1;
						end
						overflowRes = ($signed(a) - $signed(b)); 		// check flag
						if (($signed(a) < 0) != ($signed(b) < 0)) begin						// NOTE: be wary of $signed in non tb
							conCodes[2] = 1;
						end
						carryoutRes = (a - b);
						if ((a < 0) != (b < 0)) begin						// check carry
							if ((b < 0) == (carryoutRes < 0)) begin
								conCodes[0] = 1;
							end
						end
					end//CMP
			'd1: begin
				result = a & b;							// AND
				conCodes = 5'd0;
			end
			'd2: begin
				result = a | b; 							// OR
				conCodes = 5'd0;
			end
			'd3: begin
				//codesComputed = 1;
				result = a + b;						// ADD
				conCodes = 5'd0;
				overflowRes = ($signed(a) - $signed(b)); 		// check flag
				if (($signed(a) < 0) != ($signed(b) < 0) && ($signed(overflowRes) < 0)) begin						// NOTE: be wary of $signed in non tb
					conCodes[2] = 1'b1;
				end
				carryoutRes = (a - b);
				if ((a < 0) != (b < 0)) begin						// check carry
					if ((b < 0) == (carryoutRes < 0)) begin
						conCodes[0] = 1;
					end
				end
			end
			'd4: begin 
				//codesComputed = 1;
				result = a + b + c;		// ADDC
				conCodes = 5'd0;
				overflowRes = ($signed(a) - $signed(b)); 		// check flag
				if (($signed(a) < 0) != ($signed(b) < 0) && ($signed(overflowRes) < 0)) begin						// NOTE: be wary of $signed in non tb
					conCodes[2] = 1;
				end
				carryoutRes = (a - b);
				if ((a < 0) != (b < 0)) begin						// check carry
					if ((b < 0) == (carryoutRes < 0)) begin
						conCodes[0] = 1;
					end
				end
			end
			'd5: begin
				//codesComputed = 1;
				result = ($signed(a)) - ($signed(b)); 						// SUB
				conCodes = 5'd0;
				overflowRes = ($signed(a) - $signed(b)); 		// check flag
				if (($signed(a) < 0) != ($signed(b) < 0)) begin						// NOTE: be wary of $signed in non tb
					conCodes[2] = 1;
				end
				carryoutRes = (a - b);
				if ((a < 0) != (b < 0)) begin						// check carry
					if ((b < 0) == (carryoutRes < 0)) begin
						conCodes[0] = 1;
					end
				end
			end
			'd6: begin
				//codesComputed = 1;
				result = a - b - c;		// SUBC
				conCodes = 5'd0;
				overflowRes = ($signed(a) - $signed(b)); 		// check flag
				if (($signed(a) < 0) != ($signed(b) < 0)) begin						// NOTE: be wary of $signed in non tb
					conCodes[2] = 1;
				end
				carryoutRes = (a - b);
				if ((a < 0) != (b < 0)) begin						// check carry
					if ((b < 0) == (carryoutRes < 0)) begin
						conCodes[0] = 1;
					end
				end
			end
			'd7: begin
				result = a ^ b;						// XOR
				conCodes = 5'd0;
			end
			'd8: begin 
				result = a * b;						// MUL
				conCodes = 5'b00000;
			end
			'd9: begin									
				result = ~b;							// NOT b/src
				conCodes = 5'd0;
			end
			default: begin
				result = 0;
				conCodes = 5'b00000;
			end
		endcase
		

	end
endmodule