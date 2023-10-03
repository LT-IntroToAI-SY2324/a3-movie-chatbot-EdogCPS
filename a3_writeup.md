# Assignment 3 - Writeup

Assignment 3 is all about creating this natural language query system.  In order to do so, you have to write a lot of functions to retrieve infomation.  You will also have to write a function to return answers from a pattern-action list.  There is a lot of work to accomplish in this assignment, but this portion is intended for you to write about what you accomplished.

## Reflection Questions
1. In your own words describe the `search_pa_list` function.
    The search_pa_list function takes a string, and compares it to the chosen sentance structures, if nothing fit it returns ["I dont understand"]. If it does find a fitting stucture but does not produce an answer, it returns ["No answers"], and it it finds an answer, it return those answers in a list. 

2. What movie did you add to the `movies.py` file?  What year was it made? Any specific reason you added that movie?
    Interstellar. 2014. I chose this movie becasue it is a really good movie that I enjoy, that I new was not already in the movies list.


3. What pattern / action did you add to the pa_list data structure?  Why do you think that is a useful pattern / action?
    I added a different structure of the get actor action. I think this is a usefull adddition to the pa_list varaible becasue the get title by actor prompt, I thought, was strangly worded.


4. What is chatbot would you create that would be like this?  Describe why you would create it and what it would do.
    I would do a "Find a study" chatbot. It would have a database of like jstor or google scholar and then it would search all these databases for anyhting relating to your topic or who wrote a publication, or the year, or any related publications. 


5. What was the most difficult portion of this assignment?
    The match function was the most dificult part of the movie chatbot. In this piece, the search_pa_list was the hardest becuase it has the most levels of complexity for this assighnment.


6. Did you write a new assert for your pattern action?



