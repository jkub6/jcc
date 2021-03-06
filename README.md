# JCC - Jake's C Compiler

Development requirments: icarus-verilog

[Download precompiled exe here](https://github.com/jkub6/jcc/releases)

[JCC Dcumentation](https://jkub6.github.io/jcc) (todo)

Designed to compile from the C language into a custom (CR16-ish) ISA

Compiles from the C language into assembly, and can then assemble to a binary file.

[ISA for produced assembly](https://utah.instructure.com/files/92486303/download?download_frd=1)

## Usage

```console
$ ./jcc -h
usage: main.py [-h] [-c] [-a] [-l] [-A assembly_output_file]
               [-L cleaned_output_file] [-B binary_output_file]
               [-g glyph_folder] [-G glyph_output_file] [-p] [-r [0-3]] [-v]
               [input_file]

positional arguments:
  input_file            input file location

optional arguments:
  -h, --help            show this help message and exit
  -c, --compile         compile C file to assembly
  -a, --assemble        assemble input file to binary
  -l, --output_cleaned  output a file with the cleaned assembly
  -A assembly_output_file, --assemby_output assembly_output_file
                        assembly output file location
  -L cleaned_output_file, --cleaned_output cleaned_output_file
                        cleaned assembly output file location
  -B binary_output_file, --binary_output binary_output_file
                        binary output file location
  -g glyph_folder, --output_glyphs glyph_folder
                        Take in a folder of images to make glyphs
  -G glyph_output_file, --glyph_output glyph_output_file
                        glyph output file location
  -p, --label_glyphs    Label output glyphs as ascii charset
  -r [0-3], --readability [0-3]
                        level (0-3) of assembly code readability comments,
                        spacing, etc...
  -v, --verbose         enable verbose output
```

## Notes

* Does not currently short circuit logical operations
* currently only scope for compounds, functions, and files
* Need to add score for if statement? <- add test
* Continue in for loops may be broken <- add test
* add test for mul, xor, or, and, and shifts.
* test for BP differential in function call.
* globals only work above all functions

## Compiler Reference Documents

<https://norasandler.com/2017/11/29/Write-a-Compiler.html>  
<http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf>  
<http://www.wilfred.me.uk/blog/2014/08/27/baby-steps-to-a-c-compiler/>  
<http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf>  
<http://effbot.org/zone/simple-top-down-parsing.htm#summary>  
<https://dl.acm.org/citation.cfm?doid=512927.512931>
