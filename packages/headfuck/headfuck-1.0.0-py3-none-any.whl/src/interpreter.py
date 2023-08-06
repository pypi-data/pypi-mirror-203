import time
import os
import sys

# Get the absolute path to the directory containing your package
package_directory = os.path.abspath(os.path.dirname(__file__))

# Add the directory to sys.path
sys.path.insert(0, package_directory)

memory_size = 300
num_cells = 300
memory = [[0] * memory_size for _ in range(num_cells)]
pointer = (0, 0)
input_received = [False] * num_cells

def interpret(code):
    global pointer
    global input_received
    output_buffer = []
    output = ''
    input_mode = False
    i = 0
    while i < len(code):
        c = code[i]
        if c == '+':
            memory[pointer[0]][pointer[1]] = (memory[pointer[0]][pointer[1]] + 1) % 256
        elif c == '-':
            memory[pointer[0]][pointer[1]] = (memory[pointer[0]][pointer[1]] + 255) % 256
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
            output += '\n'.join([' '.join([str(x) for x in row[:10]]) for row in memory[:num_cells]])
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
        i += 1
    input_received = [False] * num_cells
    output = ''.join(output_buffer)
    return output

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

while True:
    code = input()
    result = interpret(code)
    print(result)
    quit()
