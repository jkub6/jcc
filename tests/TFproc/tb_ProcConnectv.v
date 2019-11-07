module tb_ProcConnect();

reg clk, reset, regEn;
reg [15:0] loadedAdr, regIn;

wire [15:0]  dataFromMem, regData;

register TestReg(.in(regIn), .en(regEn), .clk(clk), .data(regData));

ProcConnect UUT(.clk(clk), .reset(reset), .loadedAdr(loadedAdr), .dataFromMem(dataFromMem));

initial begin
clk = 0;
reset = 1;
loadedAdr = 16'd0;
regIn = 16'd15;
#10;
regEn = 1;
#50;
reset = 0;
end 
		
always #5 clk = ~clk;	  

		
endmodule 