
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

number_of_exams = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

score_student1 = [10, 20, 30, 40, 40, 35, 25, 37, 43, 50]
score_student2 = [15, 22, 36, 45, 24, 32, 27, 30, 28, 47]
score_student3 = [18, 24, 35, 47, 41, 38, 22, 31, 32, 40]

labels = ['score_student1', 'score_student2', 'score_student3']
colors = ['yellow', 'red', 'blue']

plt.stackplot(number_of_exams, score_student1, score_student2, score_student3, labels=labels, colors=colors)

plt.legend(loc='upper left')

plt.title("My Stock Plot")
plt.tight_layout()
plt.show()
