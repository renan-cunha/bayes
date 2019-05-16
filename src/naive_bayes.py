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
        df_label_summary = summary_csv_label(df, class_col, label)
        df_label_summary = df_label_summary.rename(label)
        if "result_csv" in locals():
            result_csv = result_csv.append(df_label_summary)
        else:
            result_csv = pd.DataFrame([df_label_summary])
    return result_csv


def select_by_label(df: pd.DataFrame, label: any,
                    column: str, drop_column: bool = True) -> pd.DataFrame:
    index = df[column] == label
    result = df[index]
    if drop_column:
        result = result.drop(columns=[column])
    return result


def calculate_class_prob(df: pd.DataFrame, sample: pd.Series,
                         class_col: str) -> Dict:
    probabilities = {}

    df_summary = summary_csv(df, class_col)

    df = df.drop(columns=[class_col])
    for index in df_summary.index:
        index_prob = 1.0
        for col in df.columns:
            index_prob *= calculate_probability(sample[col],
                                                df_summary.loc[index,
                                                               f"{col}_mean"],
                                                df_summary.loc[index,
                                                               f"{col}_std"])
        probabilities[index] = index_prob

    return probabilities
