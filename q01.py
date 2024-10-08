def fibonacci(num):
    fib = [0, 1]
    
    # Gera a sequência de Fibonacci até o número informado
    while True:
        next_fib = fib[-1] + fib[-2]  # Calcula o próximo número da sequência
        if next_fib > num:  # Para quando o próximo número ultrapassar o informado
            break
        fib.append(next_fib)
    
    if num in fib:
        print(f'O número {num} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {num} não pertence à sequência de Fibonacci.')


num = int(input('Entre com um número: '))
fibonacci(num)
