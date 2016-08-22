__author__ = 'Dianlei Zhang'


question = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(question, answer):
    print('what is your {0}? It is {1}.'.format(q, a))
