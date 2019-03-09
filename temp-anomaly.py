# temp-anomaly.py
# Raunak Anand
# Our program will calculate a moving average of the temperature anomaly data for Sacramento

filename = input("Temperature anomaly filename:") # asking user to input filename
if filename == "Sacramento-1880-2018.NOAA.webarchive": # if and else statement
    infile = open("Sacramento-1880-2018.NOAA.webarchive", "r") # information input from Sacramento-1880-2018.NOAA.csv
    outfile= open("tempAnomaly.txt","w") # data output to tempAnomaly.txt
    outfile.write("Year\tValue\n") # print("Year", "\t", "Value")
    for i in range(5):
        infile.readline() # statement for the program to read the whole .csv but ignore the first five lines

    from inputCheck import canBeInt
    while True:
        k = int (input("Enter an integer between 0 and 60:"))
        if canBeInt(k) and 0 <= int(k) <= 60:
            break # infinite loop that only breaks unless user inputs an integer between 0 and 60
    
    textdoc = [TA for TA in infile]  # name of each line in file 'infile' is 'TA'
    cnt = k
    for TA in textdoc[k:-k]: # starts with k and ends with the one before k
        TA = TA.split(",") # line splits at the comma
        year = TA[0]
        total = 0
        amount = (2*k)+1
        for calculate in textdoc[cnt - k:cnt + k + 1]: # range of calculation
            calculate = calculate.split(",") # split line at the comma 
            amt = float(calculate[1]) # to make into a float
            total = total + amt

        average= "{:.4f}".format(total/amount) # statement to round off moving averages to 4 decimal places
        outfile = open('tempAnomaly.txt', 'a') # adding changes to the output file
        outfile.write(TA[0] + '\t' + average + '\n')
        cnt = cnt + 1

    infile.close() # close .webarchive file 
    outfile.close() # close .txt file
else:
    print("The file",filename,"could not be opened.")
   
