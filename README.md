# same-network-group-chat
GUI group chat for computers in the same network. Multiple clients can be created on a single computer. After starting the server. Clients can connect to the server. Clients connected to a server will be able to send broadcast messages to other clients connected to that server. Both the server program and client program are GUI based.

## Dependencies
* Python 3
* PyQt5 :- Install by running `pip3 install PyQt5` in a terminal or command prompt.

## Starting the group chat
* Server
1. Start the server by running `python3 server_app.py` in a terminal or command prompt.
2. Leave the fields in the server program empty to use default configurations.
3. Click **Start server** button.
* Client
1. Create a client by running `python3 client_app.py` in a terminal or command prompt.
2. In the client program enter a nickname to be seen by other clients when you send messages.
3. If the client programs will be running on the same machine as the server, leave the hostname field blank othereise enter the IP address of tge computer running the server.
4. Leave other fields blank if you didn't enter a port number in the server program.
5. Click **Connect to server** button.

Perform the steps to start the client multiple times to create multiple clients.

> In theory, the code should work on all platforms. The code has not been tested with MacOS.

## First run of server_app.py
![server_first_run](https://user-images.githubusercontent.com/24194821/40889048-acd656e6-6725-11e8-938a-c9a1d8417000.png)

## First run of client_app.py
![client_first_run](https://user-images.githubusercontent.com/24194821/40889053-b4c77a1a-6725-11e8-9f3c-eea9237e22f0.png)

## Client about to connect
![client_about_to_connect](https://user-images.githubusercontent.com/24194821/40889052-b4a938d4-6725-11e8-9fff-792fabbe0815.png)

## One client connected
![one_user_connected](https://user-images.githubusercontent.com/24194821/40889055-b4fdb13e-6725-11e8-8b00-6ac51429c987.png)

## Multiple clients connected
![multiple_users_connected](https://user-images.githubusercontent.com/24194821/40889054-b4e388b8-6725-11e8-8107-39fb7580fa2c.png)
