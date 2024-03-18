def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        problems = "Error: Too many problems."
        return problems

    string1 = ""
    string2 = ""
    string3 = ""
    string4 = ""

    for index,item in enumerate(problems):
        problem = item.split()
        
        if problem[1] not in ["+", "-"]:
            problems = "Error: Operator must be '+' or '-'."
            return problems

        if problem[0].isdigit() == False or problem[2].isdigit() == False:
            problems = 'Error: Numbers must only contain digits.'
            return problems

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            problems = 'Error: Numbers cannot be more than four digits.'
            return problems

        length = len(problem[0]) + 2 if len(problem[0]) > len(problem[2]) else len(problem[2]) + 2
        if index == len(problems) -1:
            string1 += (" " * (length - len(problem[0])) + problem[0])
            string2 += problem[1] + (" " * (length - 1 - len(problem[2])) + problem[2])
            string3 += length * "-"
            result = str(eval(item))
            string4 += " " * (length - len(result)) + result
        else:
            string1 += (" " * (length - len(problem[0])) + problem[0] + "    ")
            string2 += problem[1] + (" " * (length - 1 - len(problem[2])) + problem[2] + "    ")
            string3 += length * "-" + "    "
            result = str(eval(item))
            string4 += " " * (length - len(result)) + result + "    "


    if show_answers == True:
        problems = string1 + "\n" + string2 + "\n" + string3 + "\n" + string4
    else:
        problems = string1 + "\n" + string2 + "\n" + string3
    
    return problems

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
