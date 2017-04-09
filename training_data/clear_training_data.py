def has_indication(line):
    words = line.split(' ')
    sum_ind = 0
    for i in range(1, len(words) - 1):
        sum_ind += float(words[i])
    if sum_ind == 0.0:
        return False
    else:
        return True


if __name__ == "__main__":
    with open("feature_avg.txt") as inputFile:
        with open("feature_avg_filtered.txt", "w") as outputFile:
            for inputLine in inputFile:
                if has_indication(inputLine):
                    outputFile.write(inputLine)
