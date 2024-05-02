from itertools import combinations

# Task A
# Task 1
def count_sets(key, data):
    count = 0
    for transaction in data:
        if set(key).issubset(transaction):
            count += 1
    return count

# Task 2
def getUnion(itemSet, length):
    union_set = []
    for i in range(len(itemSet)):
        for j in range(i+1, len(itemSet)):
            t1 = 1
            for k in range(len(itemSet[i])-1):
                 if itemSet[i][k] != itemSet[j][k]:
                     t1 = 0
            t = set(itemSet[i]).union(set(itemSet[j]))
            if len(t) == length and t1 == 1: union_set.append(list(t))
    return union_set

# Task 3
def generate_subsets(items):
    subsets = []
    for i in range(1, len(items)):
        subsets.extend(combinations(items, i))
    return subsets
print("Task A Task 1:")
print(count_sets(('a', 'b', 'c'), [['a', 'b', 'c', 'd'], ['b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']]))
print("\nTask A Task 2:")
print(getUnion([('a','b'),('a','c'),('b','c'),('b','d'),('c','d'),('c','e'),('c','f')],3))
print("\nTask A - Task 3:")
print(generate_subsets(['a', 'b', 'c']))


#Task B
from collections import Counter
from itertools import combinations

def generate_frequent_item_sets(data, min_support_count):
    # Initialize C1
    init = sorted(set(item for sublist in data for item in sublist))
    c = Counter()
    for item in init:
        for d in data:
            if item in d:
                c[item] += 1

    s = min_support_count
    l = Counter()
    for item, count in c.items():
        if count >= s:
            l[frozenset([item])] += count

    frequent_item_sets = [dict(l)]

    # Generating frequent item sets for higher levels
    pos = 1
    for count in range(2, len(init) + 1):
        nc = set()
        temp = list(l.keys())
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                t = temp[i].union(temp[j])
                if len(t) == count:
                    nc.add(temp[i].union(temp[j]))

        nc = list(nc)
        c = Counter()
        for i in nc:
            c[i] = 0
            for q in data:
                if i.issubset(set(q)):
                    c[i] += 1

        l = Counter()
        for item, count in c.items():
            if count >= s:
                l[frozenset(item)] += count

        if len(l) == 0:
            break

        frequent_item_sets.append(dict(l))
        pos = count

    return frequent_item_sets

def generate_association_rules(frequent_item_sets, min_confidence):
    association_rules = []
    for item_set in frequent_item_sets:
        for item, support_count in item_set.items():
            if len(item) > 1:
                for i in range(1, len(item)):
                    for antecedent in combinations(item, i):
                        antecedent = frozenset(antecedent)
                        consequent = item - antecedent
                        confidence = support_count / frequent_item_sets[len(antecedent) - 1][antecedent]
                        if confidence >= min_confidence:
                            association_rules.append((antecedent, consequent, support_count, confidence))
    return association_rules

data = [
    ["a", "b", "c"],
    ["a", "b"],
    ["a", "b", "d"],
    ["b", "e"],
    ["b", "c", "e"],
    ["a", "d", "e"],
    ["a", "c"],
    ["a", "b", "d"],
    ["c", "e"],
    ["a", "b", "d", "e"],
    ["a", 'b', 'e', 'c']
]

min_support_count = 3
min_confidence = 0.8

# Generate frequent item sets
frequent_item_sets = generate_frequent_item_sets(data, min_support_count)

# Generate association rules
association_rules = generate_association_rules(frequent_item_sets, min_confidence)

# Print association rules
print("Association Rules:")
for rule in association_rules:
    print(f"Rule: {rule[0]} -> {rule[1]}, Support Count: {rule[2]}, Confidence: {rule[3]}")
