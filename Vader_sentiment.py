from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import glob
import pandas as pd

# Reading the excel file
data=pd.read_excel("/Users/Downloads/ML_Sources/Feedbacks.xlsx")

# Storing only the "feedback" section from the file
actual_data=data["feeback"]

# Converting the data into tuples
data=tuple(actual_data)

# Creating an object of SentimentAnalyzer
sid = SentimentIntensityAnalyzer()

# Looping through the data
for sentence in data1:
    
        # Calculating the Polarity score.
        ss = sid.polarity_scores(sentence)
        print(sentence)
        for k in sorted(ss):
             print('{0}: {1}, '.format(k, ss[k]), end='')
        if(ss.get("compound")<0):
            print(" The feedback is Negative")
        elif(ss.get("compound")>=0 and ss.get("compound")<=0.45 ):
            print(" The feedback is Neutral")
        elif(ss.get("compound")>0.45):
            print("The feedback is positive")
