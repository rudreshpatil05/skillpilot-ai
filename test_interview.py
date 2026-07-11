from src.interview.interview_generator import generate_interview_questions

role = "Data Scientist"

questions = generate_interview_questions(role)

print("=" * 50)
print(f"Interview Questions for: {role}")
print("=" * 50)

print("\n🟢 Easy Questions")
for q in questions["Easy"]:
    print("•", q)

print("\n🟡 Medium Questions")
for q in questions["Medium"]:
    print("•", q)

print("\n🔴 Hard Questions")
for q in questions["Hard"]:
    print("•", q)