# Email Mass Sender

This project is a Python-based email mass sender that allows you to send personalized emails to multiple recipients, with the option to CC additional recipients. It uses SMTP to send emails and supports personalization through the use of a CSV file containing recipient details.

## Features

- Send emails to multiple recipients using a CSV file.
- Personalize the greeting with each recipient's first name.
- Supports CC recipients.
- Use HTML templates for the email body.
- Easily customizable for different SMTP servers.

## Requirements

- Python 3.6+
- A valid SMTP server (e.g., Gmail, company mail server).
- A `.env` file for storing sensitive information (SMTP credentials).

### Libraries

- `pandas`: For handling CSV files.
- `smtplib`: For sending emails via SMTP.
- `email`: For composing the email content.
- `python-dotenv`: For loading environment variables.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/andrewbarker96/email-mass-sender.git
cd email-mass-sender
```

### 2. Install Required Packages
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Edit the `.env` file in the root directory of the project with the following variables:
```env
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_password
EMAIL_SUBJECT="Your Email Subject"
```
* Ensure that you do not publish your .env to your public repository!

### 4. Prepare the CSV File
To send emails to multiple recipients, you need to create a CSV file (`testList.csv`) with two columns: `fullName` and `email`. The `fullName` column contains the full names of your recipients, and the email column contains their respective email addresses.

Example `testList.csv`:
```csv
fullName,email
John Doe,john.doe@example.com
Jane Smith,jane.smith@example.com
```

### 5. Create the CC List (Optional)
If you want to CC recipients, create another CSV file (`ccList.csv`) containing a single column email with the list of `email` addresses to be CCed.

Example `ccList.csv`:
```csv
email
cc1@example.com
cc2@example.com
```

### 6. Prepare the Email Body
Create an `HTML` file named `body.html` in the project folder. This will serve as the content of the email body.

Example `body.html`:
```html
<p>Hello,</p>
<p>This is a sample email body. Feel free to customize it!</p>
```

### 7. Run the Script
After setting up the environment and CSV files, you can run the script:
```bash
python main.py
```
The script will send personalized emails to all recipients in the CSV file, with each email addressed to the recipient's first name (e.g., "Dear John").

## Customization
- You can modify the email body (`body.html`) to suit your needs.
- The script supports both HTML and plain text email formats. Simply update the MIME type in the code (`MIMEText(personalized_body, 'html')` or `'plain'`).

## Contributing
Feel free to fork this project and submit pull requests for new features or bug fixes. Any contributions are welcome!

## License
This project is licensed under the MIT License.