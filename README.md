# **Cold Email Generator**

## **Overview**
The **Cold Email Generator** is an automated tool designed to streamline the process of extracting job postings from web pages and generating tailored cold emails. It leverages advanced AI language models, a structured portfolio database, and pre-processing utilities to deliver professional and impactful emails.

---

## **Features**
1. **Web Scraping Integration**: Extracts job-related content from URLs provided by the user.
2. **Job Extraction**: Converts raw web data into structured job postings in JSON format.
3. **Portfolio Matching**: Matches job requirements with relevant portfolio links to enhance credibility.
4. **Cold Email Generation**: Creates professional cold emails customized for the extracted jobs.

---

## **Modules**

### 1. **Streamlit Interface**
This module provides a user-friendly interface to interact with the generator.

#### **File: `main.py`**

##### **Key Features**
- Accepts a URL input via a text box.
- Initiates the process of job extraction and email generation upon submission.
- Displays the generated email in markdown format.

##### **Workflow**
1. Accepts a URL from the user.
2. Scrapes the content using `WebBaseLoader`.
3. Cleans the text using the `clean_text` utility.
4. Extracts jobs using the `Chain` class.
5. Matches skills with portfolio links using the `Portfolio` class.
6. Generates a cold email using the `Chain` class.

##### **Example**
```python
if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
```

---

### 2. **Portfolio Matching**
This module manages a portfolio database and matches job skills with relevant links.

#### **File: `portfolio.py`**

##### **Key Features**
- Loads a portfolio from a CSV file.
- Stores portfolio data in a ChromaDB vector store for efficient querying.
- Queries for relevant links based on extracted job skills.

##### **Workflow**
1. Loads portfolio data into a vector store.
2. Matches job skills with portfolio links using a similarity query.
3. Returns the top relevant links.

##### **Example**
```python
portfolio = Portfolio()
portfolio.load_portfolio()
links = portfolio.query_links(["Python", "Machine Learning"])
print(links)
```

---

### 3. **AI-Driven Job Extraction and Email Generation**
This module handles interaction with the language model for job extraction and email writing.

#### **File: `chain.py`**

##### **Key Features**
- Extracts job postings from cleaned web content using structured prompts.
- Generates customized cold emails with portfolio links.

##### **Workflow**
1. **Job Extraction**:
   - Processes cleaned text with structured prompts.
   - Outputs job details in JSON format.
2. **Cold Email Generation**:
   - Creates personalized emails based on job descriptions and portfolio links.

##### **Example**
```python
chain = Chain()
jobs = chain.extract_jobs(cleaned_text)
email = chain.write_mail(jobs[0], ["http://portfolio-link1.com"])
print(email)
```

---

### 4. **Text Cleaning Utility**
This module preprocesses raw web content for extraction.

#### **File: `utility.py`**

##### **Key Features**
- Removes HTML tags, URLs, special characters, and redundant spaces.
- Prepares clean, readable text for job extraction.

##### **Example**
```python
raw_text = "<div>Python Developer</div> Visit us at https://example.com!"
cleaned_text = clean_text(raw_text)
print(cleaned_text)
```

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/cold-email-generator.git
   cd cold-email-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file and add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. Ensure your portfolio CSV file is located at:
   ```
   D:\projects\cold-email-generator\app\resource\my_portfolio.csv
   ```

---

## **Usage**

### **Run the Application**
Start the Streamlit app:
```bash
streamlit run main.py
```

### **Input**
- Provide a URL containing job listings.
- Click "Submit."

### **Output**
- View the generated cold email, ready for use.

---

## **System Architecture**

1. **User Input**: URL provided via the Streamlit interface.
2. **Web Scraping**: Retrieves text content from the URL.
3. **Text Cleaning**: Sanitizes the scraped content.
4. **Job Extraction**: Identifies job postings and their details.
5. **Portfolio Matching**: Retrieves portfolio links relevant to job skills.
6. **Email Generation**: Creates personalized emails for the extracted jobs.

---

## **Example Workflow**

1. **Input**:  
   URL: `https://example.com/careers`

2. **Process**:  
   - Scraped text: "We are hiring Python Developers with 3+ years of experience..."
   - Cleaned text: "We are hiring Python Developers with 3 years of experience..."
   - Extracted jobs:
     ```json
     [
         {
             "role": "Python Developer",
             "experience": "3+ years",
             "skills": ["Python", "Django", "REST APIs"],
             "description": "Develop scalable web applications."
         }
     ]
     ```
   - Relevant portfolio links:
     - [Link 1](http://portfolio-link1.com)
     - [Link 2](http://portfolio-link2.com)

3. **Output**:  
   **Generated Email**:
   ```
   Subject: Exciting Opportunities to Collaborate on Your Needs

   Dear [Recipient Name],

   I’m Mohan, a Business Development Executive at XYZ, an AI & Software Consulting company specializing in scalable and efficient solutions. Based on your job listing for a Python Developer, we believe XYZ can empower your team with tailored applications. Please find our previous work here:

   1. [Link 1](http://portfolio-link1.com)
   2. [Link 2](http://portfolio-link2.com)

   Let’s connect to discuss how we can collaborate!

   Regards,  
   Mohan  
   ```

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push to branch: `git push origin feature-name`.
5. Submit a pull request.

---

