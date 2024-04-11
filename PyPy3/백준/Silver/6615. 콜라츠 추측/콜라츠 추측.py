while True:
    n, m = map(int, input().split())
    initial_n = n
    initial_m = m

    if n == 0 and m == 0:
        break

    first = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        
        first.append(n)

    second = [m]
    while m > 1:
        if m % 2 == 0:
            m //= 2
        else:
            m = 3 * m + 1
        
        second.append(m)
    
    found = False

    for i in range(len(first)):
        if found:
            break

        for j in range(len(second)):
            if first[i] == second[j]:
                found = True
                print("{} needs {} steps, {} needs {} steps, they meet at {}".format(initial_n, i, initial_m, j, first[i]))
                break