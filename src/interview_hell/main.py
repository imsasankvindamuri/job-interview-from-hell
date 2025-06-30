import json
import random
import os
from pathlib import Path
from time import sleep
from inputimeout import inputimeout, TimeoutOccurred


# The code here is trash, like all game code.
# It is held together by Granma Monty's secret
# spaghetti sauce.

def get_option_input(prompt : str, time : int | float) -> int | str:
    VALID_OPTIONS = [0, 1, 2, 3]
    try:
        answer = int(inputimeout(prompt, time))
        return answer if answer in VALID_OPTIONS else "invalid_option"
    except Exception as e:
        match e:
            case TimeoutOccurred():
               return "too_slow"
            case ValueError():
                return "disobedience"
            case _:
                return "insubordination"

def main() -> None:
    # Build the path to questions.json
    questions_path = Path(__file__).parent / "questions.json"

    # Load questions from the JSON file
    with open(questions_path, "r", encoding="utf-8") as f:
        questions: dict[str, dict[str, list[str]]] = json.load(f)

    # Initialize state variables
    is_running : bool = True
    time : float = 10.0
    truth_cache : dict[str, str] = {}
    while is_running:
        os.system("cls" if os.name == "nt" else "clear")
        question_type: str = random.choice(list(questions.keys()))
        question: str = random.choice(questions[question_type]["variants"])
        options : list[str] = random.sample(questions[question_type]["options"], \
                    len(questions[question_type]["options"]))

        print(question)
        print(options)
        answer : int | str = get_option_input("Choose the right option {0,1,2,3}: ", time)
        if not isinstance(answer, int):
            is_running = not is_running
        else:
            if question_type not in truth_cache.keys():
                truth_cache[question_type] = options[answer]
            else:
                if truth_cache[question_type] != options[answer]:
                    print("You answered differently for similar question earlier, you paragon of dishonesty.")
                    print(f"You said the answer was: {truth_cache[question_type]}")
                    is_running = not is_running
                    sleep(1)
                time = max(2,time*(0.8))
    match answer:
        case "invalid_option":
            print("At Enterprise-Grade Toasters LLC, we are looking for people with functioning brain cells.")
        case "too_slow":
            print("At Enterprise-Grade Toasters LLC, we are looking for a work ethic to disrupt the disruption.")
        case "disobedience":
            print("At Enterprise-Grade Toasters LLC, we are looking for lone wolves with a team spirit.")
        case "insubordination":
            print("At Enterprise-Grade Toasters LLC, we are require unquestioning work from our freethinking employees.")
        case _:
            print("You have clearly shown yourself to be incapable of loyalty to Enterprise-Grade Toasters LLC.")

    print("As such, we have decided to reject your application.")
    print("Please fill your form and pay your interview fees of $70000.")
