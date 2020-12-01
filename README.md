# py_oneliner
![Licence](https://img.shields.io/github/license/fuzailpalnak/py_oneliner)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![Downloads](https://pepy.tech/badge/py-oneliner)

A Library build with a propose, single line console print across project to avoid unnecessary console prints.
The Library has the capability to handle all print statements in one line across the project.

When there are several tasks to be looped, which also have their own sub task,
and these sub task have to be looped over, Therefore, knowing the status of each loop, during execution
is essential, or, knowing where the code has reached for that matter, keeping all that in mind, the library is design
to just display the sequence of execution in one-line console print, so user is aware about the progress.

![demo4](https://user-images.githubusercontent.com/24665570/96991506-29e99500-1546-11eb-8180-195bb5334c8b.gif)

## Installation
    
    pip install py-oneliner

## Usage

### One Line Print   
```python
from py_oneliner import one_liner
one_liner.one_line(tag="TEST", tag_data="TESTING PRINT")
``` 

## One Line Print with Reset  
`to_reset_data` will reset the fused print statement when specified `tag` is encountered
 
```python
from py_oneliner import one_liner
one_liner.one_line(tag="TEST", tag_data="TESTING PRINT", to_reset_data=True)
``` 

## Example

#### WithOut Color

```python
from py_oneliner import one_liner
Stages = ["Start", "Middle", "End"]

for s in Stages:
    one_liner.one_line(tag=s, tag_data=s, to_reset_data=True)

    for i, j1 in enumerate(2 * [1]):
        one_liner.one_line("first_loop", f"{i + 1}/{2}")

    for i, j1 in enumerate(3 * [1]):
        one_liner.one_line(
            "second_loop", f"{i + 1}/{3}"
        )
        for x, y in enumerate(2 * [1]):
            one_liner.one_line(
                "second_loop_nested_1",
                f"{x + 1}/{2}",
            )
```
![demo1](https://user-images.githubusercontent.com/24665570/96997734-f0b62280-154f-11eb-9066-1031f9719599.gif)


#### With Color

```python
from py_oneliner import one_liner
Stages = ["Start", "Middle", "End"]

for s in Stages:
    one_liner.one_line(tag=s, tag_data=s, to_reset_data=True)

    for i, j1 in enumerate(2 * [1]):
        one_liner.one_line("first_loop", f"{i + 1}/{2}", tag_color="red", tag_data_color="green")
    for i, j1 in enumerate(3 * [1]):
        one_liner.one_line(
            "second_loop", f"{i + 1}/{3}", tag_color="yellow", tag_data_color="grey"
        )
        for x, y in enumerate(2 * [1]):
            one_liner.one_line(
                "second_loop_nested_1",
                f"{x + 1}/{2}",
                tag_color="magenta",
                tag_data_color="cyan"
            )

```
![demo2](https://user-images.githubusercontent.com/24665570/96997880-396ddb80-1550-11eb-912f-276a574b09de.gif)

