module dataPath(clk, memdata, instruction, aluControl, exMemResultEn, pcRegEn, srcRegEn, dstRegEn, immRegEn, signEn, 
					 regFileEn, pcRegMuxEn, srcSignOutEn, shiftALUMuxEn, irS, regImmMuxEn, srcData, dstData, adr, signOut, C, L, F, Z, N);
	input clk;
	input [15:0] instruction, memdata;
	input [3:0] aluControl;
	input pcRegEn, srcRegEn, dstRegEn, immRegEn, signEn, regFileEn, pcRegMuxEn, shiftALUMuxEn, regImmMuxEn, irS;
	input [1:0] srcSignOutEn, exMemResultEn;
	wire [3:0] src, dst, Rsrc, Rdest, OpCode, OpCodeExt;
	wire [15:0] result, exMemOrResult, shiftOrALU, regFileResult, pcOrReg, mux4Out, aluResult, regOrImm, shiftOut;
	wire [7:0] instImm, imm;
	output [15:0] srcData, dstData, adr, signOut;
	output C, L, F, Z, N;
	
	instructionRegister instructionRegister(.inst(instruction), .s(irS), .OpCode(OpCode), .Rdest(Rdest), .OpCodeExt(OpCodeExt), .Rsrc(Rsrc), .imm(instImm));
		
	register srcReg(.D({12'b0, Rsrc}), .En(srcRegEn), .clk(clk), .Q(src)); 
	register dstReg(.D({12'b0, Rdest}), .En(dstRegEn), .clk(clk), .Q(dst)); 
	register immReg(.D({8'b0, instImm}), .En(immRegEn), .clk(clk), .Q(imm)); 
	
	mux4 exMemOrResultMux(.d0(shiftOrALU), .d1(memdata), .d2(mux4Out), .d3(0), .s(exMemResultEn), .y(regFileResult));
	
	regfile regFile(.clk(clk), .regwrite(regFileEn), .ra1(src), .ra2(dst), .wd(regFileResult), .rd1(srcData), .rd2(dstData));
	
	signExtend signExtend(.in(imm), .s(signEn), .out(signOut));
	
	mux2 toAluMux(.d0(srcData), .d1(signOut), .s(srcSignOutEn), .y(mux4Out));
	
	alu ALU(.clk(clk), .a(mux4Out), .b(dstData), .aluControl(aluControl), .Cout(C), .Lout(L), .Fout(F), .Zout(Z), .Nout(N), .result(aluResult));
	
	mux2 regOrImmMux(.d0(srcData), .d1(signOut), .s(regImmMuxEn), .y(regOrImm));
	
	shifter shifter(.in(dstData), .s(regOrImm), .out(shiftOut));
	
	mux2 shiftOrALUMux(.d0(aluResult), .d1(shiftOut), .s(shiftALUMuxEn), .y(shiftOrALU));

endmodule 