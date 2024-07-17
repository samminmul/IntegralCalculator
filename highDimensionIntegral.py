import math
import numpy as np
import matplotlib.pyplot as plt


def integral_2():
    def semicircle(x):
        y = math.sqrt(max(1 - x**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if semicircle(X[i]) > Y[i]:
            inner += 1
    area = 2**1 * inner / N

    return area


def integral_3():
    def hemisphere(x, z):
        y = math.sqrt(max(1 - x**2 - z**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere(X[i], Z[i]) > Y[i]:
            inner += 1
    area = 2**2 * inner / N

    return area


def integral_4():
    def hemisphere4(x, z, w):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere4(X[i], Z[i], W[i]) > Y[i]:
            inner += 1
    area = 2**3 * inner / N

    return area


def integral_5():
    def hemisphere5(x, z, w, v):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2 - v**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    V = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere5(X[i], Z[i], W[i], V[i]) > Y[i]:
            inner += 1
    area = 2**4 * inner / N

    return area


def integral_6():
    def hemisphere6(x, z, w, v, u):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2 - v**2 - u**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    V = np.random.random(2*N - 1)
    U = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere6(X[i], Z[i], W[i], V[i], U[i]) > Y[i]:
            inner += 1
    area = 2**5 * inner / N

    return area


def integral_7():
    def hemisphere7(x, z, w, v, u, t):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2 - v**2 - u**2 - t**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    V = np.random.random(2*N - 1)
    U = np.random.random(2*N - 1)
    T = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere7(X[i], Z[i], W[i], V[i], U[i], T[i]) > Y[i]:
            inner += 1
    area = 2**6 * inner / N

    return area


def integral_8():
    def hemisphere8(x, z, w, v, u, t, s):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2 - v**2 - u**2 - t**2 - s**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    V = np.random.random(2*N - 1)
    U = np.random.random(2*N - 1)
    T = np.random.random(2*N - 1)
    S = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere8(X[i], Z[i], W[i], V[i], U[i], T[i], S[i]) > Y[i]:
            inner += 1
    area = 2**7 * inner / N

    return area


def integral_9():
    def hemisphere9(x, z, w, v, u, t, s, r):
        y = math.sqrt(max(1 - x**2 - z**2 - w**2 - v**2 - u**2 - t**2 - s**2 - r**2, 0))
        return y
    
    N = int(1e4)
    X = np.random.random(2*N - 1)
    Z = np.random.random(2*N - 1)
    W = np.random.random(2*N - 1)
    V = np.random.random(2*N - 1)
    U = np.random.random(2*N - 1)
    T = np.random.random(2*N - 1)
    S = np.random.random(2*N - 1)
    R = np.random.random(2*N - 1)
    Y = np.random.random(N)
    
    inner = 0
    for i in range(N):
        if hemisphere9(X[i], Z[i], W[i], V[i], U[i], T[i], S[i], R[i]) > Y[i]:
            inner += 1
    area = 2**8 * inner / N

    return area



REPEATS = 100
i2arr = [integral_2() for _ in range(REPEATS)]
i3arr = [integral_3() for _ in range(REPEATS)]
i4arr = [integral_4() for _ in range(REPEATS)]
i5arr = [integral_5() for _ in range(REPEATS)]
i6arr = [integral_6() for _ in range(REPEATS)]
i7arr = [integral_7() for _ in range(REPEATS)]
i8arr = [integral_8() for _ in range(REPEATS)]
i9arr = [integral_9() for _ in range(REPEATS)]

print("반지름이 1인 반원의 적분 결과:", np.mean(i2arr))
print("반지름이 1인 반구의 적분 결과:", np.mean(i3arr))
print("반지름이 1인 4차원 반구의 적분 결과:", np.mean(i4arr))
print("반지름이 1인 5차원 반구의 적분 결과:", np.mean(i5arr))
print("반지름이 1인 6차원 반구의 적분 결과:", np.mean(i6arr))
print("반지름이 1인 7차원 반구의 적분 결과:", np.mean(i7arr))
print("반지름이 1인 8차원 반구의 적분 결과:", np.mean(i8arr))
print("반지름이 1인 9차원 반구의 적분 결과:", np.mean(i9arr))

x = [i for i in range(2, 10)]
y = list(map(np.mean, [i2arr, i3arr, i4arr, i5arr, i6arr, i7arr, i8arr, i9arr]))

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, y)
plt.title('몬테 카를로 적분을 이용해 구한 n차원 반구의 부피')
plt.xlabel('차원')
plt.ylabel('n차원 반구의 부피')
plt.show()