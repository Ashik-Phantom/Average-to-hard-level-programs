# LED Flash Pattern
"""
In an NxN LED light matrix, each LED has a lumen (how bright an LED is). The NxN LED matrix has a pattern to flash, which is given below.
- Initially, all the LEDs flashing in the matrix (at t = 1). Then it changes the flashing mode every second.
- At t = 2, all the LEDs in the last row and the last column will not flash.
- At t = 3, all the LEDs in the first row and the first column will not flash.
- At t = 4, all the LEDs in the last two rows and the last two columns will not flash.
- At t = 5, all the LEDs in the first two rows and the first two columns will not flash.Similarly, the LEDs in the matrix are flashing.
It will repeat the flashing pattern when all the LEDs not flashing at a time.The lumen value of each LED in the matrix is passed as the input to the program. 
The program must print the highest lumen of the LED at every second in the above-mentioned flashing pattern.

Boundary Condition(s):2 <= N <= 100
1 <= Each matrix element <= 10^8
Input Format:The first line contains N.The next N lines, each contains N integers separated by a space.Output Format:The first line contains the highest lumen of the LED at every second in the matrix separated by a space.Example Input/Output 1:Input:41 2 8 46 3 4 15 6 7 29 3 4 9Output:9 8 9 6 9 1 9Explanation:At t = 1, the lumen values of the flashing LED's are given below.1 2 8 46 3 4 15 6 7 29 3 4 9Here 9 is the highest lumen value.At t = 2, the lumen values of the flashing LEDs are given below.1 2 86 3 45 6 7Here 8 is the highest lumen value.At t = 3, the lumen values of the flashing LEDs are given below.3 4 16 7 23 4 9Here 9 is the highest lumen value.At t = 4, the lumen values of the flashing LEDs are given below.1 26 3Here 6 is the highest lumen value.Similarly, at t = 5, 9 is the highest lumen value.At t = 6, 1 is the only highest lumen value.At t = 7, 9 is the only highest lumen value.At t = 8, the pattern ends as all the LEDs not flashing at this time.Hence the output is9 8 9 6 9 1 9Example Input/Output 2:Input:567 82 13 18 7691 43 25 79 5299 31 37 51 5395 82 67 54 8339 23 92 61 84Output:99 99 92 99 92 91 84 67 84
""
