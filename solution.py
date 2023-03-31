import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1067114867 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    max_x = np.max(x)
    t = (max_x - 0.092) / alpha
    t_alpha_2 = abs(t.ppf(alpha / 2, n-1))
    return max_x - t_alpha_2 * (1 - p), max_x + t_alpha_2 * (1 - p)
