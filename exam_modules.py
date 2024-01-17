def vidssum(sum, vids, month):
    if sum < 0:
        raise ValueError
    return (sum * vids * (month + 1))/(24*100)