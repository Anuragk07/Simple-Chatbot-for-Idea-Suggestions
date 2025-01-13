Simple Chatbot for Idea Suggestions
Project Overview
This project is a text-based chatbot that helps users generate creative ideas for app development, prioritize them, and receive detailed suggestions. The chatbot is built using Streamlit for the user interface and LangChain’s ChatGroq model for idea generation.

Features
Generate Ideas:

Accepts a user query and generates three unique app ideas.
Priority Ranking System:

Ranks the ideas based on relevance, impact, and feasibility to highlight the best options.
Idea Expansion:

Provides detailed suggestions for any two ideas selected by the user.
Interactive Interface:

A simple and intuitive UI for seamless interaction.
Demo Video
Watch the demo here

Technologies Used
Backend: LangChain (ChatGroq API)
Frontend: Streamlit
Programming Language: Python
Setup Instructions
1. Clone the Repository:
bash
Copy code
git clone <repository_link>  
cd <repository_name>  
2. Install Dependencies:
Ensure you have Python installed, then run:

bash
Copy code
pip install -r requirements.txt  
3. Add Your API Key:
Set your GROQ_API_KEY in the environment variables:

bash
Copy code
export GROQ_API_KEY="your_api_key_here"  
4. Run the Application:
Launch the Streamlit app:

bash
Copy code
streamlit run app.py  
How It Works
User Query:
The user enters a query, such as "What new app should I build?".

Idea Generation:
The chatbot generates three unique ideas using LangChain’s ChatGroq API.

Priority Ranking:
Ideas are ranked based on their relevance, impact, and feasibility.

User Selection:
The user selects two ideas to receive detailed suggestions.

Detailed Suggestions:
The chatbot provides actionable details for the selected ideas.

Bonus Feature
The priority ranking system evaluates ideas based on:

Relevance: How closely the idea aligns with the query.
Impact: Potential influence or innovation of the idea.
Feasibility: Practicality and ease of implementation.
Future Enhancements
Adding support for multilingual queries.
Providing an option to save ideas and suggestions.
Integrating with additional AI APIs for diversified idea generation.
