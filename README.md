# NFA-Project
## Python Numerical Literal Checker
**Team:** "Villagers"<br>
**Members:** <br>Alison Ching - github: @alisoneching
	<br>Stella Sinlao - github: @ssinlao

## Contents:
1. **Python-Numerical-Literal-NFA.jff** - JFLAP file of NFA that recognizes decimal integers, octal integers, and hexadecimal integers
2. **PythonNumLitChecker.py** - main code with NFA implementation
3. **nl.jpg** - jpg image of the NFA

## How to Use Code:
1. Run the code.
2. A menu will be displayed. Type a number 1, 2, or 3 to pick an option.
3. Option 1 will allow the user to input their own string and see if the NFA accepts or rejects it.
4. Option 2 will allow the user to see an input file "in.txt" and the expected output "in-ans.txt". 
   If the coded NFA works properly, all of the outputs will contain "PASS" in a new output file, "out.txt"
5. Option 3 will exit the program.

## Tasks:
1. Create NFA for decimal-integers on JFLAP (Stella)
2. Program "PythonNumLitChecker.py"
    - class NFA: (Stella)
	    - self, states, alphabet, transitions, start_state, accept_state (Stella)
      	    - expand NFA to recognize decimal-integers, octal-integers, and hexadecimal-integers (Stella)
    - def is_valid_string() (Alison)
    - def test_file_cases() (Alison)
    - def test_user_input() (Alison)
    - def main() (Alison)
3. Make txt files "in.txt" (input), "in_ans.txt" (expected results) (Alison and Stella)
