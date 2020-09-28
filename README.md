# chat-on-flask
Simple application for chatting on flask with socket io and postgres database.
This is just for template purpose.


## Explaination about the Libraries used
SocketIO library enables BiDirectional, Realtime and event based communication between the client and the server. Here it Consists of:
* flask-socketio
* javascript client side library

It working by trying to create a websocket connection, which provides full-duplex and low-latency channel between client and server, if possible or does HTTP longpolling if websocket connection is not connected.

### How does this program work?

#### When joined from the client side
When Client Side is opened it connects to the server through a websocket and creates a event called `joined_room` sending data such as username and room number with it. While using on another platform on connection the cilent should create this event with necessary data passed. When making a proper chatting application two usernames needs to be sent. When this event is created in backend serverside there is a event handler for this which is inside `socketio_on()` decorator. Function inside it gets the data sent from the client side and then processes it such as creating room for the users from the database, storing information who joined the database etc.

In the context of this small project, Roomid and user joined are added to the database and it is checked if that room is empty or not. If the room is empty, Serverside creates `join_room_announcement` event and if the room is not empty i.e. has chat history then it creates `rejoin_room` event and fetches all the chat history from the database and sends it to the client. The `join_room_announcement` event can be used as a trigger that the message was opened. In this project, it is used to show that a person is online for simplicity. The `rejoin_room` event takes all of the data send from the server side and then displays it in proper format. It can be used as normal history displaying with trigger that the message was opened. Here on this program, This event also updates the scroll so that it shows the bottom part i.e. the latest part of the message.


#### When sending messages