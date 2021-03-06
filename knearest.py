from typing import List, NamedTuple
from collections import Counter
from resources.linear_algebra import Vector, distance

# Let's pick a number k like 3 and then classify some new data point, we will look for the k nearest labeled points and let them vote
# however this won't be able to deal with ties...
def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

assert raw_majority_vote(['a','b','c','b']) == 'b'

#  So we will reduce k until it finds only one winner

def majority_vote(labels: List[str]) -> str:
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winner = len([count for count in vote_counts.values() if count == winner_count])
    if num_winner == 1:
        return winner
    else:
        return majority_vote(labels[:-1])

assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'


class LabeledPoint(NamedTuple):
    point: Vector
    label: str

def knn_classify(k: int, labeled_points: List[LabeledPoint], new_point: Vector) -> str:
    by_distance = sorted(labeled_points, key=lambda lp: distance(lp.point, new_point))
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)
