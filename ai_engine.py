# ---------------- WEAK TOPIC ANALYZER ---------------- #

def analyze_user(data):

    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)

    insights = []

    # ---------------- HARD PROBLEMS ---------------- #

    if hard < 50:

        insights.append({
            "type": "warning",
            "message": """
Focus more on Hard problems.

Recommended Topics:
• Graphs
• Dynamic Programming
• Trees
"""
        })

    # ---------------- MEDIUM PROBLEMS ---------------- #

    elif medium < 150:

        insights.append({
            "type": "info",
            "message": """
You should solve more Medium problems.

Recommended Topics:
• Sliding Window
• Binary Search
• Greedy
"""
        })

    else:

        insights.append({
            "type": "success",
            "message": """
Excellent consistency and balanced problem solving.
"""
        })

    return insights


# ---------------- INTERVIEW READINESS SCORE ---------------- #

def calculate_readiness(data):

    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)

    score = (
        easy * 1 +
        medium * 2 +
        hard * 3
    ) / 10

    if score > 100:
        score = 100

    return int(score)


# ---------------- QUESTION RECOMMENDER ---------------- #

def recommend_questions(data):

    hard = data.get("hardSolved", 0)

    if hard < 50:

        return [
            "Number of Islands",
            "Clone Graph",
            "Course Schedule",
            "Word Ladder",
            "Longest Increasing Subsequence"
        ]

    return [
        "Median of Two Sorted Arrays",
        "Trapping Rain Water",
        "LFU Cache"
    ]