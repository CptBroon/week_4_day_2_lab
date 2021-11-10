import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
import os

os.system('psql -d task_manager -f db/task_manager.sql')

# task_repository.delete_all()
# user_repository.delete_all()

user_1 = User('Graeme', 'Brown')
user_repository.save(user_1)
user_repository.delete(1)

user_2 = User('Amanda', 'Hendrie')
user_repository.save(user_2)

user_2.last_name = 'Brown'
user_repository.update(user_2)

task1 = Task("Learn Python", user_2, 30)
task_repository.save(task1)

# task2 = Task('blah', 'Phil', 130)
# task_repository.save(task2)

# task1.description  = "use react native"
# task1.assignee = "steph"
# task1.mark_complete()
# task_repository.update(task1)

# task_repository.delete(2)

result = task_repository.select_all()

for task in result:
    print(task.__dict__)

# mytask = task_repository.select(2)




#  above is testing the CRUD for the table tasks

pdb.set_trace()