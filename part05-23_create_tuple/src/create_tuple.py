# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple:
    return (min(x, y, z), max(x, y, z), sum([x, y, z]))

# Time complexity: O(1)
# Spce complexity: O(1)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

