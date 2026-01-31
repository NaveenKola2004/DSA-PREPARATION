import string
from collections import Counter
paragraph="I once watched a vending machine eat someone’s dollar like it was a personal vendetta, and honestly that moment explained adulthood better than any self-help book ever could. You show up hopeful, you follow the instructions, you press the right buttons, and still—clunk—nothing comes out. So you stand there, staring through the glass at the thing you wanted, debating whether to walk away with dignity or start shaking the machine like a raccoon with unresolved issues. Life’s kind of like that: half patience, half audacity, and 100% pretending you meant to do that all along."

paragraph=paragraph.lower()
paragraph=paragraph.translate(str.maketrans("","",string.punctuation))
paragraph=paragraph.split()
counter=Counter(paragraph)
print(counter)