module datapath #(parameter WIDTH = 16)
				(  input clk, reset, muxBin, muxPc, shiftOp,  
					input [1:0] muxExtImm, 
					input  instrRegEn, regFileEn, memDataRegEn, muxMemAdr, outRegEn,codesComputed,
					input [1:0] muxAin, muxToRegFile, muxShiftAmount, muxShiftShifter, muxOut, pcEn, 
					input [WIDTH-1:0] dataFromMem, pcLoad,
					input [4:0] aluOp,
					output wire [3:0] opCode, opCodeExt,
					output [WIDTH-1:0] dataToMem, adrToMem, conCodesOut);
					
wire [WIDTH-1:0] instrBus, dataToRegFile, immExtW, immExtFiveW, immExtSTW, memDataRegToMuxRegFileW, aW, bW;
wire [WIDTH-1:0]  destFromRegFW, srcFromRegFW, shiftAmountW, shiftShifterW, shiftedW;
wire [WIDTH-1:0]	aluOutW, toCodeCheckW, muxToOutRegW, outW, pcAddW, pcCountW;
wire [4:0] conCodesW;
wire [3:0] srcW, destW;
wire [7:0] immW;



register instrReg(dataFromMem, instrRegEn, clk, instrBus);

assign srcW = instrBus[3:0];
assign destW = instrBus[11:8];
assign immW = instrBus[7:0];

assign opCode = instrBus[15:12];
assign opCodeExt = instrBus[7:4];

// regfile will always write to whatever is in the dest instr or bits [11:8]
regfile regFile(clk, regFileEn, destW, srcW, destW, dataToRegFile, dataToMem, srcFromRegFW);
assign destFromRegFW = dataToMem; 	// needed for load and because reg type isnt assignable		

mux4 muxRegFile(memDataRegToMuxRegFileW,outW,pcCountW,16'b0,muxToRegFile, dataToRegFile); 

signExtender signExt(immW, immExtSTW);	

signExtender #(WIDTH,5) signExtForLSHI(immW[4:0], immExtFiveW);	// this is used in LSHI

mux4 muxExtendedImm(immExtSTW, immExtFiveW, {{8'd0},immW}, 16'd0, muxExtImm, immExtW);

register memDataReg(dataFromMem, memDataRegEn, clk, memDataRegToMuxRegFileW);

mux4 muxAIn(pcCountW,destFromRegFW,16'd1,16'd0,muxAin,aW); 

mux2 muxBIn(srcFromRegFW,immExtW,muxBin, bW); 

mux4 muxShiftShift(destFromRegFW, immExtW, srcFromRegFW, immExtFiveW, muxShiftShifter, shiftShifterW);

mux4 muxShiftAm(srcFromRegFW, immExtW, 16'd8, 16'd0, muxShiftAmount, shiftAmountW);

shifter Shifter(shiftShifterW, shiftAmountW, shiftOp, shiftedW);

alu ALU(aW, bW, aluOp, toCodeCheckW[0], aluOutW, conCodesW); // carry comes from the condition of Carry from last instr 

register codesRegister({{WIDTH-5{1'b0}},conCodesW}, codesComputed, clk, toCodeCheckW ); // extends the 5 bit output

condCheck conditionCheck(toCodeCheckW, destW, conCodesOut );	// destW is in the same spot as the conditions are

mux4 outMux(shiftedW, aluOutW, conCodesOut, 16'd0, muxOut, muxToOutRegW);

register OutReg(muxToOutRegW,outRegEn,clk,outW);

mux2 toPC(16'd1, outW, muxPc, pcAddW);

pc progcount(clk, reset, pcEn, pcAddW, pcLoad, pcCountW );

mux2 muxToMemory(pcCountW, srcFromRegFW, muxMemAdr, adrToMem );

endmodule


module pc #(parameter WIDTH = 16)
	(input clk, reset,
	input [1:0] en, // if 11 adds toAdd, if 01 loads pcload, if 10 loads toAdd, if 00 doesn't load anything
	input [WIDTH-1:0] toAdd, pcLoad,
	output reg [WIDTH-1:0] count);
	
	reg [1:0] littleCount;
	
	always @(posedge clk) begin
		if (reset) begin
			count <= 0;
		end
		case (en)
			2'b00: ;// nothing
			2'b01: count <= pcLoad;
			2'b10: count <= toAdd;
			2'b11: count <= count + toAdd;
		endcase
	
	end
	
endmodule



module shifter #(parameter WIDTH = 16) // TO DO: test when arith needs to be enables
			(input [WIDTH-1:0]shiftNum, shiftAmm,
			 input arith,
			 output reg [WIDTH-1:0]shifted);
	
			 
	reg signext;
	
	always @(*) begin
		if (arith) begin 		// arithmetic
			shifted = shiftNum <<< shiftAmm;	
		end
		else begin		 		// logical
			shifted = shiftNum << shiftAmm;
		end
	end
	
			 
				
endmodule




module mux2 #( parameter WIDTH = 16)
		(input [WIDTH - 1: 0] d0, d1,
		input op,
		output reg [WIDTH - 1: 0] out);
	always @(*) begin
		out = op ? d1 : d0;
	end
endmodule


module mux4 #(parameter WIDTH = 16)
             (input      [WIDTH-1:0] d0, d1, d2, d3,
              input      [1:0]       s, 
              output reg [WIDTH-1:0] y);

   always @(*)
      case(s)
         2'b00: y <= d0;
         2'b01: y <= d1;
         2'b10: y <= d2;
         2'b11: y <= d3;
      endcase
endmodule



module signExtender #(parameter WIDTH = 16, VALIDBITS = 8)
					( input [VALIDBITS-1:0] in,
					  output reg [WIDTH-1: 0] out);
	always @(*) begin
		out = {{(WIDTH - VALIDBITS){in[VALIDBITS - 1]}},in};
	end
		
endmodule


module condCheck #( parameter WIDTH = 16)
			( input [WIDTH-1:0] codes,
			input [3:0] condition,
			output reg [WIDTH-1:0] result);
	// codes[4] = negative,  codes[3] = zero,  codes[2] = flag
	// codes[1] = lower,     codes[0] = carry
	
	always @(*)
	begin
		case(condition)
			4'b0000:begin  // EQ:  equal
				result = codes[3] ? 16'd1 : 16'd0;
			end
			4'b0001:begin	// NE:  not equal
				result = codes[3] ? 16'd0 : 16'd1;
			end
			4'b1101:begin	// GE:  greater than or equal
				if (codes[4] | codes[3]) begin
					result = 16'd1;
				end
				else begin
					result = 16'd0;
				end
			end
			4'b0010:begin	// CS:  carry set
				result = codes[0] ? 16'd1 : 16'd0;
			end
			4'b0011:begin	// CC:  carry clear
				result = codes[0] ? 16'd0 : 16'd1;
			end
			4'b0100:begin	// HI:  higher than
				result = codes[1] ? 16'd1 : 16'd0;
			end
			4'b0101:begin	// LS:  lower than or same as
				result = codes[1] ? 16'd0 : 16'd1;
			end
			4'b1010:begin	// LO:  lower than
				if (~codes[1] & ~codes[3]) begin
					result = 16'd1;
				end
				else begin
					result = 16'd0;
				end
			end
			4'b1011:begin	// HS:  higher than or same as
				if (codes[1] | codes[3]) begin
					result = 16'd1;
				end
				else begin
					result = 16'd0;
				end
			end
			4'b0110:begin	// GT:  greater than
				result = codes[4] ? 16'd1 : 16'd0;
			end
			4'b0111:begin	// LE:  less than or equal
				result = codes[4] ? 16'd0 : 16'd1;
			end
			4'b1000:begin	// FS:  flag set
				result = codes[2] ? 16'd1 : 16'd0;
			end
			4'b1001:begin	// FC:  flag clear
				result = codes[2] ? 16'd0 : 16'd1;
			end
			4'b1100:begin	// LT:  less than
				if (~codes[4] & ~codes[3]) begin
					result = 16'd1;
				end
				else begin
					result = 16'd0;
				end
			end
			4'b1110:begin	// UC:  unconditonal
				result = 16'd1;
			end
			4'b1111:begin	// Never Jump
				result = 16'd0;
			end
			default:begin	
				result = 16'd0;
			end
		endcase
	end
endmodule

module register #(parameter WIDTH = 16)
			(input [WIDTH-1:0] in,
			 input en, clk,
			 output reg [WIDTH-1:0] data);

	always@( posedge clk) begin
		if (en) begin
			data <= in;
		end
	end

endmodule



