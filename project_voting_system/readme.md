**🗳️ Voting System (Python)**
📘 **Description**

This Python program simulates a simple voting system between two candidates.
It allows users to cast votes, validates input, counts votes, and finally announces the winner (or declares a tie if needed).

**🧠 Example**

Candidates:

Rakesh

Chanti

Sample Run:

Voting has started! Type 'stop' to end voting.

Enter the candidate you would like to vote for (rakesh/chanti): rakesh  
Vote recorded for Rakesh.  

Enter the candidate you would like to vote for (rakesh/chanti): chanti  
Vote recorded for Chanti.  

Enter the candidate you would like to vote for (rakesh/chanti): rakesh  
Vote recorded for Rakesh.  

Enter the candidate you would like to vote for (rakesh/chanti): stop  

Voting ended.

Final Vote Count: {'rakesh': 2, 'chanti': 1}

🏆 The winner is: Rakesh with 2 votes!

**⚙️ Working Logic**

* A dictionary candidates stores candidate codes and names.
* Another dictionary votes initializes all candidates with zero votes.
* The program repeatedly asks the user to enter a candidate name to vote for.
* Each valid vote increases the respective candidate’s count.
* Typing 'stop' ends the voting process.
The program then:
* Displays total votes per candidate.
* Identifies the candidate(s) with the maximum votes.
* Declares the winner or a tie if needed.

**🚀 Features**

* Handles unlimited votes until 'stop' is entered.
* Prevents invalid candidate inputs.
* Supports tie situations gracefully.
* Displays final vote counts and results clearly.

**🧰 Use Cases**

* Demonstration of real-time voting logic.
* Learning dictionary manipulation and loops.
* Building foundational logic for polling or survey apps.