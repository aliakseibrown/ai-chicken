from collections import Counter

def tree_learn(examples, attributes, default_class):
    if len(examples) == 0:
        return default_class
    
    if all(examples[0][-1] == example[-1] for example in examples):
        return examples[0][-1]
    
    if len(attributes) == 0:
        class_counts = Counter(example[-1] for example in examples)
        majority_class = class_counts.most_common(1)[0][0]
        return majority_class
    
    # Choose the attribute A as the root of the decision tree
    A = select_attribute(attributes, examples)
    
    tree = {A: {}}
    new_attributes = [attr for attr in attributes if attr != A]
    new_default_class = Counter(example[-1] for example in examples).most_common(1)[0][0]
    
    for value in get_attribute_values(A):
        new_examples = [example for example in examples if example[attributes.index(A)] == value]
        subtree = tree_learn(new_examples, new_attributes, new_default_class)
        tree[A][value] = subtree
    
    return tree

# Helper function: Select the best attribute based on a certain criterion (e.g., information gain)
def select_attribute(attributes, examples):
    # Implement your attribute selection criterion here
    pass

# Helper function: Get the possible values of an attribute from the examples
def get_attribute_values(attribute):
    # Implement your code to retrieve the attribute values from the examples here
    pass

# Example usage with coordinates
examples = [
    [1, 2, 'A'],
    [3, 4, 'A'],
    [5, 6, 'B'],
    [7, 8, 'B']
]

attributes = ['x', 'y']
default_class = 'unknown'

decision_tree = tree_learn(examples, attributes, default_class)
print(decision_tree)