def reversebits (input)
    input = 1234
    binary = "{:032b}".format(input)
    binary = binary[::-1]
    output = int(binary,2)
    return output
