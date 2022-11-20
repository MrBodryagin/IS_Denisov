from solutionsearchsystem import SolutionSearchSystem
from wm import WorkingMemory
from kb import KnowledgeBase


wm = WorkingMemory('facts.txt')
kb = KnowledgeBase('kb.txt')
sss = SolutionSearchSystem(wm, kb)


num_iter = 1
print(f'Итерация - {num_iter}')
while not sss.search_solution():
    num_iter += 1
    print(f'Итерация - {num_iter}')

with open('explanation.txt', 'w') as f:
    f.write(sss.get_and_delete_explanation())
    
    