# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

   #The purpose of the game was just for a simple guessing game that users could enjoy. It also served as a baseline to introduce us to using AI agents to help fix broken code. Initially, one of the bugs I first saw was that the difficulty levels had 0 correlation with how hard the guessing game was. The new game button didn't work and the hint button had absolutely zero correlation with where the actual number was at. I fixed all three of those bugs and had the difficulty numbers aligned with where I think they would be. 



## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Selected hard mode, 100 different numbers and only 5 guesses available
2. User submits guess of 54, number is too low and within 24 numbers of correct answer
3. User submits guess of 67, number is too low
4. User submits guess of 74, guess was correct!
5. Game ends and there is an option to start a new game. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

#For my enhanced UI features, I added cold and hot emojis to let you know how close you were to the correct answer. Double cold meant you were 50 or more numbers away, cold meant you were 25 or more numbers away, fire meant you were 24 or less away, and double fire meant you were 13 or less away. 