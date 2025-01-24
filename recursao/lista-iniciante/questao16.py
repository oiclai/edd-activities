def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
# Aqui se inicia o programa principal
for i in range(1,6):
    print(pascal(i))

# [1]
# [1, 1]
# [1, 2, 1]      
# [1, 3, 3, 1]   
# [1, 4, 6, 4, 1]