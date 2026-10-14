LETTERS = ["A", "B", "C", "D"]


def _options(doc) -> list[str]:
    return [doc["option1"], doc["option2"], doc["option3"], doc["option4"]]


def doc_to_text(doc) -> str:
    """The prompt of the MILU authors' evaluation (github.com/AI4Bharat/MILU):

    Question: <question>
    Choices:
    A. <option1>
    ...
    D. <option4>
    Answer:
    """
    prompt = "Question: " + doc["question"] + "\nChoices:\n"
    for letter, option in zip(LETTERS, _options(doc), strict=True):
        prompt += f"{letter}. {option}\n"
    return prompt + "Answer:"


def doc_to_choice(doc) -> list[str]:
    return _options(doc)


def doc_to_target(doc) -> int:
    """`target` names the correct option: "option1" .. "option4"."""
    return int(doc["target"].strip().removeprefix("option")) - 1
