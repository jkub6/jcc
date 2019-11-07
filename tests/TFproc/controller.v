module controller #(parameter WIDTH = 16)
					(input clk, reset, 
					input [WIDTH-1:0] conCodesOut,
					input [3:0] opCode, opCodeExt,
					output reg  muxBin, muxPc, shiftOp, muxExtImm, memRead, memWrite, codesComputed,
					output reg  instrRegEn, regFileEn, memDataRegEn, muxMemAdr, outRegEn,
					output reg  [1:0] muxAin, muxToRegFile, muxShiftAmount, muxOut, pcEn, muxShiftShifter,
					output reg  [4:0] aluOp);
					
reg [4:0] state, nextState;

always@(posedge clk) begin
	if (reset) begin
		state <= 'd0;
	end
	else begin
		state <= nextState;
	end
end


//always @(*) begin
//	case (state)
//	'd0: nextState <= 'd1;
//	'd1: 
//
//end


always @(*)
begin
	muxBin = 0;
	muxPc = 0;
	shiftOp = 0;
	muxExtImm = 0;
	memRead = 0;
	memWrite = 0;
	instrRegEn = 0;
	codesComputed = 0;
	regFileEn = 0;
	memDataRegEn = 0;
	muxMemAdr = 0;
	outRegEn = 0;
	muxAin = 'd0;
	muxToRegFile = 'd0;
	muxShiftAmount = 'd0;
	muxOut = 'd0;
	pcEn = 'd0;
	muxShiftShifter = 'd0;
	aluOp = 'd0;
	
	
	case (state)
		'd0:begin 	// state 0
			pcEn = 01; 
			nextState = 'd1;
		end
		
		'd1:begin	// sate 1
			muxMemAdr = 'd0;
			memRead = 'd1;
			instrRegEn = 'd1;
			nextState = 'd22;
		end
		
		'd2:begin	// state 2
			muxShiftShifter = 2;
			muxShiftAmount = 3;
			outRegEn = 1;
			nextState = 'd3;
		end
		
		'd3:begin	// sate 3
			muxToRegFile = 1;
			regFileEn = 1;
			pcEn = 'b11;
			nextState = 'd1;
		end
		
		'd4:begin	// state 4
			muxAin = 'd1;
			muxBin = 'd0;
			case (opCodeExt)
				4'b1011: begin 			// CMP
					aluOp = 'd0;
					codesComputed = 1;
				end
				4'b0001: aluOp = 'd1;	// AND
				4'b0010: aluOp = 'd2; 	// OR
				4'b0011: aluOp = 'd7;	//XOR
				4'b0101: begin				// ADD
					aluOp = 'd3;				
					codesComputed = 1;
				end
				4'b0110: begin				// ADDU
					aluOp = 'd4;				
					codesComputed = 1;
				end
				4'b0111: begin				// ADDC
					aluOp = 'd4;				
					codesComputed = 1;
				end
				4'b1001: begin				// SUB
					aluOp = 'd5;				
					codesComputed = 1;
				end
				4'b1010: begin				// SUBC
					aluOp = 'd6;				
					codesComputed = 1;
				end
				default: aluOp = 'd3;	// shouldnt happen
			endcase
			outRegEn = 1;
			muxOut = 1;
			nextState = 'd3;
		end
		
		'd5:begin	// state 5
			muxAin = 1;
			muxBin = 1;
			case (opCode)
				4'b1011: begin 			// CMP
					aluOp = 'd0;
					codesComputed = 1;
				end
				4'b0001: aluOp = 'd1;	// AND
				4'b0010: aluOp = 'd2; 	// OR
				4'b0011: aluOp = 'd7;	//XOR
				4'b0101: begin				// ADD
					aluOp = 'd3;				
					codesComputed = 1;
				end
				4'b0110: begin				// ADDU
					aluOp = 'd4;				
					codesComputed = 1;
				end
				4'b0111: begin				// ADDC
					aluOp = 'd4;				
					codesComputed = 1;
				end
				4'b1001: begin				// SUB
					aluOp = 'd5;				
					codesComputed = 1;
				end
				4'b1010: begin				// SUBC
					aluOp = 'd6;				
					codesComputed = 1;
				end
				default: aluOp = 'd3;	// shouldnt happen
			endcase
			outRegEn = 1;
			muxOut = 1;
			nextState = 'd3;
		end
		
		'd6:begin
			muxMemAdr = 1;
			memRead = 1;
			memDataRegEn = 1;
			nextState = 'd7;
		end
		
		'd7:begin
			//muxTOREgFile 0
			regFileEn = 1;
			pcEn = 'b11;
			nextState = 'd1;
		end
		
		'd8:begin
			muxMemAdr = 'd1;
			memWrite = 'd1;
			nextState = 'd9;
		end
		
		'd9:begin
			pcEn = 'b11;
			nextState = 'd1;
		end
		
		'd10:begin
			muxOut = 'd2;
			outRegEn = 'd1; 
			nextState = 'd3;
		end
		
		'd11:begin
			muxShiftAmount = 'd3;
			muxShiftShifter = 'd2;
			outRegEn = 1;
			nextState = 'd12;
		end
		
		'd12:begin
			muxPc = conCodesOut[0];
			pcEn = 'b10;
			nextState = 'd1;
		end
		'd13:begin
			muxShiftAmount = 'd3;
			muxShiftShifter = 'd2;
			outRegEn = 'd1;
			muxToRegFile = 'd2;
			regFileEn = 'd1;
			nextState = 'd21;
		end
		
		'd14:begin
			outRegEn =1;
			nextState = 'd3;
		end
		
		'd15:begin
			muxShiftAmount = 'd1;
			muxExtImm = 'd1;
			outRegEn = 'd1;
			nextState = 'd3;
		end
		
		'd16:begin
			shiftOp = 'd1;
			outRegEn = 'd1;
			nextState = 'd3;
		end
		
		'd17:begin
			muxShiftAmount = 'd3;
			muxShiftShifter = 'd1;
			outRegEn = 'd1;
			nextState = 'd18;
		end
		
		'd18:begin
			muxPc = conCodesOut[0];
			pcEn = 'b11;
			nextState = 'd1;
		end
		
		'd19:begin
			muxShiftAmount = 'd2;
			muxShiftShifter = 'd1;
			outRegEn = 'd1;
			nextState = 'd3;
		end
		
		'd20:begin
			muxShiftAmount = 'd3;
			muxShiftShifter = 'd1;
			outRegEn = 'd1;
			nextState = 'd3;
		end
		
		'd21:begin
			muxPc = 'd1;
			pcEn = 'b10;
			nextState = 'd1;
		end
		'd22:begin	// intermediate state that gives an extra clk cycle to get instuction
			case (opCode) 
				4'b0000: begin		// arithmetic and mov
					if (opCodeExt == 4'b1101)begin
						nextState = 'd2;
					end
					else begin
						nextState = 'd4;
					end
				end
				4'b0100: begin		// load stor jcond jal scond
					case(opCodeExt)
						4'b0000: nextState = 5'd6;
						4'b0100: nextState = 5'd8;
						4'b1101: nextState = 5'd10;
						4'b1100: nextState = 5'd11;
						default: nextState = 5'd13; // JAL TO ASK
					endcase
				end
				
				4'b1000: begin		// LSH LSHI SAR
					if (opCodeExt == 4'b0100) begin
						nextState = 'd14;
					end
					else if (opCodeExt == 4'b1000) begin
						nextState = 'd16;
					end
					else begin
						nextState = 'd15;
					end
				end
				
				4'b1100: begin		// Bcond
					nextState = 'd17;
				end
				
				4'b1111: begin		//LUI
					nextState = 'd19;
				end
				
				4'b1101: begin		// MOVI
					nextState  = 'd20;
				end
				
				default: begin		// immediate arithmetic
					nextState = 'd5;
				end
			endcase
		end
		default: nextState = 'd0;
	endcase
end

endmodule