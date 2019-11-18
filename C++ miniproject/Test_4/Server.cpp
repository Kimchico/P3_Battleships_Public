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
#include <stdio.h>
#include <cstring>

using namespace std;

struct Data{
    char buffer[1024];
    int file_d;
    string name;
    int ID;

    Data(int n){
        this -> ID = n; 
    }

};


void receive(Data data, Data data_2, Data data_3){
	char client_name[100];
	strcpy(client_name, data.name.c_str());
	
	
    while(true){
        recv(data.file_d, data.buffer, (sizeof(data.buffer) / sizeof(*data.buffer)), 0);
	
	if(*data.buffer == '#'){
		// close program
	}

	//Send client name
	send(data_2.file_d, client_name, (sizeof(client_name) / sizeof(*client_name)), 0);
	send(data_3.file_d, client_name, (sizeof(client_name) / sizeof(*client_name)), 0);

	//send message
	send(data_2.file_d, data.buffer, (sizeof(data.buffer) / sizeof(*data.buffer)), 0);
        send(data_3.file_d, data.buffer, (sizeof(data.buffer) / sizeof(*data.buffer)), 0);
        cout << data.name << ": " << data.buffer << endl;
    }
}

int main(int argc, char *argv[]){
    int port = 5000;
    bool isExit = false;
    int buff_size = 1024;
    int master_socket  = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in server_address;
    socklen_t size;


    if(master_socket < 0) {
        cout << "\nError making sockets, try reloading the program" << endl;
        exit(1);
    } else cout << "\nSocket established" << endl;


    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = INADDR_ANY;
    server_address.sin_port = htons(port);
    

    
    if (::bind(master_socket, (struct sockaddr*)&server_address, sizeof(server_address)) < 0) {
            cout << "\nError binding connection, the socket has already been established..." << endl;
            close(master_socket);
            return -1;
    }
    
    cout << "\nLooking for clients" << endl;

    listen(master_socket, 3);
    
    //server = accept(master_socket, (struct sockaddr*)&server_address, &size);
    Data client_1(1), client_2(2), client_3(3);
    client_1.file_d = accept(master_socket, (struct sockaddr*)&server_address, &size);
    client_2.file_d = accept(master_socket, (struct sockaddr*)&server_address, &size);
    client_3.file_d = accept(master_socket, (struct sockaddr*)&server_address, &size);
    close(master_socket);

    if(client_1.file_d < 0 && client_2.file_d < 0 && client_3.file_d < 0){
        cout << "\nError on accepting" << endl;
        return -1;
    }else cout << "\nConnected" << endl;
    
    


    recv(client_1.file_d, client_1.buffer, (sizeof(client_1.buffer) / sizeof(*client_1.buffer)), 0);
    recv(client_2.file_d, client_2.buffer, (sizeof(client_2.buffer) / sizeof(*client_2.buffer)), 0);
    recv(client_3.file_d, client_3.buffer, (sizeof(client_3.buffer) / sizeof(*client_3.buffer)), 0);

    client_1.name = client_1.buffer;
    client_2.name = client_2.buffer;
    client_3.name = client_3.buffer;
    
    thread t1(receive, client_1, client_2, client_3);
    thread t2(receive, client_2, client_1, client_3);
    thread t3(receive, client_3, client_1, client_2);
    
    t1.join();
    t2.join();
    t3.join();

    
    close(client_1.file_d);
    close(client_2.file_d);
    close(client_2.file_d);
    return 0;
}








