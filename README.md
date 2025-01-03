# Art Paris LinkedIn Scraper

## Streamlit Web Application

This Streamlit application allows users to process salon data by:
- Uploading CSV or Excel files
- Selecting specific salons
- Choosing job roles
- Sending data to a Make webhook for further processing

### Features
- File upload support (CSV, XLS, XLSX)
- Salon and role selection
- Webhook integration for data processing

### Deployment on Streamlit Share

#### Configuration Steps
1. Fork this repository to your GitHub account
2. Create a Streamlit Share account (https://streamlit.io/cloud)
3. Replace the webhook URL in `.streamlit/secrets.toml`:
   ```toml
   MAKE_WEBHOOK_URL = "YOUR_ACTUAL_MAKE_WEBHOOK_URL"
   ```

#### Prerequisites
- Streamlit account
- Make account with configured webhook
- GitHub account

#### Local Development
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run app.py
   ```

### Secrets Management
- The `secrets.toml` file is used to store sensitive information like webhook URLs
- NEVER commit the actual webhook URL to version control
- Use placeholder values in the repository
- Replace with actual values during deployment

### Troubleshooting
- Ensure all dependencies are installed
- Verify webhook URL is correct
- Check Streamlit Share deployment logs for any errors
