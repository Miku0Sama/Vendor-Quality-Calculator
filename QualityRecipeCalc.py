from itertools import combinations
from collections import Counter
import random

# Generator for creating random inputs for debug and testing
'''
def generate_set():
    # Generate a random length between 6 and 20
    set_length = random.randint(6, 20)

    # Generate a list of random numbers between 1 and 20
    random_set = [random.randint(1, 20) for _ in range(set_length)]
    return random_set
'''

def find_combinations(qualities=[1, 20], max_waste=2, flasks_or_gems=False):
    qualities.sort(reverse=True)
    target_sum = 40
    used_numbers = Counter()
    combinations_list = []
    
    # Step 1: Find any numbers equal to or greater than 20 only if vendoring flasks or gems
    if flasks_or_gems:
        for quality in qualities:
            if quality >= 20:
                combinations_list.append([quality])
                used_numbers[quality] += 1

    # Helper function to check if a combination can be used (takes duplicates into account)
    def is_usable(combo):
        combo_count = Counter(combo)
        for quality, count in combo_count.items():
            if used_numbers[quality] + count > numbers.count(quality):  # Ensure it doesn't exceed the original count
                return False
        return True

    # Mark combo as used
    def mark_as_used(combo):
        combo_count = Counter(combo)
        for quality, count in combo_count.items():
            used_numbers[quality] += count

    # Step 2: Find all combinations that sum exactly to 40
    for r in range(2, len(qualities) + 1):
        for combo in combinations(qualities, r):
            combo_sum = sum(combo)
            if combo_sum == target_sum and is_usable(combo):
                combinations_list.append(list(combo))
                mark_as_used(combo)

    # Step 3: Find combinations that exceed 40 by no more than max_waste
    for r in range(2, len(qualities) + 1):
        for combo in combinations(qualities, r):
            combo_sum = sum(combo)
            if target_sum < combo_sum <= target_sum + max_waste and is_usable(combo):
                combinations_list.append(list(combo))
                mark_as_used(combo)

    # Get unused numbers (handling duplicates correctly)
    unused_numbers = [quality for quality in qualities if used_numbers[quality] < qualities.count(quality)]

    return combinations_list, unused_numbers

# User Input
# numbers = generate_set() Ignore this line, it is for testing and debug purposes
# Input the quality of each item separated by a comma
###############################
###### DO NOT PUT THE % #######
###############################
# Only put the actual number itself
# Make sure you type inside the square brackets!
qualities = []

# Set this to be the maximum amount of wasted Quality % you want to have in each combination
max_waste = 2

# Set this to true if you are checking flasks or gems We do this because a single 20% quality gem or flask gives a prism or bauble respectively. Alternatively, you can exclude any 20's from the input numbers.
flasks_or_gems = False

output_combinations, unused_numbers = find_combinations(qualities, max_waste, flasks_or_gems)
print("Input:", qualities)
print("Combinations:", output_combinations)
print("Unused Numbers:", unused_numbers)
