# def main():
#     print("✅ LLM Agent Pipeline starting...")
#     print("🔄 Planner: interpreting user mission")
#     print("👁️ Perception: scanning environment")
#     print("🤖 Control: sending nav goals")
#     print("✅ Mission complete.")

import yaml
from pathlib import Path
from llm_agent_project.llm_agent.planner import query_llm
from llm_agent_project.llm_agent.interpreter import interpret_mission_response


def main():
    print("✅ LLM Agent Pipeline starting...")

    config_path = Path(__file__).resolve().parents[2] / 'llm_agent_project' / 'config' / 'agent_config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    mission = config.get('mission', 'No mission found.')
    print(f"🧠 Mission from config: {mission}")

    prompt = f"""You are a robot assistant. Break the following mission into simple step-by-step tasks.
    Mission: {mission}
    Return the steps in numbered list format.
    """

    response = query_llm(prompt)
    print("🤖 LLM Response:", response)

    subtasks = interpret_mission_response(response)
    print("🧩 Interpreted Subtasks:")
    for i, task in enumerate(subtasks, 1):
        print(f" Executing step {i}: {task}")

    print("✅ Mission complete.")


if __name__ == '__main__':
    main()


