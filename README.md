# **Simple Chatbot for Idea Suggestions**  

## **Project Overview**  
This project is a text-based chatbot that helps users generate creative ideas for app development, prioritize them, and receive detailed suggestions. The chatbot is built using **Streamlit** for the user interface and **LangChain’s ChatGroq** model for idea generation.  

## **Features**  
1. **Generate Ideas:**  
   - Accepts a user query and generates three unique app ideas.  

2. **Priority Ranking System:**  
   - Ranks the ideas based on relevance, impact, and feasibility to highlight the best options.  

3. **Idea Expansion:**  
   - Provides detailed suggestions for any two ideas selected by the user.  

4. **Interactive Interface:**  
   - A simple and intuitive UI for seamless interaction.  

---

## **Demo Video**  
[Watch the demo here](<[insert_your_video_link_here](https://drive.google.com/file/d/1LLCfeBzmRkQvYeG1mRYGKcb1AQmaipnK/view?usp=sharing)>)  

---

## **Technologies Used**  
- **Backend:** LangChain (ChatGroq API)  
- **Frontend:** Streamlit  
- **Programming Language:** Python  

---

## **Setup Instructions**  

### **1. Clone the Repository:**  
```bash  
git clone <repository_link>  
cd <repository_name>  
```  

### **2. Install Dependencies:**  
Ensure you have Python installed, then run:  
```bash  
pip install -r requirements.txt  
```  

### **3. Add Your API Key:**  
Set your **GROQ_API_KEY** in the environment variables:  
```bash  
export GROQ_API_KEY="your_api_key_here"  
```  

### **4. Run the Application:**  
Launch the Streamlit app:  
```bash  
streamlit run app.py  
```  

---

## **How It Works**  

1. **User Query:**  
   The user enters a query, such as *"What new app should I build?"*.  

2. **Idea Generation:**  
   The chatbot generates three unique ideas using LangChain’s ChatGroq API.  

3. **Priority Ranking:**  
   Ideas are ranked based on their relevance, impact, and feasibility.  

4. **User Selection:**  
   The user selects two ideas to receive detailed suggestions.  

5. **Detailed Suggestions:**  
   The chatbot provides actionable details for the selected ideas.  

---

## **Bonus Feature**  
The **priority ranking system** evaluates ideas based on:  
- **Relevance:** How closely the idea aligns with the query.  
- **Impact:** Potential influence or innovation of the idea.  
- **Feasibility:** Practicality and ease of implementation.  

---

## **Future Enhancements**  
- Adding support for multilingual queries.  
- Providing an option to save ideas and suggestions.  
- Integrating with additional AI APIs for diversified idea generation.  
