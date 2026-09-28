courses = []
DATA_FILE = 'data.txt'

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    name, score, credit = line.split(',')
                    courses.append({
                        'name' : name,
                        'score' : score,
                        'credit' : credit
                    })
    except FileNotFoundError:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            pass


def save_data():
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for c in courses:
            f.write(f"{c['name']}, {c['score']}, {c['credit']}")


def score_to_gpa(score):
    if score >= 80:
        return 4.0
    elif score >= 70:
        return 3.67
    elif score >= 60:
        return 3.33
    elif score >= 50:
        return 3.0
    elif score >= 40:
        return 2.67
    else:
        return 0.0


def calculate_gpa():
    total_score = 0
    total_credit = 0
    for c in courses:
        g = score_to_gpa(c['score'])
        total_score += g * c['credit']
        total_credit += c['credit']
    if total_credit == 0.0:
        return 0.0
    return round(total_score / total_credit, 2)


def add_course():
    name = input("Please enter a course to add: ")
    score = float(input("Please enter your score: "))
    credit = float(input("Please enter your credit: "))

    courses.append({
        'name' : name, 
        'score' : score,
        'credit' : credit
    })

    save_data()
    print("Your score has already saved automatically")

def delete_course():
    if not courses:
        print("No record can delete")
        return
    found = False
    name = input("Please enter a course you want to delete: ")
    for c in courses:
        if c['name'] == name:
            courses.remove(c)
            save_data()
            new_gpa = calculate_gpa()
            print("Successfully delete the course")
            print(f"Your new GPA is {new_gpa}")
            found = True
    if not found:
        print("Unsuccessfully delete")


def show_all():
    print("All GPA record: ")
    if not courses:
        print("No record")
        return
    for idx, c in enumerate(courses, 1):
        g = calculate_gpa()
        print(f"{idx}.{c['name']} | score: {c['score']} | credit: {c['credit']} | score of one course: {g}")
    print(f"Current overall GPA: {calculate_gpa()}")


def main():
    while True:
        print("GPA control system: ")
        print("1. Adding a course: ")
        print("2. Deleting a course: ")
        print("3. Checking your GPA: ")
        print("4. Quit")
        choices = input("Please enter a number of functions: ")

        if choices == '1':
            add_course()
        elif choices == '2':
            delete_course()
        elif choices == '3':
            show_all()
        elif choices == '4':
            print("Quit and your GPA was saved automatically")
            break
        else:
            print("Error number")


if __name__ == "__main__":
    main()
