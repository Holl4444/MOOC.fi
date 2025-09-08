# Write your solution here
from string import ascii_uppercase

def calculate(operator: str, current_val: str, operand_val: str, var_dict: dict) -> int:
    current_val = int(current_val) if current_val.isdigit() else var_dict[current_val]
    operand_val = int(operand_val) if operand_val.isdigit() else var_dict[operand_val]
    
    op_set = {'ADD': current_val + operand_val, 'SUB': current_val - operand_val, 'MUL': current_val * operand_val}
    return op_set[operator]

def condition_passes(el1: int, symbol: str, el2: int) -> bool:
    conditional_ops = {'==': el1 == el2, '!=': el1 != el2, '<': el1 < el2, '<=': el1 <= el2, '>': el1 > el2, '>=': el1 >= el2}
    return conditional_ops[symbol]


def run(program: list):
    vars = {letter: 0 for letter in ascii_uppercase}
    output = []
    i = 0
    while True:
        if i == len(program):
            return output
        line = program[i].strip().split()
        command = line[0].strip()
        if command == 'END':
            return output

        if command == 'PRINT':
            value = int(line[1]) if line[1].isdigit() else vars[line[1]]
            output.append(value)
        elif command == 'MOV':
            var, value = line[1:]
            value = int(value) if value.isdigit() else vars[value]
            vars[var.strip()] = value
        elif command == 'ADD' or command == 'SUB' or command == 'MUL':
            var, value = line[1:]
            vars[var] = calculate(command, var, value, vars)
        elif 'JUMP' in line:
            jump_start = line.index('JUMP')
            sub_line = line[jump_start:]
            location = sub_line[1].strip()
            location_idx = program.index(location + ':')
            if jump_start == 0:
                # JUMP location index
                i = location_idx   
            else:                
                condition = line[:jump_start]
                condition1 = int(condition[1]) if condition[1].isdigit() else vars[condition[1]]
                condition3 = int(condition[3]) if condition[3].isdigit() else vars[condition[3]]
                if condition_passes(condition1, condition[2], condition3):
                    # JUMP to location index
                    i = location_idx             
        i += 1

# if __name__ == '__main__':
#     program4 = []
#     program4.append("MOV N 50")
#     program4.append("PRINT 2")
#     program4.append("MOV A 3")
#     program4.append("begin:")
#     program4.append("MOV B 2")
#     program4.append("MOV Z 0")
#     program4.append("test:")
#     program4.append("MOV C B")
#     program4.append("new:")
#     program4.append("IF C == A JUMP error")
#     program4.append("IF C > A JUMP over")
#     program4.append("ADD C B")
#     program4.append("JUMP new")
#     program4.append("error:")
#     program4.append("MOV Z 1")
#     program4.append("JUMP over2")
#     program4.append("over:")
#     program4.append("ADD B 1")
#     program4.append("IF B < A JUMP test")
#     program4.append("over2:")
#     program4.append("IF Z == 1 JUMP over3")
#     program4.append("PRINT A")
#     program4.append("over3:")
#     program4.append("ADD A 1")
#     program4.append("IF A <= N JUMP begin")
#     result = run(program4)
#     print(result)