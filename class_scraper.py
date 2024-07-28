import fitz  # PyMuPDF
import re
import pymysql

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Tomcar123!',
    'database': 'coursesniper'
}

# Path to your PDF file (use raw string to avoid escape issues)
pdf_path = r"2023-2024+Courses.pdf"  # Replace with the actual path to your PDF file

# Function to extract class codes from PDF
def extract_class_codes_from_pdf(pdf_path):
    text = ''
    # Open the PDF file
    document = fitz.open(pdf_path)
    
    # Iterate through each page in the PDF
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    
    document.close()
    return text

# Function to find and extract class codes from text
def find_class_codes(text):
    class_codes = re.findall(r'\b[A-Za-z]{2,4}\s\d{5}\b', text)
    return class_codes

# Function to save class codes to MySQL database
def save_to_database(class_codes):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            # Create table if not exists
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS class_codes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                class_code VARCHAR(50) NOT NULL UNIQUE
            )
            """)
            
            # Insert class codes if they don't already exist
            for code in class_codes:
                try:
                    cursor.execute("INSERT INTO class_codes (class_code) VALUES (%s)", (code,))
                except pymysql.err.IntegrityError:
                    # This error is raised if the class_code already exists due to the UNIQUE constraint
                    print(f"Duplicate entry found: {code}")
        connection.commit()
    finally:
        connection.close()

if __name__ == "__main__":
    try:
        # Step 1: Extract text from PDF
        extracted_text = extract_class_codes_from_pdf(pdf_path)
        
        # Step 2: Find class codes in extracted text
        class_codes = find_class_codes(extracted_text)
        
        # Step 3: Save class codes to database
        save_to_database(class_codes)
        
        print(f"Successfully saved {len(class_codes)} class codes to the database.")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
