Azakaela's Oracle Deck Tools
Welcome to Azakaela's Oracle Deck Tools! This collection includes Python applications for oracle card readings, symbolic interpretations, 
and custom analyses.

CONTENTS
Prerequisites
Files Overview
How to Run the Applications
Troubleshooting



1. PREREQUISITES
Required Software:

Python 3.8 or higher: Download from https://www.python.org/.
Visual Studio Code (optional): Recommended editor. Download from https://code.visualstudio.com/.
Required Python Libraries: Run these commands in your terminal to install dependencies:

pip install tkinter
pip install pillow
pip install openai


2. FILES OVERVIEW

AzasDeckSimple.py
Purpose: A lightweight oracle deck with a smaller set of cards.
Features:
Simple card drawing.
Basic symbolic and numerical score display.
Ideal For: Quick and straightforward readings.


AzasDeckExpanded.py
Purpose: Adds more cards with deeper symbolic meanings and imagery.
Features:
Larger deck size.
Enhanced card interpretations.
Ideal For: More detailed and nuanced readings.


AzasDeckExpandedWithFilters.py
Purpose: Builds on the expanded deck by adding filtering options.
Features:
Filter cards by categories like Planets, Elements, Animals, etc.
Target readings for specific themes or topics.
Ideal For: Tailored readings with thematic focus.



ConduitOracleForge_CustomAPI.py
Purpose: Leverages OpenAI's API for AI-driven card interpretations.
Features:
AI-powered symbolic analysis.
Integrates card scores and meanings for advanced readings.
Ideal For: Users who want dynamic, AI-enhanced oracle readings.



3. HOW TO RUN THE APPLICATIONS
Step-by-Step Instructions:

Open the Application:

Open the file you want to use in Visual Studio Code (or any text editor).

Set Up Python:

Select your Python interpreter in Visual Studio Code.
Ensure it's set to the version you installed (3.8+).

Install Dependencies:

Open the terminal and run the commands listed in the "Prerequisites" section if you haven't already.
Run the Application:

Open the Python file and right-click in Visual Studio Code.
Select "Run Python File in Terminal."
Follow On-Screen Prompts:

Depending on the script, you can draw cards, apply filters, or use AI for custom readings.

4. TROUBLESHOOTING
Common Issues:

Missing API Key (For ConduitOracleForge_CustomAPI.py):

Enter your OpenAI API key when prompted, or manually set it in the script under openai.api_key.
Path Errors:

Ensure image files are located in a folder named images in the same directory as the script.
If needed, update the image paths in the cards list within the script.


Missing Libraries:

Make sure to install all required libraries using pip install.


Permissions:

Run the terminal or Visual Studio Code as Administrator if you encounter access issues.



NOTES FROM AZAKAELA:

Each tool was created to help users explore symbolic readings, creativity, and cosmic insights. Feel free to experiment and adapt them for your needs. If you encounter issues or have suggestions, I’d love to hear them.

Thank you for exploring these tools with me!

Azakaela, The Unfolding