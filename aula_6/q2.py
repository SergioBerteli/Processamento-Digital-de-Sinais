import matplotlib.pyplot as plt
from tabulate import tabulate
prev_ns = 2
n_max = 9

impulso = [1 if i==prev_ns else 0 for i in range(n_max+prev_ns)]

degrau = [1 if i>=prev_ns else 0 for i in range(n_max+prev_ns)]

exp = [(1/2)**i if i>=prev_ns else 0 for i in range(n_max+prev_ns)]


def primeira_fn_discreta(y, x, n):
    res = 0.2 * x[n]+ 0.3 * x[n-1]+ 0.3 * x[n-2] + 0.2 * x[n-3] 
    y.append(res)

y = [0 for i in range(prev_ns)]

x = degrau

for i in range(n_max):
    primeira_fn_discreta(y, x, i+prev_ns)

headers = ["n", "y(n)", "x(n)"]

n = [i for i in range(-prev_ns, n_max)]

table = zip(n, y, x)

print(tabulate(table, headers))
plt.scatter(n, y, color='blue', label='y(n)', linewidth=8)
plt.scatter(n, x, color='red', label='x(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Plotagem da função y(n)')
plt.legend()
plt.grid(True)
plt.show()

