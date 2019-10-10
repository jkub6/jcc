# JCC - Jake's C Compiler

Compiles from the C language into assembly, and can then assemble to a binary file.

 [ISA for produced assembly](https://utah.instructure.com/files/92486303/download?download_frd=1)

## Usage

```shell
$ ./jcc -h
usage: main.py [-h] [-c] [-a] [-l] [-A assembly_output_file]
               [-L cleaned_output_file] [-B binary_output_file] [-v]
               input_file

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
  -v, --verbose         enable verbose output
```

## Compiler Reference Documents

<https://norasandler.com/2017/11/29/Write-a-Compiler.html>
<http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf>
<http://www.wilfred.me.uk/blog/2014/08/27/baby-steps-to-a-c-compiler/>
<http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf>
<http://effbot.org/zone/simple-top-down-parsing.htm#summary>
<https://dl.acm.org/citation.cfm?doid=512927.512931>
