import numpy as np                                  # pip install numpy
import matplotlib.pyplot as plt                     # pip install mathpotlib
import random
import sympy as sp                                  # pip install sympy
import math as math
from tkinter import *
import ast

tk = Tk()
tk.title("적분값 계산기")
tk.geometry("500x200")
s = ''

label1 = Label(tk, text='함수: ', font=10).grid(row=0,column=0)
label2 = Label(tk, text='구간 시작: ', font=10).grid(row=1,column=0)
label3 = Label(tk, text='구간 끝: ', font=10).grid(row=2,column=0)
label4 = Label(tk, text='샘플수: ', font=10).grid(row=3,column=0)
label5 = Label(tk, text='적분값: ', font=10).grid(row=4,column=0)

entry1 = Entry(tk,font=10, width= 20)
entry1.grid(row=0,column=1)
entry2 = Entry(tk,font=10, width= 20)
entry2.grid(row=1,column=1)
entry3 = Entry(tk,font=10, width= 20)
entry3.grid(row=2,column=1)
entry4 = Entry(tk,font=10, width= 20)
entry4.grid(row=3,column=1)

def zukbun():
    global s, label6
    def monte_carlo_integration(func, start, end, num_samples):
        total_area = (end - start) * max_value
        points_inside = 0
        points_m_inside = 0
        
        inside_x = []
        inside_y = []
        
        outside_x = []
        outside_y = []
        
        m_inside_x = []
        m_inside_y = []
        
        for _ in range(num_samples):
            x = random.uniform(start, end)
            y = random.uniform(min_value, max_value)
            if 0 <= y <= func(x):
                points_inside += 1
                inside_x.append(x)
                inside_y.append(y)
                        
            elif 0 > y >= func(x):
                points_m_inside += 1
                m_inside_x.append(x)
                m_inside_y.append(y)
                
            else:
                outside_x.append(x)
                outside_y.append(y)
                

                
        probability = points_inside / num_samples - points_m_inside / num_samples
        integral_value = total_area * probability
        return integral_value, inside_x, inside_y, outside_x, outside_y, m_inside_x, m_inside_y


    # 입력값 가져오기
    x = sp.Symbol('x')
    f_sympy = entry1.get()  # entry1은 tkinter 또는 다른 GUI 프레임워크에서 입력된 함수 식입니다.

    # sympy로 함수와 도함수 생성
    f = sp.sympify(f_sympy)
    f_func = sp.lambdify(x, f, 'numpy')
    df = sp.diff(f, x)
    df_func = sp.lambdify(x, df, 'numpy')

    # 적분할 함수와 구간 입력
    function_to_integrate = f_func
    print(type(function_to_integrate))
    interval_start = float(entry2.get())  # entry2는 시작 구간의 입력값입니다.
    interval_end = float(entry3.get())  # entry3은 끝 구간의 입력값입니다.

    
    def find_min_and_max(f, df, x0, lower_bound, upper_bound, minimize=True, maximize=True, learning_rate=0.01, momentum=0.9, tolerance=1e-6, max_iterations=1000):
        # 초기값 설정
        x_min = x0
        x_max = x0
        velocity_min = np.zeros_like(x_min)
        velocity_max = np.zeros_like(x_max)
        iteration = 0
        
        while iteration < max_iterations:
            if minimize:
                # 경사하강법: 최솟값 찾기
                grad_min = df(x_min)
                if np.linalg.norm(grad_min) < tolerance:
                    break
                velocity_min = momentum * velocity_min - learning_rate * grad_min
                x_min = x_min + velocity_min
                x_min = np.clip(x_min, lower_bound, upper_bound)  # 구간 내에 x_min을 제한
            
            if maximize:
                # 경사상승법: 최댓값 찾기
                grad_max = df(x_max)
                if np.linalg.norm(grad_max) < tolerance:
                    break
                velocity_max = momentum * velocity_max + learning_rate * grad_max
                x_max = x_max + velocity_max
                x_max = np.clip(x_max, lower_bound, upper_bound)  # 구간 내에 x_max를 제한
            
            iteration += 1
        
        return x_min, f(x_min), x_max, f(x_max)

    d = 0.1
     
    min_point, min_value, max_point, max_value = find_min_and_max(f_func, df_func, interval_start, interval_start, interval_end)
    print("구간 내에서의 최솟값:", min_value)
    print("최솟값이 위치한 지점:", min_point)
    print("구간 내에서의 최댓값:", max_value)
    print("최댓값이 위치한 지점:", max_point)
    min_value -= d
    max_value += d


    # 샘플 개수 설정
    num_samples = int(entry4.get())

    # 몬테카를로 적분을 사용하여 적분 값 추정
    integral_estimate, inside_x, inside_y, outside_x, outside_y, m_inside_x, m_inside_y = monte_carlo_integration(function_to_integrate, interval_start, interval_end, num_samples)
    print("몬테카를로 적분을 사용하여 추정한 적분 값:", integral_estimate)
    s = round(float(integral_estimate), 4)
    label6 = Label(tk, text=s, font=10).grid(row=4,column=1) 

    # 함수 그래프 그리기
    x = np.linspace(interval_start, interval_end, 100)
    y = function_to_integrate(x)
    plt.plot(x, y, label='Function')

    # 사각형의 외각선 그리기
    plt.plot([interval_start, interval_end, interval_end, interval_start, interval_start], 
            [min_value, min_value, max_value, max_value, min_value], 
            color='black', linestyle='--', label='Rectangle')

    # 랜덤한 점의 분포 그리기
    plt.scatter(inside_x, inside_y, color='blue', label='Inside Points')
    plt.scatter(outside_x, outside_y, color='red', label='Outside Points')
    plt.scatter(m_inside_x, m_inside_y, color='green', label='Minus Inside Points')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Monte Carlo Integration')
    plt.legend()
    plt.grid(True)
    plt.show()

btn = Button(tk, text='적분', bg='gray', fg='white', font=10, command=zukbun).grid(row=5,column=0)
tk.mainloop()