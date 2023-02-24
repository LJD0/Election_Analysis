# Election Analysis

        Using Python to analyze the results of an election using a csv file.

## Project Overview

        Within this study we were tasked with auditing of an election to find the winner. This required gathering a list of the candidates, a total count of votes for the election and for each candidate, determining the percentage of the total vote each candidate received, and verifying the winner of the election.

### Resources Used

    Software:
        VS Code 1.71.2
        Python 3.10.4
    
    Data:
        election_results.csv
        
    Output:    
        election_analysis.txt

## Summary

    This election had a total of 369,711 votes cast between three candidates, Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane, and was conducted in three counties, Denver, Arapaho, and Jefferson.

   * Devner county had the highest turnout with 82.8% of the vote or 306,055 total votes.
   * Jefferson county had the second highest with 10.5% of the vote or 38,855 total votes.
   * Arapahoe county had the lowest turnout with 6.7% of the vote or 24,801 total votes. 


   * Doane received 3.1% of the total vote, with 11,606 votes cast with their name. 
   * Stockham received 23.0% of the total vote, with 85,213 votes cast with their name.
   * Degette received 73.8% of the total vote with 272,892 votes cast with their name.

    By an overwhelming majority Diana Degette was the winner of this election with a total vote count of 272,892, 73.8% of the total votes cast.



    This audit code can be used to check other counties and candidates votes if more of that data was abailable for audit. The parameters of the dta we received only had three total counties. This script would run the same if we were to expand the dataset to include more counties. This same concept applies to the candidates as well. If there were to be more candidates they could easily be added to our data for auditing.
