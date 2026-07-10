import sys, os
from dotenv import load_dotenv
load_dotenv()
sys.path.append('.')
from agent_core.memory import MemoryManager
mem = MemoryManager(user_id='personal_user')
print('Get all before:', mem.get_all(agent_id='default_user'))
res = mem.add('I love programming', agent_id='default_user')
print('Add success:', res)
print('Get all after:', mem.get_all(agent_id='default_user'))
