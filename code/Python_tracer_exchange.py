# Python code for simulating tracer exchange

m1 = 100
x1 = 0.95
m2 = 300.47
x2 = 0.069825
n = 0.1088
times = 1800

with open('tracer_exchange_simulation.txt', 'w') as f:
    f.write('Time 6Li_abundance_in_electrode 6Li_abundance_in_electrolyte\n')

    for i in range(times + 1):
        x2 = (m2 * x2 + n * x1) / (m2 + n)
        x1 = (n * x2 + (m1 - n) * x1) / m1
        f.write(f'{i} {x1:.4f} {x2:.4f}\n')
        
        print(f'{i} {x1:.4f} {x2:.4f}')