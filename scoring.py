import sys
from LDCalc import distanceCalc

MAX_POWER = 6.28232727

def parsePowerFile(powerFile):
    with open(powerFile, "r") as f:
        lines = f.readlines()

    if lines:
        powerline = lines[-2]
        powerdata = powerline.split(",")
        power = float(powerdata[7])
        return power
    return -1

def calc_final_score(groundTruthFile, submissionFile, powerFile, videoLength):
    if powerFile == None:
        return 0
    videoLengthHours = videoLength / 3600.0
    ldError = distanceCalc(groundTruthFile, submissionFile)
    ldAccuracy = 1 - ldError
    power = parsePowerFile(powerFile)
    final_score_a = ldAccuracy * (1 - (power / (3 * MAX_POWER * videoLengthHours))) if power != -1 else 0
    final_score_b = ldAccuracy / (1 + power)
    return (ldAccuracy, power, final_score_a, final_score_b)



if __name__ == '__main__':
     if len(sys.argv) == 5:
         final_tuple = calc_final_score(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
         print(final_tuple)
     else:
         print("Incorrect number of arguments. Found {:d}, expected 5".format(len(sys.argv)))
		 print("Usage: python3 scoring.py [ground truth file] [submission file] [power csv file] [video length in seconds]