def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here   +
    th = 0
    tmin = 0
    tsec = 0

    if (hr2 > hr1):
        th = int(hr2-hr1)
    else:
        th = 0
    if (min2 > min1):
        tmin = int(min2 - min1)
    else:
        tmin = 0

    if (sec2 > sec1):
        tsec = int (sec2 - sec1)
    else:
        tsec = 0

    return (th * 3600 + tmin * 60 + tsec)


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
