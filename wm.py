class WorkingMemory:

    def __init__(self, file_name: str) -> None:
        self.working_memory = list()
        self.read_facts(file_name)

    
    def read_facts(self, file_name) -> None:
        with open(file_name, 'r') as f:
            text = f.read().replace('(', '').replace(')', '').split('\n')
            facts = [fact.strip() for fact in text]
            # facts = [fact.strip() for fact in f.read().split('\n')]
            self.working_memory = facts

    
    def add(self, facts_list: list) -> None:
        for fact in facts_list:
            self.working_memory.append(fact)


if __name__ == '__main__':
    wb = WorkingMemory('facts.txt')
    print(wb.working_memory)