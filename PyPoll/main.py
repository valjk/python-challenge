# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
election_data_csv = os.path.join('/Users/valkeeranan/Desktop/python-challenge/PyPoll/Resources/election_data.csv')  # Input file path
election_analysis_txt = os.path.join('/Users/valkeeranan/Desktop/python-challenge/PyPoll/analysis/election_analysis.txt')  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {} 

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(election_data_csv) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Open a text file to save the output
with open(election_analysis_txt, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Election Results\n")
    print(f"Total Votes: {total_votes}")
    print(" ")

    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates.items():

        # Get the vote count and calculate the percentage
        percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    # Update the winning candidate if this one has more votes
    winning_candidate = max(candidates, key=candidates.get)
    winning_count = candidates[winning_candidate]

  # Generate and print the winning candidate summary
    print(" ")
    print(f"Winner: {winning_candidate}")
    print(" ")
    
# Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-------------------------\n")