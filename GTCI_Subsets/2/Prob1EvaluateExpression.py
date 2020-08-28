def diff_ways_to_evaluate_expression(input):
    return diff_ways_rec({}, input)

def diff_ways_rec(map,input):

    if input in map:
        return map[input]

    result = []

    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    
    else:
        for index in range(len(input)):
            curr_elem = input[index]

            if not curr_elem.isdigit():
                leftSide = diff_ways_rec(map,input[0:index])
                rightSide = diff_ways_rec(map, input[index + 1: ])

                for part1 in leftSide:
                    for part2 in rightSide:
                        if curr_elem == "+":
                            result.append(part1 + part2)
                        elif curr_elem == "-":    
                            result.append(part1 - part2)
                        else:
                            result.append(part1 * part2)

    map[input] = result
    return result

def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
