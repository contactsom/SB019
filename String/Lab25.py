# Formate of String
simplilearnBootCam="Simplilearn got 8 Million Learners having 700+ Live class monthly and 550 + Learning and 100+ Hands - on projects"
print(simplilearnBootCam)


print(
        "Simplilearn got %(numberofLearners)d Million Learners having 700+ Live class monthly and 550 + Learning and 100+ Hands - on projects"
       %{
            'numberofLearners':8
        }
)

print(
        "Simplilearn got %(numberofLearners)d Million Learners having %(liveclass)d + Live class monthly and 550 + Learning and 100+ Hands - on projects"
       %{
            'numberofLearners':8,
            'liveclass':700
        }
)

print(
        "Simplilearn got %(numberofLearners)d Million Learners having %(liveclass)d + Live class monthly and %(learning)d + Learning and %(projects)d + Hands - on projects"
       %{
            'numberofLearners':8,
            'liveclass':700,
            'learning':550,
            'projects':100
        }
)
print(
        "%(edtech)s got %(numberofLearners)d Million Learners having %(liveclass)d + Live class monthly and %(learning)d + Learning and %(projects)d + Hands - on projects"
       %{
            'numberofLearners':8,
            'liveclass':700,
            'learning':550,
            'projects':100,
            'edtech':"Simplilearn"
        }
)
