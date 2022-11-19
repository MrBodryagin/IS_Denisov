class FactsAndResults:

    def __init__(self) -> None:
        self.fact_to_rules = dict()

    def add_string(self, string: str) -> None:
        string = string.strip().split('!')
        self.fact_to_rules[string[-2].replace('=>', '').strip()] = [rule.strip() for rule in string[:-2]]

    def read_file_with_rules(self, file_name: str) -> None:
        with open(file_name, 'r') as f:
            rules_string = f.read().split('\n')
            for rule_string in rules_string: 
                self.add_string(rule_string)


class Engine:
    
    def __init__(self) -> None:
        self.facts_dict = dict()

    def parse_user_data(self, file_name) -> None:
        with open(file_name, 'r') as f:
            facts_list= f.read().split('\n')
            for ind, fact_string in enumerate(facts_list):
                self.facts_dict[ind + 1] = [fact.strip() for fact in fact_string.split('!')[:-1]]

    
    def equals_condition(self, condition: list, facts: list) -> bool:
        for atom_condtion in condition:
            if atom_condtion not in facts:
                return False
        return True


    def computing_of_correct_fact(self, file_name: str, fact_to_rules: dict) -> str:
        with open(file_name, 'w') as f:
            for condition in self.facts_dict.keys():
                for fact in fact_to_rules.keys():
                    if self.equals_condition(self.facts_dict[condition], fact_to_rules[fact]):
                        f.write(f'{condition} --- {fact}\n')

        

someObject = FactsAndResults()
someObject.read_file_with_rules('text.txt')

engine = Engine()
engine.parse_user_data('user.txt')
engine.computing_of_correct_fact('result.txt', someObject.fact_to_rules)

# print(someObject.fact_to_rules)
