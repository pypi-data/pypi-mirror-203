# printbuddies

A few utilities to do terminal printing tricks. <br>
Install with:
<pre>pip install printbuddies</pre>

Contains one class and three functions: ProgBar, print_in_place, ticker, and clear.<br>

### ProgBar

ProgBar is a self-incrementing, dynamically sized progress bar.<br>
The progress counter and completion values can be manually overriden if desired.<br>
The width of the progress bar is set according to a ratio of the terminal width
so it will be resized automatically if the terminal width is changed.<br>
The display function has a 'return_object' parameter, allowing ProgBar to be used in comprehensions.<br>

<pre>
from printbuddies import ProgBar
total = 100
bar = ProgBar(total=total-1)
for _ in range(total):
    bar.display()
bar.reset()
my_list = [bar.display(return_object=i) for i in range(total)]
</pre>


### print_in_place

'print_in_place' erases the current line in the terminal and then writes the value of 
the 'string' param to the terminal.<br>
<pre>
from printbuddies import print_in_place
import time
#This will print numbers 0-99 to the terminal with each digit overwriting the last.
for i in range(100):
    print_in_place(i)
    time.sleep(0.1)
</pre>

### ticker

'ticker' prints a list of strings to the terminal with empty lines above and below
such that previous text in the terminal is no longer visible.<br>
Visually, It functions as a multi-line version of print_in_place.<br>
<pre>
from printbuddies import ticker
import time
#This will produce visually the same output as the above example
for i in range(100):
    ticker([i])
    time.sleep(0.1)
</pre>

### clear
A call to `printbuddies.clear()` simply clears the current line from the terminal.
