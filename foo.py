from pick import pick

title = 'Welcome to myClass!\n\nWhat would you like to do?'
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
option, index = pick(options, title, indicator='=>', default_index=2)
print(option, index)
