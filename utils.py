import requests


# ---------------- COMMON HEADERS ---------------- #

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}


# ---------------- FETCH USER DATA ---------------- #

def fetch_user_data(username):

    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username

        profile {
          ranking
          reputation
          userAvatar
        }

        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    variables = {
        "username": username
    }

    try:

        response = requests.post(
            url,
            json={
                "query": query,
                "variables": variables
            },
            headers=headers,
            timeout=15
        )

        if response.status_code == 200:

            data = response.json()

            user = data.get("data", {}).get("matchedUser")

            if user:

                stats = user["submitStats"]["acSubmissionNum"]

                return {
                    "username": user["username"],

                    "ranking": user["profile"]["ranking"],

                    "reputation": user["profile"]["reputation"],

                    "avatar": user["profile"]["userAvatar"],

                    "easySolved": stats[1]["count"],

                    "mediumSolved": stats[2]["count"],

                    "hardSolved": stats[3]["count"],

                    "totalSolved": (
                        stats[1]["count"] +
                        stats[2]["count"] +
                        stats[3]["count"]
                    )
                }

    except Exception as e:

        print("Error fetching user data:", e)

    return None


# ---------------- FETCH RECENT SUBMISSIONS ---------------- #

def fetch_recent_submissions(username):

    url = "https://leetcode.com/graphql"

    query = """
    query recentAcSubmissions($username: String!) {
      recentAcSubmissionList(username: $username) {
        title
        lang
        timestamp
      }
    }
    """

    variables = {
        "username": username
    }

    try:

        response = requests.post(
            url,
            json={
                "query": query,
                "variables": variables
            },
            headers=headers,
            timeout=15
        )

        if response.status_code == 200:

            data = response.json()

            submissions = data.get(
                "data",
                {}
            ).get(
                "recentAcSubmissionList",
                []
            )

            return submissions

    except Exception as e:

        print("Error fetching submissions:", e)

    return []