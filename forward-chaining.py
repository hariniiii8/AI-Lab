class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def evaluate(self, facts):
        if all(condition in facts for condition in self.conditions) and self.conclusion not in facts:
            facts.add(self.conclusion)
            return True
        return False

class ForwardReasoningSystem:
    def __init__(self, rules):
        self.rules = rules
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chain(self):
        while True:
            updated = False
            for rule in self.rules:
                if rule.evaluate(self.facts):
                    updated = True
            if not updated:
                break

# Example knowledge base
knowledge_base_rules = [
    Rule(['has_feathers', 'can_fly'], 'bird'),
    Rule(['has_fur', 'gives_milk'], 'mammal'),
    Rule(['has_scales', 'lives_in_water'], 'fish'),
    Rule(['bird'], 'animal'),
    Rule(['mammal'], 'animal'),
    Rule(['fish'], 'animal'),
]

# Initialize the forward reasoning system with the knowledge base
frs = ForwardReasoningSystem(knowledge_base_rules)

# Add initial facts
frs.add_fact('has_feathers')
frs.add_fact('can_fly')

# Run forward chaining
frs.forward_chain()

# Query: Is a bird an animal?
query = 'bird'
result = query in frs.facts

# Print the resulting facts and the query result
print("Final facts:", frs.facts)
print(f"Is '{query}' an animal? {result}")
