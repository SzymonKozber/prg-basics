test_results = [
False, True, False, True, True,
True, True, False, True, True,
False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if test_results == "True":
        correct_answer += 1

# calculates the number of incorrect answers
incorrect_answers = 0
for answer in test_results:
    if test_results == "False":
        incorrect_answers += 1

# calculates the percentage of correct answers
test_statistics = correct_answers/test_results*100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', ...)
print('Number of correct answers:', ...)
...
...