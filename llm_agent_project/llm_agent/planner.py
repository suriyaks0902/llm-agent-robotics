import subprocess

def query_llm(prompt):
    
    result = subprocess.run(['ollama', 'run', 'mistral'], input=prompt.encode(), stdout=subprocess.PIPE)
    return result.stdout.decode()
