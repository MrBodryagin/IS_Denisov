from wm import WorkingMemory


class KnowledgeBase:

    def __init__(self, file_name) -> None:
        self.rules_list = list() # [[[conditions], [actions]], [[conditions], [actions]]]
        self.read_rules(file_name)

    
    def read_rules(self, file_name) -> None:
        with open(file_name, 'r') as f:
            text = f.read().split('\n')
            for line in text:
                line = line.split('=>')
                conditions = [condition.strip() for condition in line[0].replace('(', '').split(')')[:-1]]
                actions = [action.strip() for action in line[1].replace('(', '').split(')')[:-1]]
                self.rules_list.append([conditions, actions])


if __name__ == '__main__':
    kb = KnowledgeBase('kb.txt')
    print(kb.rules_list[3][1])