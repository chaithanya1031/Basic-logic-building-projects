candidates = {'C1': 'rakesh', 'C2': 'chanti'}
votes = {}
for name in candidates.values():
    votes[name] = 0
print("Voting has started! Type 'stop' to end voting.\n")
while True:
    vote = input("Enter the candidate you would like to vote for (rakesh/chanti): ").lower()
    if vote == 'stop':
        print("\nVoting ended.")
        break
    if vote in votes:
        votes[vote] += 1
        print(f"Vote recorded for {vote.capitalize()}.")
    else:
        print("Invalid candidate name. Please vote for either rakesh or chanti.")
print("\nFinal Vote Count:", votes)
# winner
max_votes = max(votes.values())
winners = []
for name, count in votes.items():
    if count == max_votes:
        winners.append(name)
if len(winners) > 1:
    print(f"\nIt's a tie between: {', '.join(winners)}")
else:
    print(f"\n🏆 The winner is: {winners[0].capitalize()} with {max_votes} votes!")
