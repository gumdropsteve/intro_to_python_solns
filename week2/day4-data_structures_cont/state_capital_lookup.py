state_dictionary = {'colorado': 'Denver', 'alaska': 'Juneau', 'california': 'Sacramento',
                    'georgia': 'Atlanta', 'kansas': 'Topeka', 'nebraska': 'Lincoln',
                    'oregon': 'Salem', 'texas': 'Austin', 'new york': 'Albany'}

state_input = input('Please input the name of a state to lookup: ')
state_name = state_input.lower()

if state_name in state_dictionary:
    print(state_dictionary[state_name])
else:
    print('{} capital unknown.'.format(state_input))
