# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    p1_average = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    p2_average = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    p3_average = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    smallest_average = min(p1_average, p2_average, p3_average)
    if smallest_average == p1_average:
        return person1
    if smallest_average == p2_average:
        return person2
    if smallest_average == p3_average:
        return person3
    return -1

if __name__ =='__main__':
    print(smallest_average({"name": "Mary", "result1": 2, "result2": 3, "result3": 3}, {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}, {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}))