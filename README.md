# MSTC-CORE-TASK

Task:

Anuj is given a shuffled string made by randomly shuffling a special string.
A string is special only if it is formed by joining some special words any
number of times. Special words are mapping of numbers (0 <= number < 10)
to their words, for example, mapping of ‘0’ to ‘zero ',’ mapping of ‘1’ to ‘one,’
and so on.

Anuj is asked to convert the shuffled string to the smallest special number.
A special number is a number formed using numbers (0 <= number < 10)
without any leading zeros.
Anuj , who is not so good with numbers and strings, has asked for your
help.

INPUT

The first line of the input will contain T, number of test cases. For each test
case, there will be a, s shuffled string, on a separate line.

1 <= T <= 100

1 <= s.length <= 100000

OUTPUT

For each test case, on a new line, the smallest special number is in the
string format.
Some notes on output:
Shuffled string will always be able to convert into at least one valid special
string.
Shuffled string will only contain small English alphabets.
If a shuffled string contains only zeros, you should output “0”.

Sample Input

2

“ttnrwoooeeefurh”

“ewtooetzrowon”


Sample output

1234

1022
