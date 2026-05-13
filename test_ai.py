from grok_ai import generate_roadmap

dummy_data = {
    "totalSolved": 400,
    "easySolved": 200,
    "mediumSolved": 150,
    "hardSolved": 50
}

result = generate_roadmap(dummy_data)

print(result)