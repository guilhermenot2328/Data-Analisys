# Projeto: Qual soma entre dados da array, dá o número target?

arr = [2, 7, 11, 15]
target = 26

for n in arr:
    for n1 in arr:
        if n1 == n:
            break
        else:
            if n + n1 == target:
                n + n1 == target
                print(f"{n} + {n1} == {target}")
