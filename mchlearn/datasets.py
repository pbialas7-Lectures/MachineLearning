import pandas as pd

inch = 0.01 * 2.54  # m
pound = 0.453  # kg


def load_height_weight(f):
    data = pd.read_csv(f)
    data['Height'] = data['Height'] * inch
    data['Weight'] = data['Weight'] * pound

    data['BMI'] = data['Weight'] / data['Height'] ** 2

    return data
