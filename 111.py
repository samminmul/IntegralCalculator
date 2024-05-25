import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize_scalar
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

    def create_function_from_input(input_string):
        # 사용자로부터 입력된 문자열을 파이썬 코드로 변환
        parsed_code = ast.parse(input_string, mode='eval')
        
        # 안전한 표현식인지 확인
        if not isinstance(parsed_code, ast.Expression):
            raise ValueError("입력된 코드가 표현식이 아닙니다.")
        
        # 컴파일된 코드를 함수로 변환
        function = compile(parsed_code, '<string>', 'eval')
        
        # 함수 객체 반환
        return lambda x: eval(function)

    # 적분할 함수와 구간 입력
    function_to_integrate = create_function_from_input(entry1.get())
    print(type(function_to_integrate))
    interval_start = float(entry2.get())
    interval_end = float(entry3.get())

    def find_max_in_interval(func, start, end):
        # 최댓값을 찾을 함수를 정의합니다.
        def neg_func(x):
            return -func(x)
        
        # minimize_scalar 함수를 사용하여 최댓값을 찾습니다.
        result = minimize_scalar(neg_func, bounds=(start, end), method='bounded')
        
        return -result.fun, result.x

    def find_min_in_interval(func, start, end):
        # 최솟값을 찾을 함수를 정의합니다.
        def neg_func(x):
            return func(x)
        
        # minimize_scalar 함수를 사용하여 최솟값을 찾습니다.
        result = minimize_scalar(neg_func, bounds=(start, end), method='bounded')
        
        return result.fun, result.x

    d = 0.1
    
    # 최댓값 찾기
    max_value, max_point = find_max_in_interval(function_to_integrate, interval_start, interval_end)
    print("구간 내에서의 최댓값:", max_value)
    print("최댓값이 위치한 지점:", max_point)
    max_value += d
    min_value, min_point = find_min_in_interval(function_to_integrate, interval_start, interval_end)
    print("구간 내에서의 최솟값:", min_value)
    print("최솟값이 위치한 지점:", min_point)
    min_value -= d


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
