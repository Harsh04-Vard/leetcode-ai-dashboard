# ---------------- QUESTION RECOMMENDER ---------------- #

def recommend_questions(data):

    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)

    recommendations = []

    # ---------------- BEGINNER LEVEL ---------------- #

    if medium < 100:

        recommendations = [
            "Two Sum",
            "Best Time to Buy and Sell Stock",
            "Contains Duplicate",
            "Maximum Subarray",
            "Valid Anagram",
            "Product of Array Except Self",
            "3Sum",
            "Container With Most Water"
        ]

    # ---------------- INTERMEDIATE LEVEL ---------------- #

    elif hard < 50:

        recommendations = [
            "Number of Islands",
            "Clone Graph",
            "Course Schedule",
            "Pacific Atlantic Water Flow",
            "Word Ladder",
            "Longest Increasing Subsequence",
            "Coin Change",
            "Network Delay Time"
        ]

    # ---------------- ADVANCED LEVEL ---------------- #

    else:

        recommendations = [
            "Median of Two Sorted Arrays",
            "Trapping Rain Water",
            "LFU Cache",
            "Serialize and Deserialize Binary Tree",
            "Sliding Window Maximum",
            "Merge k Sorted Lists",
            "N-Queens",
            "Edit Distance"
        ]

    return recommendations