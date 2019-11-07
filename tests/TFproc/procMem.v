module procMem #(parameter WIDTH = 16, RAM_adr_BITS = 16)
   (input clk, en,
    input memWrite,
    input [RAM_adr_BITS-1:0] adr,
    input [WIDTH-1:0] dataToMem,
    output reg [WIDTH-1:0] dataFromMem
    );

   reg [WIDTH-1:0] ram [(2**RAM_adr_BITS)-1:0];

 //initial

 // dat files in memory
 //$readmemh("test.dat", ram);
 //$readmemh("math_tests.dat", ram);
	//$readmemh("sub_another.dat", ram);
 
 // This "always" block simulates as a RAM, and synthesizes to a block
 // RAM on the Spartan-3E part. Note that the RAM is clocked. Reading
 // and writing happen on the rising clock edge. This is very important
 // to keep in mind when you're using the RAM in your system! 
   always @(posedge clk) begin
      if (en) begin
         if (memWrite)
            ram[adr] <= dataToMem;
      end
		dataFromMem <= ram[adr];
	end
						
endmodule