from solutionsearchsystem import SolutionSearchSystem
from wm import WorkingMemory
from kb import KnowledgeBase
from explanation import Explanation


wm = WorkingMemory('facts.txt')
kb = KnowledgeBase('kb.txt')
explanation = Explanation()
sss = SolutionSearchSystem(wm, kb, explanation)


sss.execute_search()
    
    