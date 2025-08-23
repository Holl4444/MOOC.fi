# Write your solution here
# def histogram(string: str) -> str:
    # histogram = { key: f'{"*" * string.count(key)}' for key in set(string)}
    # for key, value in histogram.items():
    #     print(f'{key} {value}')
#O(n * m)

def histogram(string: str) -> str:
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    for key in counts:
        print(f'{key} {'*' * counts[key]}')

    # O(n + m) as dictionaries are hash tables and O(1) (O(m)) per key access
    

if __name__ == '__main__':
    histogram('sausages')
    histogram('cat')
    histogram('abba')