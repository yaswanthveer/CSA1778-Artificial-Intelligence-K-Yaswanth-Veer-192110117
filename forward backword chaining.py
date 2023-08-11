print("K Yaswanth Veer 192110117")

class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = {}

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, consequent, antecedents):
        self.rules[consequent] = antecedents

    def forward_chaining(self):
        inferred_facts = set()
        queue = list(self.facts)

        while queue:
            fact = queue.pop(0)
            if fact in inferred_facts:
                continue
            
            inferred_facts.add(fact)
            
            if fact in self.rules:
                antecedents = self.rules[fact]
                if all(antecedent in inferred_facts for antecedent in antecedents):
                    queue.append(fact)
        
        return inferred_facts

    def backward_chaining(self, goal):
        inferred_facts = set()
        
        def backward_chain(fact):
            if fact in inferred_facts:
                return True
            
            if fact in self.facts:
                inferred_facts.add(fact)
                return True
            
            if fact in self.rules:
                antecedents = self.rules[fact]
                if all(backward_chain(antecedent) for antecedent in antecedents):
                    inferred_facts.add(fact)
                    return True
            
            return False
        
        return backward_chain(goal)

if __name__ == "__main__":
    kb = KnowledgeBase()
    
    kb.add_fact("has_feathers")
    kb.add_fact("lays_eggs")
    
    kb.add_rule("is_bird", ["has_feathers", "lays_eggs"])
    kb.add_rule("is_mammal", ["has_fur"])
    
    print("Forward Chaining:")
    inferred_facts_fc = kb.forward_chaining()
    print("Inferred Facts:", inferred_facts_fc)
    
    print("\nBackward Chaining:")
    goal_bc = "is_bird"
    if kb.backward_chaining(goal_bc):
        print(f"The goal '{goal_bc}' is satisfied.")
        print("Inferred Facts:", kb.inferred_facts)
    else:
        print(f"The goal '{goal_bc}' cannot be satisfied.")
