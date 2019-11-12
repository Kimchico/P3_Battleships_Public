#include <iostream>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>

using namespace std;    

int main(int argc, char *argv[]){
    int client;
    int portNum = 1500;
    bool isExit = false;
    char buffer[1024];
    int buff_size = (sizeof(buffer) / sizeof(*buffer));
    char* ip = "127.0.0.1";
    struct sockaddr_in server_address;

    client = socket(AF_INET, SOCK_STREAM, 0);

    if(client < 0){
        cout << "\nError establishing socket" << endl;
        exit(1);
    }

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(portNum);
    
    if (connect(client,(struct sockaddr *)&server_address, sizeof(server_address)) == 0)
        cout << "Connection to the server port number: " << portNum << endl;


    do{
        cin.getline(buffer, 1024);
        send(client, buffer, buff_size, 0);
        recv(client, buffer, buff_size, 0);
        cout << "Server: " << buffer << endl;

    } while(!isExit);
    
    return 0;
}
