import colorama

colorama.init(autoreset=True)

# Some color variables
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE

# Some background color variables
BACKGROUND_RED = colorama.Back.RED
BACKGROUND_GREEN = colorama.Back.GREEN
BACKGROUND_YELLOW = colorama.Back.YELLOW
BACKGROUND_BLUE = colorama.Back.BLUE

# Bold text
BOLD = colorama.Style.BRIGHT

# Price variable
price = 0.000

print(BOLD + YELLOW + "Welcome to kaun banega crore pati")
# list of questions
ques = [
    "What is the capital of India?",
    "What is the capital of Russia?",
    "What is the capital of Japan?",
    "Who is the founder of OpenAI?",
    "Who is the founder of Amazon?",
    "Who is the founder of Apple?",
    "Who is the founder of Facebook?",
    "Who is the founder of Microsoft?",
]

# list of hints
hints = [["Delhi", "Mumbai", "Kolkata", "Chennai"],
         ["Tokyo", "Berlin", "Moscow", "Seoul"],
         ["Tokyo", "Seoul", "Shanghai", "Beijing"],
         ["Bill Gates", "Mark Zuckerberg", "Elon Musk", "Sam Altman"],
         ["Tim Cock", "Tim Barne-Lee", "Jeff Bezos", "Larry Page"],
         ["Steve Jobs", "Tim Cock", "Warren Buffet", "Georgin Zulis"],
         ["Bill Gates", "Larry Page", "Mark Zuckerberg", "Jeff Bezos"],
         ["Steve Jobs", "Tim Cock", "Bill Gates", "Georgin Zulis"]]

# tuple of correct answers
ans = (1, 3, 1, 4, 3, 1, 3, 3)

# printing all the answers
for i in range(len(hints)):
    print(RED + f"Q{i + 1}.{ques[i]}")

    for j in range(len(hints[i])):
        print(BACKGROUND_BLUE + f"{j + 1}.{hints[i][j]}")
    print()

    # taking user input
    user = int(input("Enter your answer: "))
    if user == ans[i]:
        print("Correct Answer")
        price = price + 400.50
    else:
        print("Wrong Answer")

print(f"Your Reward is {GREEN + f"${price:.2f}"}")
