module Processor #(parameter WIDTH = 16, REGBITS = 4) 
             (input              clk, reset, 
              input  [WIDTH-1:0] dataFromMem, loadedAdr,
              output             memRead, memWrite, 
              output [WIDTH-1:0] adrToMem, dataToMem);
			
wire muxBin, muxPc, shiftOp,  instrRegEn, regFileEn, memDataRegEn, muxMemAdr, outRegEn, codesComputed;
wire [1:0] muxAin, muxToRegFile, muxExtImm, muxShiftAmount, muxOut, pcEn, muxShiftShifter;
wire[WIDTH-1:0] conCodesOut;
wire[3:0] opCode, opCodeExt;
wire [4:0] aluOp;		
				  
controller cont(.clk(clk), .reset(reset), .conCodesOut(conCodesOut), .opCode(opCode), .opCodeExt(opCodeExt),
					.muxBin(muxBin), .muxPc(muxPc), .shiftOp(shiftOp), .muxExtImm(muxExtImm), .memRead(memRead),
					.memWrite(memWrite), .codesComputed(codesComputed), .instrRegEn(instrRegEn), .regFileEn(regFileEn), .memDataRegEn(memDataRegEn), 
					.muxMemAdr(muxMemAdr), .outRegEn(outRegEn), .muxAin(muxAin), 
					.muxToRegFile(muxToRegFile), .muxShiftAmount(muxShiftAmount), .muxOut(muxOut), .pcEn(pcEn), 
					.muxShiftShifter(muxShiftShifter), .aluOp(aluOp));
					
					
					
datapath dp( .clk(clk), .reset(reset), .muxBin(muxBin), .muxPc(muxPc), .shiftOp(shiftOp),  .muxExtImm(muxExtImm), 
				.instrRegEn(instrRegEn), .regFileEn(regFileEn), .memDataRegEn(memDataRegEn), .muxMemAdr(muxMemAdr), 
				.outRegEn(outRegEn), .codesComputed(codesComputed), .muxAin(muxAin), .muxToRegFile(muxToRegFile), .muxShiftAmount(muxShiftAmount), 
				.muxShiftShifter(muxShiftShifter), .muxOut(muxOut), .pcEn(pcEn), .dataFromMem(dataFromMem), .pcLoad(loadedAdr), .aluOp(aluOp), 
				.opCode(opCode), .opCodeExt(opCodeExt), .dataToMem(dataToMem), .adrToMem(adrToMem), .conCodesOut(conCodesOut));
										
endmodule

