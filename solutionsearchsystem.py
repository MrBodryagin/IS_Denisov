from wm import WorkingMemory as wm
from kb import KnowledgeBase as kb

class SolutionSearchSystem:
    def __init__(self, working_memory: wm, knowledge_base: kb) -> None:
        self.working_memory = working_memory
        self.knowledge_base = knowledge_base
        self.delete_rules = []
        self.explanation = ''
        self.num_iteration = 1

    def listIn(self, list1: list, list2: list) -> bool:
        for el in list1:
            if el not in list2:
                return False
        return True

    
    def get_and_delete_explanation(self):
        text = self.explanation
        self.explanation = ''
        self.explanation = 1
        return text


    
    def search_solution(self):
        self.explanation += f'Итерация №{self.num_iteration}\n'
        self.num_iteration += 1
        self.explanation += f'Рабочая память: {", ".join(self.working_memory.working_memory)}\n'
        max_count_conditions = 0
        conflict_indeces = []
        max_index = 0
        for i, rule in enumerate(self.knowledge_base.rules_list):
            if self.listIn(rule[0], self.working_memory.working_memory) and i not in self.delete_rules:
                conflict_indeces.append(i + 1)
                if len(rule[0]) > max_count_conditions:
                    max_index = i
                    max_count_conditions = len(rule[0])
        self.working_memory.add(self.knowledge_base.rules_list[max_index][1])
        # self.knowledge_base.rules_list.pop(max_index)
        self.delete_rules.append(max_index)

        if conflict_indeces == []: 
            self.explanation += "Конфликтный набор: empty\n"
        else: 
            self.explanation += f"Конфликтный набор: {', '.join([str(ind) for ind in conflict_indeces])}\n"
            self.explanation += f'Разрешение конфликта: {max_index + 1}\n\n'

        return conflict_indeces == []


        