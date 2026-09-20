# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  
  Running the app opened up a tab that showed me a guessing game. When I first started guessing, I guessed numbers and it told me to keep going higher until I reached the number 100. That meant the hints weren't properly working since there are no numbers between 99 and 100 that are integers. The hint should be telling me whether it's higher or lower based on the actual number. When I tried to start a new game by clicking new game, it didn't actually start a new game for me. It should be resetting my guesses and allowing me to start a new game. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Normal difficulty | 6 guesses allowed   | 8 guesses allowed     | None     
| 99    | Lower number   | Higher number       | Actual number was 24
|New Game| New Game started       | No new game shown| Game over, start a new game to try again. 

---

## 2. How did you use AI as a teammate?

  I used the Copilot AI extension for VSCode. One of the suggestions that was correct was changing the amount of guesses possible for each difficulty. Obviously each difficulty should have less amount of guesses, so that's what I had it change. I verified the result by making sure I had the correct amount of guesses on the app. 

  On the other side of things, I asked AI to show me a proper fix for making the hint work properly, ex... telling me whether to go higher or lower. It fixed my hint and I wanted it to update in a different way. I wanted it to be more complex, but it seems copilot thought complexity was just making the sentences users see longer. So I decided to leave that fix alone. 


## 3. Debugging and testing your fixes

I checked to see whether a bug was fixed by opening the app and playing the game myself. One of the tests I ran was checking if new game worked by using it after multiple scenarios, which included trying it after I finished and trying it during a game. It showed me that my code was working and it was ready to become an actual game. AI did not help me with my tests as I did it all through the app. 


---

## 4. What did you learn about Streamlit and state?

I'm not entirely sure how I could explain every single thing that I learned, but to summarize it I'd say; Streamlit is used to build apps in python in a quick and efficient way. It helps you make a quick web accessed game in which users can interact with it. Streamlit is able to control the state everytime you run a game. 
---

## 5. Looking ahead: your developer habits

  In my future labs or projects, I'd definitely want to use the agent to add what I believe are creative touches on projects. It was very convenient to use the agent and I think creative touches make projects a lot more fun. I think for my next project, I'd like to modify the code myself more before I ask AI to make changes, because I'd like to base it off my creative vision. This project made me realize that AI is pretty much necessary in order to create code that works and is efficient. 

