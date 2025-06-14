import re

def interpret_mission_response(response: str):
    """
    Parses the LLM response to extract a sequence of subtasks.

    Args:
        response (str): Full response from the LLM.

    Returns:
        list[str]: A list of ordered subtasks.
    """
    lines = response.splitlines()
    subtasks = []

    for line in lines:
        line = line.strip()
        if re.match(r"^(\d+\.|-)", line):
            task = re.sub(r"^(\d+\.\s*|- )", "", line)
            subtasks.append(task)

    if not subtasks and response.strip():
        subtasks.append(response.strip())

    return subtasks
