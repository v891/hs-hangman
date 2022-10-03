def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return "I " + instructions[11:len(instructions)]
    elif instructions.endswith("Simon says"):
        return "I " + instructions[0: instructions.rindex(" Simon says")]
    else:
        return "I won't do it!"

# print(what_to_do("Simon says make a wish"))