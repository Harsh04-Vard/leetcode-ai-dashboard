# ---------------- ROADMAP GENERATOR ---------------- #

def generate_local_roadmap(data):

    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)

    roadmap = []

    # ---------------- BEGINNER ---------------- #

    if medium < 100:

        roadmap = [
            "Day 1 → Arrays Revision",
            "Day 2 → Hashing Problems",
            "Day 3 → Sliding Window",
            "Day 4 → Binary Search",
            "Day 5 → Linked Lists",
            "Day 6 → Stack & Queue",
            "Day 7 → Trees Basics",
            "Day 8 → BST Problems",
            "Day 9 → Heap / Priority Queue",
            "Day 10 → Recursion & Backtracking",
            "Day 11 → Greedy Algorithms",
            "Day 12 → Graph Basics",
            "Day 13 → BFS & DFS",
            "Day 14 → Mixed Revision + Mock Contest"
        ]

    # ---------------- INTERMEDIATE ---------------- #

    elif hard < 50:

        roadmap = [
            "Day 1 → Advanced Trees",
            "Day 2 → Graph Traversals",
            "Day 3 → Topological Sort",
            "Day 4 → Shortest Path Algorithms",
            "Day 5 → Dynamic Programming Basics",
            "Day 6 → 1D DP Problems",
            "Day 7 → 2D DP Problems",
            "Day 8 → Greedy + Intervals",
            "Day 9 → Backtracking",
            "Day 10 → Tries",
            "Day 11 → Segment Trees",
            "Day 12 → Advanced Graphs",
            "Day 13 → Hard LeetCode Problems",
            "Day 14 → Full Mock Interview"
        ]

    # ---------------- ADVANCED ---------------- #

    else:

        roadmap = [
            "Day 1 → Hard DP",
            "Day 2 → Graph Hard Problems",
            "Day 3 → Advanced Trees",
            "Day 4 → Segment Trees",
            "Day 5 → Fenwick Trees",
            "Day 6 → Bit Manipulation",
            "Day 7 → Trie Problems",
            "Day 8 → Union Find",
            "Day 9 → Hard Sliding Window",
            "Day 10 → Monotonic Stack",
            "Day 11 → Competitive Programming",
            "Day 12 → Timed Contest",
            "Day 13 → Interview Simulation",
            "Day 14 → Final Revision"
        ]

    return roadmap