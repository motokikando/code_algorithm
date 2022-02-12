from typing import List
l = list(map(int, input().split()))
# l = [4,1,3]
def judge_sequence(seq: List[int]) -> str:
    seq = sorted(seq)
    if seq[2] - seq[1] == seq[1] - seq[0]:
        return "Yes"
    else:
        return "No"

print(judge_sequence(l))

