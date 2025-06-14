# 🤖 LLM-Powered Autonomous Agent for Robotics Simulation
This project implements a ROS 2-based autonomous agent powered by a local LLM (Mistral via Ollama) to interpret user-defined missions and break them into executable subtasks. It simulates a robotics pipeline with Perception → Planning → Control, using an LLM for intelligent task interpretation.

## 📁 Folder Structure (simplified)
```bash

llm_ws/
├── src/
│   └── llm_agent_project/
│       ├── llm_agent/            # Planner and interpreter logic
│       ├── scripts/              # Entrypoint (main.py)
│       ├── config/               # agent_config.yaml (mission)
│       └── ... (control, sim_env, perception, etc.)
```

## ⚙️ Setup & Installation
### 1. Clone & Setup Workspace
```bash

git clone https://github.com/suriyaks0902/llm-agent-robotics.git
cd llm-agent-robotics/..
mv llm-agent-robotics llm_agent_project
mkdir -p llm_ws/src
mv llm_agent_project llm_ws/src/
cd llm_ws
```

### 2. Create Python Virtual Environment (Optional but recommended)
```bash

python3 -m venv llm_env
source llm_env/bin/activate
pip install -r src/llm_agent_project/requirements.txt  # if you add one later
```

### 3. Install and Run Local LLM with Ollama
Make sure you have ollama installed:

```bash

ollama pull mistral
```
This pulls the local mistral model used for mission interpretation.

### 🚀 Build and Run the Agent
```bash

cd ~/llm_ws
source /opt/ros/humble/setup.bash  # or your ROS 2 version
rm -rf build/ install/ log/
colcon build
source install/setup.bash
ros2 run llm_agent_project run_agent
```

### 📜 Mission Configuration
Define your task in config/agent_config.yaml:

```yaml

mission: "Pick up the red cube and place it on the table"
```

The LLM will interpret this into ordered subtasks like:

```markdown

1. Locate the red cube
2. Approach the red cube
3. Grasp it
...
```

These subtasks are then printed and can later be passed to perception/control modules.

### ✅ Output Sample
```sql

✅ LLM Agent Pipeline starting...
🧠 Mission from config: Pick up the red cube and place it on the table
🤖 LLM Response: 
1. Locate the red cube
2. Approach the red cube
...

```

### 🧩 Interpreted Subtasks:
 Executing step 1: Locate the red cube
 Executing step 2: Approach the red cube
 ...
✅ Mission complete.

### 📌 Next Steps (Planned)
 Execute subtasks using simulated control

 Integrate real perception data

 Connect to a physics simulator (e.g., Gazebo or CARLA)

