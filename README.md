# Unsplash Image Search Application

This is a Flask-based web application that allows users to search for images from Unsplash using a keyword. The application fetches images from the Unsplash API and displays them dynamically on the webpage. Users can also copy the image link easily.

## Features
- Search for images using keywords
- Display the first image result
- Copy the image link with a single click
- Responsive and stylish UI with Bootstrap

## Technologies Used
- Flask (Python backend)
- HTML, CSS, Bootstrap (Frontend)
- jQuery (for AJAX requests)
- Unsplash API (for fetching images)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/unsplash-image-search.git
   cd unsplash-image-search
   ```
2. Install dependencies:
   ```bash
   pip install flask requests
   ```
3. Replace `your_unsplash_access_key` in `app.py` with your Unsplash API key.
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter a keyword in the search bar.
2. Click the "Search" button.
3. The first image result will be displayed.
4. Click the "Copy Link" button to copy the image URL.

## API Key Requirement
To use the Unsplash API, you need an API key. Sign up at [Unsplash Developers](https://unsplash.com/developers) to obtain one.

## License
This project is open-source and available under the MIT License.

## Contribution
Feel free to submit pull requests or report issues.
