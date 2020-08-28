
def diff_ways_to_evaluate_expression(input):
    return diff_ways_map({}, input)

def diff_ways_map(map,input):
    if input in map:
        return map[input]

    result = []
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))

    else:
        for elem in range(len(input)):
            char = input[elem]

            if not char.isdigit():
                leftside = diff_ways_map(map, input[0:elem])      
                rightside = diff_ways_map(map, input[elem + 1:])

                for part1 in leftside:
                    for part2 in rightside:
                        if char == "+":
                            result.append(part1 + part2)

                        elif char == "-":
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