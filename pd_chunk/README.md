# Pandas Chunk Manipulation

Creating and manipulating 'chunks'/sections of pandas by row

### Table of Contents

 1. Installation
 2. Motivation
 3. File Descriptions
 4. Example
 5. Issues
 6. Licensing, Authors, and Acknowledgements

## 1. Installation

To get this initial code running, you will only need the standard Anaconda
distribution of Python 3.

## 2. Motivation

Starting with a basic row_insert I built up to a class object with some pandas
row manipulation. This was however mainly an exercise in

## 3. File Descriptions
pandas_chunk: contains the `chunk_manipulate` class with the following functions

`chunk()`         - Creates a 'chunk' of rows from a DataFrame
`row_insert()`    - Inserts rows with identical columns into a DataFrame
`multiply_rows()` - Copies rows and pastes them back into its DataFrame at index

## 4. Example
Example use of `row_insert()`
```
numbers = [[1,2,3],[2,3,4],[3,3,3],[5,6,7]]
numbers2 = [[9,9,9]]

df = pd.DataFrame(numbers, columns = ['a','b','c'])
df_new = pd.DataFrame(numbers2, columns = ['a','b','c'])
```
>df:
  a	b	c
0	1	2	3
1	2	3	4
2	3	3	3
3	5	6	7

>df_new:
  a	b	c
0	9	9	9
```

new_chunk = chunk_manipulate(df)
new_chunk.row_insert(df_new, 2)

>>
  a b	c
0	1	2	3
1	2	3	4
2	9	9	9
3	3	3	3
4	5	6	7
```

## 5. Issues
Would like to eventually add the ability to transform or manipulate a chunk with
a function from another package having required the need of it once before.

## 6. Licences
Copyright (c) 2020 Ben Stone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
