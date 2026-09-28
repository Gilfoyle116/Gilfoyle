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
            f.write(f"{c['name']}, {c['score']}, {c['credit']}\n")


def scores_to_gpa(score):
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
        g = scores_to_gpa(c['score'])
        total_score += g * c['credit']
        total_credit += c['credit']
    if total_credit == 0.0:
        return 0.0
    return round(total_score / total_credit, 2)


def add_course():
    name = input('Please enter a subject: ')
    score = float(input('Please enter your scores: '))
    credit = float(input('Please enter your credit: '))

    courses.append({
        'name' : name,
        'score' : score,
        'credit' : credit
    })

    save_data()
    print("Your scores have already saved")

def show_all():
    print("All GPA record: ")
    if not courses:
        print("No record")
        return
    for idx, c in enumerate(courses, 1):
        g = scores_to_gpa(c['score'])
        print(f"{idx}.{c['name']} | scores: {c['score']} | credit: {c['credit']} | scores of one subject: {g}")
    print(f"Current overall GPA: {calculate_gpa()}")


def main():
    while True:
        print("GPA control system")
        print("1. Adding a course: ")
        print("2. Checking your GPA: ")
        print("3. Quit: ")
        choices = input("Please enter numbers of functions: ")

        if choices == '1':
            add_course()
        elif choices == '2':
            show_all()
        elif choices == '3':
            print("Quit and all your GPA was saved")
            break
        else:
            print("Error numbers")


if __name__ == '__main__':
    main()