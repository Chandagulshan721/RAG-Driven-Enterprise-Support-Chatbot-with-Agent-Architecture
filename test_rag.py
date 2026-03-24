from agent_service import run_agent

question = "What is the return policy?"

answer = run_agent(question)

print("Question:", question)
print("\nAI Answer:\n")
print(answer)