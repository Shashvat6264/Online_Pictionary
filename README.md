# Online_Pictionary [WIP]
A web platform to play pictionary online with friends
NOTICE - FRAMEWORK IS FLASK NOW.

## Components
1. Chat Room - Flask_SocketIO 
2. Scribble Pad 

## Authentication
ML Based authentication against alphabets

## Work done
1. Made a Paint app
2. Made a Flask framework for a chat room
3. Create Rooms according to Room IDs
4. Make the Paint app in the Flask Chat Room Real-time using Flask and JQuery i.e. Make the Scribble Pad such that it emits the drawn pad to all connected clients.

## Work to be done 
1. Make a nice FrontEnd
2. Implement the ML Algo
3. Authenticate a Person's ID
4. Create a framework to create new rooms.
5. Create a ScoreBoard.
6. Integrate the game loop as in loop through all clients to appoint drawer and watchers and end the round according to either time or the correct answer by detecting the keyword. 
7. Disable editing chat room and Enable editing sketch pad for Drawer and vice versa for the watchers.
8. Assign a Keyword to the decided Drawer.

## How to use it right now
1. The folder chat app contains the integrated project so far. 
2. Run the main.py by 
```bash
python main.py
```
3. Go to your browser and enter the URL http://127.0.0.1:5000/
