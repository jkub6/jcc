module statemachine(clk, reset, C, L, F, Z, N, instruction, aluControl, pcRegEn, srcRegEn, dstRegEn, immRegEn, signEn,
						regFileEn, pcRegMuxEn, srcSignOutEn, shiftALUMuxEn, regImmMuxEn, exMemResultEn, memread, memwrite, link, pcEn, irS, pcAdrMuxEn);
	input clk, reset, C, L, F, Z, N;
	input [15:0] instruction;
	output reg [3:0] aluControl;
	output reg pcRegEn, srcRegEn, dstRegEn, immRegEn, signEn, regFileEn, pcRegMuxEn, shiftALUMuxEn, regImmMuxEn, 
							memread, memwrite, link, irS, pcAdrMuxEn;
	output reg [1:0] srcSignOutEn, pcEn, exMemResultEn;
	reg [5:0] PS, NS;
	parameter [5:0] FETCH = 6'd0, DECODE = 6'd1, ADD = 6'd2, SUB = 6'd3, CMP = 6'd4, AND = 6'd5, OR = 6'd6, XOR = 6'd7, MOV = 6'd8, LOAD = 6'd9, STOR = 6'd10, 
						 JAL = 6'd11, JCOND = 6'd12, LSH = 6'd13, LSHI = 6'd14, S15 = 6'd15, BCOND = 6'd16, ANDI = 6'd17, ORI = 6'd18, XORI = 6'd19, ADDI = 6'd20,
						 SUBI = 6'd21, CMPI = 6'd22, MOVI = 6'd23, LUI = 6'd24;
						 
	always @(negedge reset, posedge clk) begin
		if (!reset) PS <= FETCH;
		else PS <= NS;
	end
	
	always@(clk, reset, instruction, PS) begin
		// initialize control signals
		{pcRegEn, srcRegEn, dstRegEn, immRegEn, signEn, regFileEn, pcRegMuxEn, 
		shiftALUMuxEn, regImmMuxEn, memread, memwrite, link, irS, pcAdrMuxEn} <= 1'd0;
		{srcSignOutEn, pcEn, exMemResultEn} <= 2'b0;
		aluControl <= 4'b0;
		NS <= 6'b0;
		
		case(PS)
			FETCH: begin // FETCH
				pcRegEn <= 1;
				memread <= 1;
				NS <= DECODE;
				if (instruction[7:4] == 4'b1011) // CMP
					aluControl <= 4'b0010;
			end
			
			DECODE: begin // DECODE
				case(instruction[15:12])
					4'b000: begin // Register
						if (instruction[7:4] == 4'b0101) begin // ADD
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= ADD;
						end
						else if (instruction[7:4] == 4'b1001) begin // SUB
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= SUB;
						end
						else if (instruction[7:4] == 4'b1011) begin // CMP
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= CMP;
						end
						else if (instruction[7:4] == 4'b0001) begin // AND
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= AND;
						end
						else if (instruction[7:4] == 4'b0010) begin // OR
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= OR;
						end
						else if (instruction[7:4] == 4'b0011) begin // XOR
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= XOR;
						end 
						else if (instruction[7:4] == 4'b1101) begin // MOV
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= MOV;
						end
					end
				
					4'b0100: begin // Special
						if (instruction[7:4] == 4'b0000) begin // LOAD
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= LOAD;
						end
						else if (instruction[7:4] == 4'b0100) begin // STOR
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= STOR;
						end
						else if (instruction[7:4] == 4'b1000) begin // JAL
							srcRegEn <= 1;
							dstRegEn <= 1;
							NS <= JAL;
						end
						else if (instruction[7:4] == 4'b1100) begin // Jcond
							srcRegEn <= 1;
							NS <= JCOND;
						end
					end

					4'b1000: begin //Shift
						if (instruction[7:4] == 4'b0100) begin // LSH
							NS <= LSH;
						end
						else if (instruction[7:4] == 4'b0000) begin // LSHI 
							NS <= LSHI;
						end
						else if (instruction[7:4] == 4'b0001) begin // LSHI
							NS <= S15;
						end
					end
					
					4'b1100: begin // Bcond
						NS <= BCOND;
					end
					
					4'b0001: begin // ANDI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= ANDI;
					end
					
					4'b0010: begin // ORI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= ORI;
					end
					
					4'b0011: begin // XORI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= XORI;
					end
					
					4'b0101: begin // ADDI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= ADDI;
					end
					
					4'b1001: begin // SUBI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= SUBI;
					end
					
					4'b1011: begin // CMPI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= CMPI;
					end
					
					4'b1101: begin // MOVI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= MOVI;
					end
					
					4'b1111: begin // LUI
						immRegEn <= 1;
						dstRegEn <= 1;
						irS <= 1;
						NS <= LUI;
					end
				endcase
			end
					
			ADD: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b1000;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			SUB: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b0001;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			CMP: begin 
				srcSignOutEn <= 0;
				aluControl <= 4'b0010;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;	
				NS <= FETCH;
			end
			
			AND: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b0011;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			OR: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b0100;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH;
			end
			
			XOR: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b0101;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH;
			end
			
			MOV: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				exMemResultEn <= 2'b10;
				NS <= FETCH;
			end
			
			LOAD: begin 
				regFileEn <= 1;
				memread <= 1;
				memwrite <= 0;
				exMemResultEn <= 2'b1;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			STOR: begin 
				regFileEn <= 0;
				memread <= 0;
				memwrite <= 1;
				exMemResultEn <= 2'b1;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			JAL: begin 
				// signals for jump
				pcEn <= 2'b10;
				// signals for storing link
				regFileEn <= 1;
				link <= 1;
				exMemResultEn <= 2'b1;
				pcAdrMuxEn <= 1;
				NS <= FETCH; 
			end
			
			JCOND: begin 
				pcEn <= 2'b01; // Initialize pcEn to pc += 1
				pcAdrMuxEn <= 1;
				case(instruction[11:8])
					4'b0000: // EQ Equal
						if (Z == 1)
							pcEn <= 2'b10;
					4'b0001: // NE Not Equal
						if (Z == 0)
							pcEn <= 2'b10;
					4'b1101: // GE Greater than or Equal
						if (N == 1 || Z == 1)
							pcEn <= 2'b10;
					4'b0010: // CS Carry Set
						if (C == 1)
							pcEn <= 2'b10;
					4'b0011: // CC Carry Clear
						if (C == 0)
							pcEn <= 2'b10;
					4'b0100: // HI Higher than
						if (L == 1)
							pcEn <= 2'b10;
					4'b0101: // LS Lower than or Same as
						if (L == 0)
							pcEn <= 2'b10;
					4'b1010: // LO Lower than
						if (L == 0 && Z == 0)
							pcEn <= 2'b10;
					4'b1011: // HS Higher than or Same as
						if (L == 1 || Z == 1)
							pcEn <= 2'b10;
					4'b0110: // GT Greater than
						if (N == 1)
							pcEn <= 2'b10;
					4'b0111: // LE Less than or Equal
						if (N == 0)
							pcEn <= 2'b10;
					4'b1000: // FS Flag Set
						if (F == 1)
							pcEn <= 2'b10;
					4'b1001: // FC Flag Clear
						if (F == 0)	
							pcEn <= 2'b10;
					4'b1100: // LT Less Than
						if (N == 0 && Z == 0)
							pcEn <= 2'b10;
					4'b1110: // UC Unconditional
						pcEn <= 2'b10;
					default:
						pcEn <= 2'b01;
				endcase
			end
			
			LSH: begin 
				regFileEn <= 1;
				srcSignOutEn <= 0;
				aluControl <= 4'b0111;
				shiftALUMuxEn <= 0;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			LSHI: begin 
				NS <= FETCH; 
			end
			
			S15: begin // LSHI
				NS <= FETCH; 
			end
			
			BCOND: begin 
				pcEn <= 2'b11;
				NS <= FETCH; 
			end
			
			ANDI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0011;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			ORI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0100;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH;
			end
			
			XORI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0101;
				shiftALUMuxEn <=0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH;
			end
			
			ADDI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b1000;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			SUBI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0001;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH; 
			end
			
			CMPI: begin 
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0010;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				NS <= FETCH;
			end
			
			MOVI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				exMemResultEn <= 2'b10;
				NS <= FETCH;
			end
			
			LUI: begin 
				regFileEn <= 1;
				srcSignOutEn <= 2'b01;
				aluControl <= 4'b0110;
				shiftALUMuxEn <= 0;
				irS <= 1;
				pcEn <= 2'b01;
				memread <= 1;
				NS <= FETCH;
			end					
		endcase
	end
endmodule
