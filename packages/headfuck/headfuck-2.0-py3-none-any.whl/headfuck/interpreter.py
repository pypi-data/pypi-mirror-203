memory_size = 3000
num_cells = 3000
memory = [[0] * memory_size for _ in range(num_cells)]
pointer = (0, 0)
input_received = [False] * num_cells
variable_memory = [0] * 10

import time
import os
import sys
import random

package_directory = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, package_directory)
variables = {}

def interpret(code):
    global pointer
    global variables
    global input_received
    output_buffer = []
    output = ''
    i = 0
    while i < len(code):
        c = code[i]
        if c == '+':
            memory[pointer[0]][pointer[1]] = (memory[pointer[0]][pointer[1]] + 1) % 256
        elif c == '-':
            memory[pointer[0]][pointer[1]] = (memory[pointer[0]][pointer[1]] + 255) % 256
        elif c == '*':
            memory[pointer[0]][pointer[1]] = (memory[pointer[0]][pointer[1]] * 2) % 256
        elif c == '>':
            pointer = (pointer[0], (pointer[1] + 1) % memory_size)
        elif c == '<':
            pointer = (pointer[0], (pointer[1] - 1 + memory_size) % memory_size)
        elif c == '^':
            pointer = ((pointer[0] - 1 + num_cells) % num_cells, pointer[1])
        elif c == 'v':
            pointer = ((pointer[0] + 1) % num_cells, pointer[1])
        elif c == '.': 
            output += chr(memory[pointer[0]][pointer[1]])
            print(chr(memory[pointer[0]][pointer[1]]), end='')
        elif c == ',':
            if not input_received[pointer[0]]:
                user_input = input("Enter a value: ")
                if len(user_input) > 0:
                    memory[pointer[0]][pointer[1]] = ord(user_input[0])
                    input_received[pointer[0]] = True
        elif c == '[':
            if memory[pointer[0]][pointer[1]] == 0:
                i = find_loop_end(code, i)
        elif c == ']':
            if memory[pointer[0]][pointer[1]] != 0:
                i = find_loop_start(code, i)
        elif c == '#':
            output += '\n'.join([' '.join([str(x) for x in row[:10]]) for row in memory[:10]])
            print('\n'.join([' '.join([str(x) for x in row[:10]]) for row in memory[:10]]))
        elif c == '/':
            memory[pointer[0]][pointer[1]] = 0
        elif c == '?':
            memory[pointer[0]][pointer[1]] = random.randint(0, 255)
        elif c == '!':
            filename = input("Enter file name: ")
            with open(filename, 'r') as f:
                input_string = f.read()
                interpret(input_string)
        elif c == '&':
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
            with open('output_' + timestamp + '.txt', 'w') as f:
                f.write(output)
                print("Output succesfully dumped to file.")
        elif c == ';':
            while True:
                interpret(code[i+1:])
        elif c == '=':
            variable_name = code[i+1]
            i += 1
            variables[variable_name] = memory[pointer[0]][pointer[1]]
        elif c == '@':
            variable_name = code[i+1]
            i += 1
            if variable_name in variables:
                memory[pointer[0]][pointer[1]] = variables[variable_name]
            else:
                print(f"Variable {variable_name} not defined")
        i += 1
    input_received = [False] * num_cells
    output = ''.join(output_buffer)
    return output

# def set_var(variable_index):
#     global variable_memory, pointer
#     variable_memory[variable_index] = memory[pointer[0]][pointer[1]]

# def get_var(variable_index):
#     global variable_memory, pointer
#     memory[pointer[0]][pointer[1]] = variable_memory[variable_index]

def find_loop_end(code,index):
    if code[index]!='[': raise Exception(f'Expected [ at index {index}')
    loop_counter=0
    for i in range(index+1,len(code)):
        if code[i]=='[': loop_counter+=1
        elif code[i]==']':
            if loop_counter==0: return i
            else: loop_counter-=1
    raise SyntaxError(f'Unmatched [ at index {index}')

def find_loop_start(code,index):
    if code[index]!=']': 
        raise SyntaxError(f'Expected ] at index {index}')
    loop_counter=0
    for i in range(index-1,-1,-1):
        if code[i]==']': loop_counter+=1
        elif code[i]=='[':
            if loop_counter==0:
                return i
            else: loop_counter-=1
    raise SyntaxError(f'Unmatched ] at index {index}')
if __name__ == "__main__":
    while True:
        code = input("Enter code: ")
        result = interpret(code)
        print(result)
        quit()
