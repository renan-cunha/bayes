import pandas as pd
import numpy as np
import math
from typing import Dict


def calculate_probability(x: float, mean: float, stdev: float) -> float:
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent


def summary_csv_label(df: pd.DataFrame, class_col: str,
                      label: any) -> pd.Series:
    df_label = select_by_label(df, label, class_col)
    df_label_mean = df_label.mean()
    df_label_mean = df_label_mean.add_suffix("_mean")
    df_label_std = df_label.std()
    df_label_std = df_label_std.add_suffix("_std")
    return df_label_mean.append(df_label_std)


def summary_csv(df: pd.DataFrame, class_col: str) -> pd.DataFrame:
    """Returns a csv in wich each row corresponds to data of class,
    the columns represents the mean and std of the attributes"""
    labels = set(df[class_col])
    for label in labels:
        df_label = select_by_label(df, label, class_col)
        df_label.mean



def select_by_label(df: pd.DataFrame, label: any,
                    column: str) -> pd.DataFrame:
    index = df[column] == label
    return df[index]


