from groq import Groq
from rag_service import retrieve_context
from tools import calculator_tool, order_status_tool

# 🔑 Add your API key here
client = Groq(api_key="GROQ_API_KEY")

# Memory
conversation_memory = []


# -------------------------------
# 🧠 Decision Functions
# -------------------------------

def is_policy_question(q):
    keywords = ["policy", "return", "exchange", "shipping", "warranty"]
    return any(word in q.lower() for word in keywords)


def is_math_question(q):
    return any(char.isdigit() for char in q)


def is_order_question(q):
    return "order" in q.lower()


# -------------------------------
# 🚀 MAIN AGENT FUNCTION
# -------------------------------

def run_agent(question):

    global conversation_memory

    # -------------------------------
    # 🧠 STEP 1 — DECISION MAKING
    # -------------------------------

    # 👉 Tool 1: Calculator
    if is_math_question(question):
        return calculator_tool(question)

    # 👉 Tool 2: Order status
    elif is_order_question(question):
        return order_status_tool("123")  # dummy order id

    # 👉 Tool 3: RAG (company policy)
    elif is_policy_question(question):
        context = retrieve_context(question)
        system_message = "You are a customer support assistant. Answer using company policy."

    # 👉 Tool 4: Normal Chat
    else:
        context = ""
        system_message = "You are a friendly AI assistant."

    # -------------------------------
    # 🧠 STEP 2 — BUILD CHAT MEMORY
    # -------------------------------

    messages = [{"role": "system", "content": system_message}]

    for msg in conversation_memory:
        messages.append(msg)

    messages.append({"role": "user", "content": question})

    # Add RAG context if available
    if context:
        messages.append({
            "role": "system",
            "content": f"Context:\n{context}"
        })

    # -------------------------------
    # 🤖 STEP 3 — CALL LLM
    # -------------------------------

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant"
    )

    answer = response.choices[0].message.content

    # -------------------------------
    # 💾 STEP 4 — SAVE MEMORY
    # -------------------------------

    conversation_memory.append({"role": "user", "content": question})
    conversation_memory.append({"role": "assistant", "content": answer})

    return answer