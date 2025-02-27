from fuzzywuzzy import process

# Define responses to frequently asked questions
# The key is the user query and the value is the response to the query
response = {
    "How do I apply for a program at RITA Africa?": "To apply for a program at RITA Africa, simply visit our website and join the next Python Developer Bootcamp organized by InfoSorse. Upon successful completion of the bootcamp, use your certificate to apply for any RITA Africa program. Complete the online application form, ensuring you provide accurate information and upload required documents, such as proof of identity. Once your application is submitted, our admissions team will review it and notify you of the next steps.",
    "Can I apply if I'm not based in Africa?" : "Given the stated requirement that applicants must be both African citizens and residents in Africa, if you are not currently residing in Africa, you would not meet the eligibility criteria for the application, even if you hold African citizenship.",
    "What types of certifications do you offer?" : "RITA Africa offers industry-recognized certifications in various tech-related fields, including data analytics, cloud computing, software engineering, cybersecurity, and more. Our certifications are designed to equip you with the skills and credentials you need to succeed in your chosen career path.",
    "How long are the programs?" : "Program durations vary depending on the specific course. Some programs may be completed in 9 months, while others may span 12 months. Visit our website or check the program page for information on the duration of your chosen program."
}

# Function to save unknown user input in a txt file for future training
def save_unknown_input(input_text):
    with open("unknown_input.txt", "a") as file:
        file.write(input_text + "\n")

# Function to get the best response to a user query using fuzzy matching
def get_best_response(user_query):
    best_response, score = process.extractOne(user_query, response.keys())
    return best_response if score > 80 else None

# Define bot function
def chatbot():
    print("Welcome to RITA Africa! How can I help you today?")
    print("You can type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Thank you for chatting with me. Have a great day!")
            break

        if best_response := get_best_response(user_input):
            print("Bot:" ,response[best_response])
        else:
            print("Bot: I'm sorry, I don't have the answer to that question. Can you try to rephrase it?")
            save_unknown_input(user_input)

# Run the chatbot
chatbot()