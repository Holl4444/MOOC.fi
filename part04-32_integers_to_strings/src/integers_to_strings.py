# Write your solution here
def formatted(float_list: list[float]) -> list[str]:
    return [f'{x:.2f}' for x in float_list]

if __name__  ==  '__main__':
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))