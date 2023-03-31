# URL Authentication Status Checker

This application is a Flask web app that checks the HTTP status and response time of a list of URLs provided in a text file. The app uses HTTP Basic Authentication with a username and password that are provided as environment variables.

## Requirements

- Docker

## Setup

1. Clone this repository to your local machine:



git clone https://github.com/yourusername/url-authentication-status.git
cd url-authentication-status


Make sure to replace `yourusername` with your actual GitHub username.

2. Create a `urls.txt` file in the project root directory and add the URLs you want to check, one per line:


3. Build the Docker image:

docker build -t url-authentication-status .



4. Run the Docker container:



docker run -p 5000:5000 -e USERNAME='xxxxxxxxxx' -e PASSWORD='xxxxxxxxxxx' url_auth_status


Replace `your_username` and `your_password` with the actual username and password.

5. Open your web browser and navigate to `http://localhost:5000` to view the URL authentication status.

## License

This project is licensed under the MIT License.




this README provides instructions for setting up and running the project. Make sure to replace yourusername with your actual GitHub username, and add any additional information you find necessary.