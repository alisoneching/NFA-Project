import re

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def reset(self):
        self.current_state = self.start_state

    def transition(self, char):
        if (self.current_state, char) in self.transitions:
            self.current_state = self.transitions[(self.current_state, char)]
        else:
            self.current_state = None

    def is_accepting(self):
        return self.current_state in self.accept_states

    def process_input(self, input_string):
        self.reset()
        for char in input_string:
            if self.current_state is None:
                return False
            self.transition(char)
        return self.is_accepting()

states = {"q0", "q1", "q2", "q3", "q5", "q6", "q7"}
alphabet = set("0123456789_")
transitions = {
    # Q0 TRANSITIONS (DEC, OCT, HEX)
    ("q0", "0"): "q3", # OCT and HEX must start with 0
    ("q0", "1"): "q1",
    ("q0", "2"): "q1",
    ("q0", "3"): "q1",
    ("q0", "4"): "q1",
    ("q0", "5"): "q1",
    ("q0", "6"): "q1",
    ("q0", "7"): "q1",
    ("q0", "8"): "q1",
    ("q0", "9"): "q1",

    # Q1 TRANSITIONS (DEC)
    ("q1", "0"): "q1",
    ("q1", "1"): "q1",
    ("q1", "2"): "q1",
    ("q1", "3"): "q1",
    ("q1", "4"): "q1",
    ("q1", "5"): "q1",
    ("q1", "6"): "q1",
    ("q1", "7"): "q1",
    ("q1", "8"): "q1",
    ("q1", "9"): "q1",
    ("q1", "_"): "q2",

    # Q2 TRANSITIONS (DEC)
    ("q2", "0"): "q1",
    ("q2", "1"): "q1",
    ("q2", "2"): "q1",
    ("q2", "3"): "q1",
    ("q2", "4"): "q1",
    ("q2", "5"): "q1",
    ("q2", "6"): "q1",
    ("q2", "7"): "q1",
    ("q2", "8"): "q1",
    ("q2", "9"): "q1",

    # Q3 TRANSITIONS (DEC, OCT, HEX)
    # DEC
    ("q3", "0"): "q3",
    ("q3", "_"): "q4",
    # OCT
    ("q3", "o"): "q5",
    ("q3", "O"): "q5",
    # HEX
    ("q3", "x"): "q8",
    ("q3", "X"): "q8",

    # Q4 TRANSITIONS (DEC)
    ("q4", "0"): "q3",

    # Q5 TRANSITIONS (OCT)
    ("q5", "_"): "q6",

    # Q6 TRANSITIONS (OCT)
    ("q6", "0"): "q7",
    ("q6", "1"): "q7",
    ("q6", "2"): "q7",
    ("q6", "3"): "q7",
    ("q6", "4"): "q7",
    ("q6", "5"): "q7",
    ("q6", "6"): "q7",
    ("q6", "7"): "q7",

    # Q7 TRANSITIONS (OCT)
    ("q7", "0"): "q7",
    ("q7", "1"): "q7",
    ("q7", "2"): "q7",
    ("q7", "3"): "q7",
    ("q7", "4"): "q7",
    ("q7", "5"): "q7",
    ("q7", "6"): "q7",
    ("q7", "7"): "q7",
    ("q7", "_"): "q6",

    # Q8 TRANSITIONS (HEX)
    ("q8", "_"): "q9",

    # Q9 TRANSITIONS (HEX)
    ("q9", "0"): "q10",
    ("q9", "1"): "q10",
    ("q9", "2"): "q10",
    ("q9", "3"): "q10",
    ("q9", "4"): "q10",
    ("q9", "5"): "q10",
    ("q9", "6"): "q10",
    ("q9", "7"): "q10",
    ("q9", "8"): "q10",
    ("q9", "9"): "q10",
    ("q9", "a"): "q10",
    ("q9", "b"): "q10",
    ("q9", "c"): "q10",
    ("q9", "d"): "q10",
    ("q9", "e"): "q10",
    ("q9", "f"): "q10",
    ("q9", "A"): "q10",
    ("q9", "B"): "q10",
    ("q9", "C"): "q10",
    ("q9", "D"): "q10",
    ("q9", "E"): "q10",
    ("q9", "F"): "q10",

    # Q10 TRANSITIONS (HEX)
    ("q10", "0"): "q10",
    ("q10", "1"): "q10",
    ("q10", "2"): "q10",
    ("q10", "3"): "q10",
    ("q10", "4"): "q10",
    ("q10", "5"): "q10",
    ("q10", "6"): "q10",
    ("q10", "7"): "q10",
    ("q10", "8"): "q10",
    ("q10", "9"): "q10",
    ("q10", "a"): "q10",
    ("q10", "b"): "q10",
    ("q10", "c"): "q10",
    ("q10", "d"): "q10",
    ("q10", "e"): "q10",
    ("q10", "f"): "q10",
    ("q10", "A"): "q10",
    ("q10", "B"): "q10",
    ("q10", "C"): "q10",
    ("q10", "D"): "q10",
    ("q10", "E"): "q10",
    ("q10", "F"): "q10",
    ("q10", "_"): "q9",

}

start_state = "q0"
accept_states = {"q1", "q3", "q7", "q10"}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)

# is_valid_string() method: returns boolean, TRUE if in an accept
#                           state, FALSE if not

def is_valid_string(input_string, nfa_instance):
    return nfa_instance.process_input(input_string)

# test_file_cases() method: gets strings from the test file as input
#                           and puts them through the NFA

def test_file_cases(nfa_instance, input_file_path, ans_file_path, output_file_path):
    try:
        # read input file test cases
        with open(input_file_path, "r") as input_file:
            test_cases = input_file.readlines()

        # read the input file expected answers
        with open(ans_file_path, "r") as answer_file:
            expected_answers = [line.strip() for line in answer_file.readlines()]

        actual_output = [] # so we can compare to the expected output
        comparisons = [] # this array will be written to the out.txt file

        print("-----------------------------")
        print("\nExpected Output (from 'in_ans.txt'):")
        for line in expected_answers:
            print(line)

        print("\nRunning test cases from file...\n")
        print("-----------------------------")
        print("\nActual Output (with 'in.txt' as an input):")
        for test_string in test_cases:
            test_string = test_string.strip()
            if test_string:
                result = "accepted" if is_valid_string(test_string, nfa_instance) else "rejected"
                actual_line = f"'{test_string}' -> {result}"
                actual_output.append(actual_line)
        
        # prints acutal output in a nice format
        for actual in actual_output:
            print(actual)

        # compare the output of the nfa to the expected output ("in_ans.txt")
        print("-----------------------------")
        print(f"\nComparisons written to '{output_file_path}':")
        for i, (actual, expected) in enumerate(zip(actual_output, expected_answers), start=1):
            if actual == expected:
                comparison = f"{actual} PASS"
            else:
                comparison = f"{actual} FAIL"
            comparisons.append(comparison)

        with open(output_file_path, "w") as output_file:
            output_file.write("\n".join(comparisons))

        print(f"Comparisons ")
        print("\nGoing back to menu...")
    except FileNotFoundError:
        print(f"Error: File not found.")

# test_user_input() method: gets strings from the user and puts
#                           them through the NFA

def test_user_input(nfa_instance):
    print("Enter strings to test (type 'exit' to exit):")
    while True:
        user_input = input("Enter a string: ").strip()
        if user_input.lower() == 'exit':
            print("\nGoing back to menu...")
            break
        result = "accepted" if is_valid_string(user_input, nfa_instance) else "rejected"
        print(f"'{user_input}' -> {result}")