import numpy as np

student_scores = np.array([
    [85, 78, 90, 82],
    [92, 88, 85, 80],
    [76, 95, 89, 91],
    [88, 84, 92, 86]
])

subjects = ["Math", "Science", "English", "History"]

# Calculate average of each subject
averages = np.mean(student_scores, axis=0)

print("Average score for each subject:")
for subject, average in zip(subjects, averages):
    print(subject, ":", average)

# Find subject with highest average
highest_index = np.argmax(averages)

print("\nSubject with highest average:", subjects[highest_index])
print("Highest average score:", averages[highest_index])