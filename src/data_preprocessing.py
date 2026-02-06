from config import config
import pandas as pd





numerical_stats = []
def data_preprocessing(df):
    # Segregate the numerical and categorical columns
    numerical_cols = df.select_dtypes(exclude=['object']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    from collections import OrderedDict

    for i in numerical_cols:
        num_stats = OrderedDict({
            "Feature":i,
            "Maximum":df[i].max(),
            "Minimum":df[i].min(),
            "Mean":df[i].mean(),
            "Q1":df[i].quantile(0.25),
            "Q2":df[i].quantile(0.50),
            "Q3":df[i].quantile(0.75),
            "IQR":df[i].quantile(0.75) - df[i].quantile(0.25),\
            "Standard Deviation":df[i].std(),
            "Variance":df[i].var(),
            "Skewness":df[i].skew(),
            "Kurtosis":df[i].kurtosis(),
        })
        numerical_stats.append(num_stats)
        numerical_stats_report = pd.DataFrame(numerical_stats)

    return numerical_stats_report

