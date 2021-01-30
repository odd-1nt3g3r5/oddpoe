import pyperclip
GreedyCounts = {}
Greedies = ['performs','executes','swings','delivers']
with open('Scratch') as f:
    for line in f:
        Tokens = line.split()
        # If the chat line is a greedy, check to see if the pirate is already in the 
        # GreedyCounts dictionary. If they are, increment their greedy count by 1.
        # If they are not, set their greedy count to 1
        if Tokens[1] in Greedies :
            if Tokens[0] in GreedyCounts:
                GreedyCounts[Tokens[0]] = GreedyCounts[Tokens[0]] +1
            else :
                GreedyCounts[Tokens[0]] = 1
        # If the pirate was slain, remove their greedies
        elif len(Tokens) >= 3 and Tokens[2] == "eliminated!" :
            if Tokens[0] in GreedyCounts :
                del GreedyCounts[Tokens[0]]
# Copy result to windows clipboard and print to terminal
pyperclip.copy(str(GreedyCounts))
print(GreedyCounts)