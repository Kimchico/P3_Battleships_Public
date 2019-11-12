// Server side of networking text program

#define _OE_SOCKETS
#include <iostream>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <thread>
#include <sys/time.h>
#include <mutex>
#include <cstdint>

using namespace std;

int main(int argc, char *argv[]){
    int port = 1500;
    bool is_exit = false;
    char buffer[1024];
    int buff_size = (sizeof(buffer) / sizeof(*buffer));
    int client = socket(AF_INET, SOCK_STREAM, 0);
    bool server_running = true;
    int server;

    struct sockaddr_in server_address;
    socklen_t size;

    if(client < 0) {
        cout << "\nError making sockets, try reloading the program" << endl;
        exit(1);
    } else cout << "\nSocket established" << endl;


    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = htons(INADDR_ANY);
    server_address.sin_port = htons(port);
    
    
    if (::bind(client, (struct sockaddr*)&server_address, sizeof(server_address)) < 0) {
            cout << "\nError binding connection, the socket has already been established..." << endl;
            return -1;
    }
    

    size = sizeof(server_address);
    cout << "\nLooking for clients" << endl;

    listen(client, 1);
    
    server = accept(client, (struct sockaddr*)&server_address, &size);

    if(server < 0){
        cout << "\nError on accepting" << endl;
    }else cout << "\nConnected" << endl;
    
    do{
        recv(server, buffer, buff_size, 0);
        cout << "Client: " << buffer << endl;


        cin.getline(buffer, 1024);
        send(server, buffer, buff_size, 0);        
    }while(!is_exit);

    return 0;
}








