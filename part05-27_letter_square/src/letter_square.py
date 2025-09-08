# # Write your solution here
# from collections import deque

# num = int(input('Layers: '))

# # Use ascii table to get the first letter as a capital. chr() turns ints into letters
# def get_first_line(num: int):
#     letter = chr(num + 64)
#     length = num * 2 - 1
#     first_line = letter * length
#     return first_line

# # Get the next letter, build its substring and insert into what we have so far
# # ord() turns letters into their ascii int values
# def build_line(last_line: str, current_index: int):
#     next_letter = chr(ord(last_line[current_index]) - 1)
#     current_index += 1
#     sub_str = next_letter * (len(last_line) - 2 * current_index)
#     next_line = last_line[: current_index] + sub_str + last_line[-current_index:]
#     return next_line
 
# def print_lines(start_line: str, num):
#     print(start_line)
#     used_lines = deque([start_line])
#     current_line = start_line
#     for i in range(num - 1):
#         next_line = build_line(current_line, i)
#         print(next_line)
#         current_line = next_line
#         if i < num - 2:
#             used_lines.appendleft(next_line)
#     for line in used_lines:
#         print(line)
    


# print_lines(get_first_line(num), num)

# num = int(input('Layers: '))

# def get_longest_alph(num: int) -> str:
#     string = ''.join([chr(i) for i in range(65, num + 65)])
#     return string

# def get_whole_line(string: str) -> str:
#     # remove doubled 'A'
#     reversed = string[::-1][: -1]
#     return reversed + string

# def replace_letter(string: str, index: int) -> str:
#     letter = string[index]
#     new_letter = chr(ord(letter) + 1)
#     new_string = ''.join([new_letter if char == letter else char for char in string])
#     return new_string

# def get_lines(num: int) -> str:
#     layers = []
#     current_line = get_longest_alph(num)
    
#     for index in range(num):
#         whole_line = get_whole_line(current_line)
#         layers.append(whole_line)
#         next_line = replace_letter(current_line, index)
#         current_line = next_line
#     return layers

# def print_lines(layers: list[str]):
#     for layer in layers[:0:-1]:
#         print(layer)
#     for layer in layers:
#         print(layer)

# layers = get_lines(num)
# print_lines(layers)
    



# if __name__ == '__main__':
#    num = 3
#    main(num)

##AI## ->

# layers = int(input("Layers: "))
   

# size = layers * 2 - 1
# for i in range(size):
#     row = []
#     for j in range(size):
#         # The "distance" from the edge determines the letter
#         dist = min(i, j, size - 1 - i, size - 1 - j)
#         letter = chr(ord('A') + layers - 1 - dist)
#         row.append(letter)
#     print(''.join(row))
