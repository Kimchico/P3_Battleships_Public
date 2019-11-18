#include <iostream>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>
#include <thread>

using namespace std;    


void receive(int file_d, char buffer[]){
	char client_name[100];

    while(true){
        recv(file_d, client_name, (sizeof(client_name) / sizeof(*client_name)), 0);
        recv(file_d, buffer, 1024, 0);
	cout << client_name << " says:";
        cout << " " << buffer << "\n\n";
    }
}

int main(int argc, char *argv[]){
    int client;
    int port = 5000;
    bool isExit = false;
    char buffer[1024];
    char buffer_[1024];
    int buff_size = (sizeof(buffer) / sizeof(*buffer));
    struct sockaddr_in server_address;

    client = socket(AF_INET, SOCK_STREAM, 0);

    if(client < 0){
        cout << "\nError establishing socket" << endl;
        exit(1);
    }
    
    // server_address.sin_addr.s_addr is the ip address of the machine which the Server.cpp is running on.
    // Windows: use ipconfig in cmd and set the inet_addr to your IPv4.
    
    server_address.sin_addr.s_addr = inet_addr("172.24.216.58");
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(port);
    
    if (connect(client,(struct sockaddr *)&server_address, sizeof(server_address)) == 0)
        cout << "\nConnection to the server port number: " << port << endl;

    cout << "Please input your name: ";

    cin.getline(buffer, buff_size);
    send(client, buffer, buff_size, 0);
    cout << "\n\n";
    
    thread t1(receive, client, buffer_);
    t1.detach();

    do{

        cin.getline(buffer, buff_size);
        send(client, buffer, buff_size, 0);
	cout << "\n";

    } while(!isExit);

    
    return 0;
}
