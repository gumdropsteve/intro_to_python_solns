from our_class import OurClass
from member import Member
from instructor import Instructor

josh = Member('Josh', 'Brown', 'April 27th')
sean = Member('Sean', 'Brown', 'January 24th')
cary = Member('Cary', 'Brown', 'May 22nd')
thomas = Member('Thomas', 'Brown', 'September 12th')

members = [josh, sean, cary, thomas]

our_ds_class = OurClass('Data Science', 'Galvanize', members=members)

print('Initial Tests')
print('-' * 50)
print(our_ds_class.size) # Should be 4
print(our_ds_class.at_capacity) # Should be False.
print(our_ds_class.get_num_questions_asked()) # Should be 0.
print(our_ds_class.get_num_lines_code()) # Should be 0.
print

josh.add_question_asked('What are we doing here?')
sean.add_question_asked('What are we learning tonight?')
cary.add_question_asked('What if I have no questions?')

josh.add_coded_line('from collections import defaultdict')
josh.add_coded_line('my_int_dct = defaultdict(int)')
josh.add_coded_line('for num in range(2000): ')
josh.add_coded_line('my_int_dct[num] += 1')

sean.add_coded_line('from pandas import pd')
sean.add_coded_line('my_df = pd.read_csv("data/my_data.csv")')

print('First Round of tests')
print('-' * 50)
print(our_ds_class.get_num_questions_asked()) # Should return 3.
print(our_ds_class.get_num_lines_code()) # Should return 6.
print(josh.num_lines_coded) # Should be 4.
print(sean.num_lines_coded) # Should be 2.
print(cary.num_lines_coded) # Should be 0
print(our_ds_class.at_capacity) # Should be False.
print(josh.get_coding_level()) # Should return 'beginner'.
print

# Let's just say that josh type in the same line over and over again, so
# we can test out that our get_coding_level is working correctly.
for num in range(1000):
    josh.add_coded_line('print hello')

print('Second Round of tests')
print('-' * 50)
print(josh.num_lines_coded) # Should be 1004
print(josh.coding_level) # Should return 'intermediate'.
print

joe = Instructor('Joe')
james = Instructor('James')
judy = Instructor('Judy')
sandy = Instructor('Sandy')
instructors = [joe, james, judy, sandy]

our_ds_class.instructors = instructors

joe.add_question_answered('What are we doing here?')
joe.add_question_answered('What are we learning tonight?')

print('Third Round - Adding Instructor Tests')
print('-' * 50)
print(our_ds_class.get_num_questions_answered()) # Should return 2.
print(our_ds_class.check_outstanding_questions()) # Should return False
print

james.add_question_answered('What if I have no questions?')

print('Fourth Round - Adding more Instructor Tests')
print('-' * 50)
print(our_ds_class.get_num_questions_answered()) # Should return 3.
print(our_ds_class.check_outstanding_questions()) # Should return True.
