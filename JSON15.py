import pickle


def names():
    name = input("Привет, как тебя зoвут?")
    print("Привет, ", name)


bites = pickle.dumps(names)
print(bites)

'''with open('models.txt', 'w') as f:
    f.write('hello\n')
    f.write('hello\n')
    f.write('hello\n')
    f.write('I am so good for this\n')
    f.writelines(['1', '2', '3', '4', 'end\n'])'''

'''with open('models.txt', 'r') as f:
    result = f.read()
    print(result)'''

'''with open('models.txt', 'r') as f:
    result = f.readline()
    print(result)
    print('***************************************\n')
    result = f.readline()
    print(result)
    print('***************************************\n')
    result = f.readline()
    print(result)
    print('***************************************\n')
    result = f.readline()
    print(result)
    print('***************************************\n')
    result = f.readline()
    print(result)
    print('***************************************\n')'''

with open('models.txt', 'r') as f:
    result = f.readlines()
    print(result)

big_object = {

    'items': [
        "1",
        (2, 3),
        ['some', 'else'],
        {'op': 'ap'}
    ]
}
result = pickle.dumps(big_object)
print(result)

big_object_recovery = pickle.loads(result)
print(big_object_recovery)
