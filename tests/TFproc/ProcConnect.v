module ProcConnect(clk, reset, loadedAdr, dataFromMem);
input clk, reset;
input [15:0] loadedAdr;
output [15:0] dataFromMem;

wire [15:0] adrToMem, dataFromMem, dataToMem;
wire memWrite, memRead;

Processor proc(clk, reset, dataFromMem, loadedAdr, memRead, memWrite, adrToMem, dataToMem);

procMem memory(~clk, 1'b1, memWrite, adrToMem, dataToMem, dataFromMem );

endmodule
