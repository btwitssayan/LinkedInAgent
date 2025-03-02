from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options  # To configure Firefox in headless mode
import time

class LinkedInBot:
    def __init__(self, email: str, password: str, driver_path: str):
        """
        Initialize the LinkedInBot with user credentials and ChromeDriver path.
        
        :param email: User's LinkedIn email/username.
        :param password: User's LinkedIn password.
        :param driver_path: Path to the ChromeDriver executable.
        """
        self.email = email
        self.password = password
        # Set up the ChromeDriver service
        # service = Service(driver_path)
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")  # Disable GPU for stability in headless mode
        self.driver = webdriver.Chrome(options=options)
    
    def login(self):
        """
        Logs into LinkedIn using the provided credentials.
        
        :return: Current URL after attempting login.
        """
        # Open LinkedIn's login page
        self.driver.get("https://www.linkedin.com/login")
        # time.sleep(2)  # Wait for the page to load
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "organic-div")))
        # Locate the email and password input fields
        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        
        # Fill in the login credentials
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        
        # Submit the form (simulate pressing 'Enter')
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)  # Allow time for login process
        
        return self.driver.current_url
    
    def post(self, content: str): 
        """
        Posts the given content on the user's LinkedIn feed.
        
        :param content: The text content to be posted.
        """
        # Click on the 'Start a post' button
        start_post_button = self.driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.dQcafCkQrDTgDAnkmIqDAVtYuNXxzBUlU")
        self.driver.execute_script("arguments[0].click();", start_post_button)

        # start_post_button.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "share-box")))

        # Locate the text area for typing the post content
        post_content_area = self.driver.find_element(By.CSS_SELECTOR, ".ql-editor.ql-blank")
        post_content_area.send_keys(content)

        # time.sleep(5)  # Wait for the content to be typed
        # Click on the 'Post' button
        post_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".share-actions__primary-action.artdeco-button.artdeco-button--2.artdeco-button--primary")))
        print("hi")
        self.driver.execute_script("arguments[0].click();", post_button)
        time.sleep(10)  # Allow time for the post to be shared



    def quit(self):
        """
        Closes the browser window.
        """
        self.driver.quit()


# Example usage:
if __name__ == '__main__':
    # Replace these with your actual LinkedIn credentials and the correct path to your ChromeDriver.
    user_email = "sayangolder2004@gmail.com"
    user_password = "amijabona@"
    chromedriver_path = "/path/to/chromedriver"  # Update with the actual path

    # Create an instance of the bot and log in
    linkedin_bot = LinkedInBot(user_email, user_password, chromedriver_path)
    current_page = linkedin_bot.login()
    linkedin_bot.post("Can you see this post? it is a post craeted by my bot")  # Post a message on the feed
    print("Login successful. Current page URL:", current_page)
    
    # When finished, close the browser
    linkedin_bot.quit()
