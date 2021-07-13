import random
choices=['r','p','s']
names={'r':'rock','p':'paper','s':'scissors'}
output={'r':{},'p':{},'s':{}}
for i in range(3):
    output[choices[i]][choices[(i+1)%3]]='You win!'
    output[choices[i]][choices[i]]='Tie!'
    output[choices[i]][choices[(i-1)%3]]='The computer won!'

while True:
    human=input("What you want to play? (r/s/p)")
    computer=random.choice(choices)
    print(f"You played {names[human]}")
    print(f"Computer played {names[computer]}")
    print(output[human][computer])
