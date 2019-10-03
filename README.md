# JCC - Jake's C Compiler

## Reference Documents

<https://norasandler.com/2017/11/29/Write-a-Compiler.html>
<http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf>
<http://www.wilfred.me.uk/blog/2014/08/27/baby-steps-to-a-c-compiler/>
<http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf>
<http://effbot.org/zone/simple-top-down-parsing.htm#summary>
<https://dl.acm.org/citation.cfm?doid=512927.512931>

## Progress

### TODO

* strings, comments, and line numbers in tokenizer
* Parser
* Generator

### Currently Implemented Syntax (almost)

```properties
<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <int>
```

### Statements to be implemented

1. expression statements
2. compound statements
3. selection statements
4. iteration statements
5. jump statements
6. declaration statements
7. try blocks
8. atomic and synchronized blocks (TM TS)

## Testing markdown syntax starts here

**Bold**
*Italic*
~~strike~~
new line now  
this is the newline

[URL to google](www.google.com)

### test table

Column1 | Column 2
--------|---------
cell1   |cell2
cell3   |cell4

```python
def foo(blah):
    this_is_some_code()
```

* [x] task2
* [ ] task3
* [ ] task 4 assigned to @jkub6
* [x] task5

This should be some `inline_code()` right here.

here is a block quote:
> Once upon a time  
> blah blah blah  
> the end

image:
![Test image should be here](https://homepages.cae.wisc.edu/~ece533/images/airplane.png)

ordered list:

1. item1
2. some other item
3. blah
4. blah

math:
$$
\int_{-\infty}^\infty
    f(\phi),d\phi
$$

The end
