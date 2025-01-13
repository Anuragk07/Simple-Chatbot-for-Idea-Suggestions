import os
import streamlit as st
from langchain_groq import ChatGroq

# Load API Key from environment variables
API_KEY = os.getenv("GROQ_API_KEY", "Your_API_Key")

# Initialize the Llama model with LangChain's ChatGroq
llm = ChatGroq(
    temperature=1,
    groq_api_key=API_KEY,
    model_name="mixtral-8x7b-32768"
)

# Function to generate ideas
def generate_ideas(query):
    # Define a detailed system prompt
    system_prompt = (
        "You are an expert assistant specializing in creative idea generation. "
        "Your goal is to help users generate innovative and actionable app ideas. "
        "Provide exactly three unique app ideas that are short, clear, and tailored to the query."
    )
    
    # Combine system and user messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    
    # Use the `invoke` method to call the model
    response = llm.invoke(messages)
    
    # Extract and clean the ideas
    raw_ideas = response.content.split("\n")
    cleaned_ideas = [idea.strip() for idea in raw_ideas if idea.strip()]  # Remove blanks and extra spaces
    
    # Ensure only 3 ideas are returned
    return cleaned_ideas[:3]

# Rank ideas based on relevance, impact, and feasibility
def rank_ideas(ideas, query):
    ranked_ideas = []
    for idea in ideas:
        relevance = len(set(query.split()) & set(idea.split()))  # Number of common keywords
        relevance_score = min(5, relevance)  # Cap the score at 5

        impact_score = min(5, len(idea.split()) // 2)  # Longer ideas get higher scores, capped at 5

        feasibility_score = 5 - min(4, len(idea.split()) // 3)  # Shorter ideas score higher

        priority_score = relevance_score + impact_score + feasibility_score

        ranked_ideas.append((idea, priority_score))
    ranked_ideas.sort(key=lambda x: x[1], reverse=True)
    return ranked_ideas

# Expand on selected ideas
def expand_idea(idea):
    return f"Expand features like {idea.lower()}. Market to target groups, and use SEO strategies to maximize reach."

# Initialize session state variables
if "ideas" not in st.session_state:
    st.session_state["ideas"] = []
if "ranked_ideas" not in st.session_state:
    st.session_state["ranked_ideas"] = []
if "selected_indices" not in st.session_state:
    st.session_state["selected_indices"] = []

# Streamlit UI
st.title("Simple Chatbot for Idea Suggestions")

# User Input
query = st.text_input("Enter your query (e.g., 'What new app should I build?')", "What new app should I build?")

if st.button("Generate Ideas"):
    # Generate Ideas and store in session state
    st.session_state["ideas"] = generate_ideas(query)
    st.session_state["ranked_ideas"] = rank_ideas(st.session_state["ideas"], query)

# Display Generated Ideas
if st.session_state["ideas"]:
    st.subheader("Generated Ideas")
    for idx, idea in enumerate(st.session_state["ideas"], 1):
        st.write(f"{idx}. {idea}")
    
    # Display Ranked Ideas
    if st.session_state["ranked_ideas"]:
        st.subheader("Ranked Ideas (by priority)")
        for idx, (idea, priority) in enumerate(st.session_state["ranked_ideas"], 1):
            st.write(f"{idx}. {idea} (Priority: {priority})")

    # User Selection
    st.session_state["selected_indices"] = st.multiselect(
        "Select two ideas you like:",
        options=list(range(1, len(st.session_state["ideas"]) + 1)),
        format_func=lambda x: f"{x}. {st.session_state['ideas'][x-1]}",
        default=st.session_state["selected_indices"]
    )

    # Display Detailed Suggestions
    if len(st.session_state["selected_indices"]) == 2:
        st.subheader("Detailed Suggestions for Selected Ideas")
        for idx in st.session_state["selected_indices"]:
            expanded = expand_idea(st.session_state["ideas"][idx - 1])
            st.write(f"- **{st.session_state['ideas'][idx - 1]}**: {expanded}")
    elif len(st.session_state["selected_indices"]) > 2:
        st.warning("Please select only two ideas.")
    elif len(st.session_state["selected_indices"]) < 2:
        st.warning("Please select at least two ideas.")
