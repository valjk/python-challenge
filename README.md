I leveraged Xpert Learning Assistance to add "-------------------------" to my election analysis text file in the PyPoll solution output:
 # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
# Save the winning candidate summary to the text file
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-------------------------\n")
