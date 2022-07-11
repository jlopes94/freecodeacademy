

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]  # switch to problems later
solve = True  # remove later


def arithmetic_arranger(problems, solve=False):
    top = ''
    bot = ''
    dashes = ''
    res = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        problem = problem.split(' ')
        l1 = problem[0]
        l2 = problem[2]
        opr = problem[1]

        if problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Error: Numbers must only contain digits."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
           return print("Error: Numbers cannot be more than four digits.")

        width = max(len(l1), len(l2)) + 2
        top += l1.rjust(width) + '    '
        bot += opr + ' ' * (width - len(l2) - 1) + l2 + '    '
        dashes += '-' * width + '    '

        if opr == '-':
            res += str(int(l1) - int(l2)).rjust(width) + '    '
        if opr == '+':
            res += str(int(l1) + int(l2)).rjust(width) + '    '


    top = top.rstrip()
    bot = bot.rstrip()
    dashes = dashes.rstrip()
    res = res.rstrip()
    results = top + '\n' + bot + '\n' + dashes
    if solve:
        results += '\n' + res
    return results


print(arithmetic_arranger(problems))

