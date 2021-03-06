def outliers_IQR(data, col):
    lower_quartile = data[col].quantile(0.25)
    upper_quartile = data[col].quantile(0.75)
    IQR = upper_quartile - lower_quartile
    outlier_thresh = 1.5 * IQR
    return data[
        data[col].between(
            (lower_quartile - outlier_thresh), (upper_quartile + outlier_thresh)
        )
    ]

def numcol2numdtype(data, cols):
    for col in cols:
        data[col].str.replace("[^0-9]", "").astype("float")
    return data
