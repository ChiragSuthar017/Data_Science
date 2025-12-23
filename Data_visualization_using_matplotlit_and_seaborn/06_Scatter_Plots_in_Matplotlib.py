import matplotlib.pyplot as plt

study_hours = [1,2,3,4,5,6,7,8,9]
exam_score = [40,45,90,55,60,25,75,85,90]

# color = ['red' if score<50 else 'green' for score in exam_score] 
sizes = [score*2 for score in exam_score] # adjust size
social_scores = [12,34,67,555,678,145,56,999,445]
plt.scatter(study_hours, exam_score, c=social_scores, cmap='viridis')
plt.grid(True)
plt.colorbar(label="score") # add color bar
for i in range (len(study_hours)):
    plt.annotate(f'S{i+1}',(study_hours[i], exam_score[i]-2.5)) # add names
plt.xlabel('study hours')
plt.ylabel('exam score')
plt.title('study vs marks')
plt.show()

# Multiple Groups in One Plot

class_a_hours = [2, 4, 6, 8]
class_a_scores = [95, 55, 65, 85]
 
class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 90]

plt.scatter(class_a_hours, class_a_scores, label='A', color='blue')
plt.scatter(class_b_hours, class_b_scores, label='B', color='red')
plt.title('scatter plot: Class A vs Class B')
plt.xlabel('Study Score')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()