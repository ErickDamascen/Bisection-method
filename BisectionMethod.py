import numpy as np
tol = 0.0001
equa = ''

menorpositivo = np.inf
cont = 0

def func(x):
    return eval(equa)

def bisec(f, a, b, tol):
    global menorpositivo, cont 
    cont += 1

    xm = (a + b)/2
    
    if xm > 0 and xm < menorpositivo:
        menorpositivo = xm

    if abs(a-xm)<tol:
        if menorpositivo == np.inf:
            menorpositivo = 'Não existe menor raiz positiva'
        return 'Raiz: {}, Menor raiz positiva: {}'.format(round(xm, 4),menorpositivo)
    
    if f(a)*f(xm)<0:
        return bisec(f,a,xm,tol)
    return bisec(f,xm,b,tol)

if __name__ == '__main__':
    equa = input('Insira Função, exemplo: x**2-4:\n')
    print('Função: {}\nTolerancia de 0.0001 definida.\n'.format(equa))
    a = float(input('intervalo inicial [a]: '))
    b = float(input('intervalo final [b]: '))
    print('\n')
    print(bisec(func,a,b,tol))
    print('Iterações realizadas: {}'.format(cont))