import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1067114867 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    z_alpha = np.sqrt(12) / 2 * (np.max(x) - 0.092)
    return loc - z_alpha * scale, loc + z_alpha * scale
