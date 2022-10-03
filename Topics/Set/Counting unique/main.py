# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

result = set(Belov)
# result.update(Belov)
result.update(Smith)
result.update(Sarada)
print(result)
# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
