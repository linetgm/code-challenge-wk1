# TOY PROBLEMS CODE CHALLENGE

## Description
This challenge consists of three separate problems that test your problem-solving and coding skills. The problems cover various aspects of handling time formats, integer manipulation, and string processing.

## Set-up
1. **Install Python**: Ensure you have Python installed on your machine. 
2. **Clone the Repository**: Clone this repository to your local machine using Git;
  ``` git clone https://github.com/linetgm/code-challenge-wk1.git```
3. **Navigate to the Project Directory**: Change your working directory to the cloned project folder;
    ```cd code-challenge-wk1```
4. **Run the code**:In the terminal;
    ```python3 challenges/challenge1.py``` for instance   

## Technology used
- Python

## Challenge 1
In this challenge, you are provided with a time in the 12-hour format (hour ranging from 1 to 12, minute from 0 to 59, and period "am" or "pm"). The goal is to convert this time into the 24-hour format and return it as a four-digit string.

The convert_to_24_hour function takes three arguments: hour, minute, and period. It first checks if the period is "pm" or "am". If it is, it adds 12 to the hour (except for 12 PM, which remains 12). If the period is "am", the function converts 12 AM to 0 hour, otherwise, it keeps the same hour. The function then formats the hour and minute with leading zeros (if needed) and combines them to form a four-digit string representing the time in 24-hour format.

## Challenge 2
In this challenge, you are given three integers a, b, and c. You need to determine if exactly two of these three integers are positive (greater than zero).

The positive_count function takes three integer arguments: a, b, and c. It calculates the sum of positive numbers among the three arguments using a generator expression and the sum function. If two of the integers are positive , the function returns True; otherwise, it returns False.

## Challenge 3
In this challenge, you are given a lowercase string consisting of alphabetic characters only. You need to find the highest value of consonant substrings. Consonants are defined as any letters of the alphabet except "aeiou", and each consonant has a corresponding value from a=1 to z=26.
The highest_consonant_value function takes a string s as input. It iterates through each character in the string and checks if the character is a consonant using the is_consonant function. If it's a consonant, the function calculates the value of the consonant using the get_consonant_value function and adds it to the current_value variable. The function also keeps track of the max_value, updating it whenever a higher value is encountered. If a vowel is encountered, the current_value is reset to 0. The function returns the max_value at the end, which represents the highest value of consonant substrings in the input string.


## License
MIT license
This project is licensed under the [MIT License] [2023] [Linet Muthii]
(https://opensource.org/licenses/MIT).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Author
Linet Muthii