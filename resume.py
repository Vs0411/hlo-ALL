def create_resume(name, email, phone, skills, experience, education):
    resume = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}

    Skills:
    {format_list(skills)}

    Experience:
    {format_list(experience)}

    Education:
    {format_list(education)}
    """
    return resume


def format_list(items):
    formatted = ""
    for item in items:
        formatted += "- " + item + "\n"
    return formatted


# Example usage
name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

skills = []
num_skills = int(input("Enter the number of skills: "))
for _ in range(num_skills):
    skill = input("Enter a skill: ")
    skills.append(skill)

experience = []
num_experience = int(input("Enter the number of experiences: "))
for _ in range(num_experience):
    position = input("Enter the position: ")
    company = input("Enter the company: ")
    duration = input("Enter the duration: ")
    experience.append(f"{position} at {company} ({duration})")

education = []
num_education = int(input("Enter the number of education details: "))
for _ in range(num_education):
    degree = input("Enter the degree: ")
    institution = input("Enter the institution: ")
    duration = input("Enter the duration: ")
    education.append(f"{degree} from {institution} ({duration})")

resume = create_resume(name, email, phone, skills, experience, education)
print(resume)