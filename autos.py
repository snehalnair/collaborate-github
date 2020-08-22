def numcol2numdtype(data, cols):
    for col in cols:
        data[col].str.replace("[^0-9]", "").astype("float")
    return data
