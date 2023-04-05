import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1067114867 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alph1 = (1 - p) / 2
    alph2 = (1 + p) / 2
    n = x.size
    a1 = pow(alph1, 1 / n)
    a2 = pow(alph2, 1 / n)
    x_max = x.max()
    return (x_max - 0.092) / a2 + 0.092, (x_max - 0.092) / a1 + 0.092
