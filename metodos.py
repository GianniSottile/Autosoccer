from matplotlib import pyplot as plt
#****************************************************
#METODO DE EULER
#****************************************************
def euler(N, x0, y0, f, x_f):
  xn = []
  yn = []
  h = (x_f - x0) / N
  yk = y0
  for k in range(N):
    xk = x0 + h * k
    yk = yk + f(xk, yk) * h
    xn.append(xk)
    yn.append(yk)
  return xn, yn


def f(x, y):
  return x/y

x0 = 0
y0 = 1

N = 2
x_f = 1
xn, yn = euler(N, x0, y0, f, x_f)
plt.plot(xn, yn)
print(yn)
plt.show()

