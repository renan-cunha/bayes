import pandas


def select_by_label(df: pandas.DataFrame, label: any,
                    column: str) -> pandas.DataFrame:
    index = df[column] == label
    return df[index]


