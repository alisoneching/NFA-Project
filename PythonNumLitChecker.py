class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        '''
        Constructor to initialize the attributes for the NFA

        :param states: finite set of states
        :param alphabet: set of input symbols
        :param transitions: dictionary of transition functions for each state to next set of states
        :param start_state: the start/initial state of machine
        :param accept_states: the set of accepting/final states'''
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def transition(self, char):
        '''
        Take in a character to transition to the next states
        
        :param char: the character input to transition to next states
        '''
        if (self.current_state, char) in self.transitions:
            self.current_state = self.transitions[(self.current_state, char)]
        else:
            self.current_state = None

    def is_accepting(self):
        '''
        Check if the current state is an accept state
        
        :return: bool True whether current state is in accept state and False if not
        '''
        return self.current_state in self.accept_states

    def process_input(self, input_string):
        '''
        Process input string for NFA to transition to next states

        :param input_string: the input string to be tested in language or not
        :return: bool whether or not NFA is accepting
        '''
        self.current_state = self.start_state   # reset the current state to the start state
        for char in input_string:
            if self.current_state is None:
                return False
            self.transition(char)
        return self.is_accepting()

states = {"q0", "q1", "q2", "q3", "q5", "q6", "q7"}
alphabet = set("0123456789_abcdefABCDEF")
transitions = {}

# Q0 TRANSITIONS (DEC, OCT, HEX)
transitions[("q0", "0")] = "q3"  # OCT and HEX must start with 0
for char in "123456789":
    transitions[("q0", char)] = "q1"

# Q1 TRANSITIONS (DEC)
for char in "0123456789":
    transitions[("q1", char)] = "q1"
transitions[("q1", "_")] = "q2"

# Q2 TRANSITIONS (DEC)
for char in "0123456789":
    transitions[("q2", char)] = "q1"

# Q3 TRANSITIONS (DEC, OCT, HEX)
transitions[("q3", "0")] = "q3"
transitions[("q3", "_")] = "q4"
for char in "oO":
    transitions[("q3", char)] = "q5"
for char in "xX":
    transitions[("q3", char)] = "q8"

# Q4 TRANSITIONS (DEC)
transitions[("q4", "0")] = "q3"

# Q5 TRANSITIONS (OCT)
transitions[("q5", "_")] = "q7"
for char in "01234567":
    transitions[("q5", char)] = "q6"

# Q6 TRANSITIONS (OCT)
for char in "01234567":
    transitions[("q6", char)] = "q6"
transitions[("q6", "_")] = "q7"

# Q7 TRANSITIONS (OCT)
for char in "01234567":
    transitions[("q7", char)] = "q6"

# Q8 TRANSITIONS (HEX)
transitions[("q8", "_")] = "q10"
for char in "0123456789abcdefABCDEF":
    transitions[("q8", char)] = "q9"

# Q9 TRANSITIONS (HEX)
for char in "0123456789abcdefABCDEF":
    transitions[("q9", char)] = "q9"
transitions[("q9", "_")] = "q10"

# Q10 TRANSITIONS (HEX)
for char in "0123456789abcdefABCDEF":
    transitions[("q10", char)] = "q9"

start_state = "q0"
accept_states = {"q1", "q3", "q6", "q9"}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)

def test_file_cases(nfa_instance, in_file, ans_file, out_file):
    '''
    Get strings from test file and puts through NFA

    :param nfa_instance: created NFA to run with
    :param in_file: input file path
    :param ans_file: expected answer file path
    :param out_file: output file path
    '''
    try:
        # read input file test cases
        with open(in_file, "r") as f:
            test_cases = f.readlines()

        # read the input file answers
        with open(ans_file, "r") as f:
            answers = [line.strip() for line in f.readlines()]

        actual_output = []
        comparisons = []

        print("-----------------------------")
        print("\nExpected Output (from 'in_ans.txt'):")
        for line in answers:
            print(line)

        print("\nRunning test cases from file...\n")
        print("-----------------------------")
        print("\nActual Output (with 'in.txt' as an input):")
        for test_string in test_cases:
            test_string = test_string.strip()
            if test_string:
                result = "accepted" if nfa_instance.process_input(test_string) else "rejected"
                actual_line = f"'{test_string}' -> {result}"
                actual_output.append(actual_line)
        
        # print acutal output
        for actual in actual_output:
            print(actual)

        # compare the output of the nfa to the expected output ("in_ans.txt")
        print("-----------------------------")
        print(f"\nComparisons written to '{out_file}':")
        for i, (actual, expected) in enumerate(zip(actual_output, answers), start=1):
            if actual == expected:
                comparison = f"{actual} PASS"
            else:
                comparison = f"{actual} FAIL"
            comparisons.append(comparison)

        with open(out_file, "w") as output_file:
            output_file.write("\n".join(comparisons))

        print("\nGoing back to menu...")
    except FileNotFoundError:
        print(f"Error: File not found.")

def test_user_input(nfa_instance):
    '''
    Get strings from user and puts through NFA
    
    :param nfa_instance: the NFA
    '''
    print("Enter strings to test (type 'exit' to exit):")
    while True:
        user_input = input("Enter a string: ").strip()
        if user_input.lower() == 'exit':
            print("\nGoing back to menu...")
            break
        result = "accepted" if nfa_instance.process_input(user_input) else "rejected"
        print(f"'{user_input}' -> {result}")

def main():
    while True:
        choice = input("\nRecognize Python Decimal Integer!\nPlease choose test input: \n(1) User Input Strings \n(2) Test File of Inputs \n(3) Exit\n").strip()

        if choice == '1':
            test_user_input(nfa)
        elif choice == '2':
            test_file_cases(nfa, file_path, "in_ans.txt", "out.txt")
        elif choice == '3':
            print("\nProgram exited.")
            break
        else:
            print("\nInvalid choice. Please enter '1', '2', or '3'")
ans_file = "in_ans.txt"
file_path = "in.txt"
main()
