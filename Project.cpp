#include<iostream>
#include<ctime>
#include<string>


void spin(std::string *pictures, int size);  
int Bet(int balances, int &bet);
int win(int balances, std::string *pictures);
int main(){
    int balances = 100;
    int bet;
    char quit;
    int winn;
    std::string pictures[3] = {"🍟", "🍔", "🍕"};
    int size = 3;

    do{
    std::cout << "**********************\n";
    std::cout << "Welcome to the casino!\n";
    std::cout << "🍟 🍔 🍕  \n";
    std::cout << "**********************\n";
    // std::cout << "How much money do you want to bet: ";
    // std::cin >> bet;
    std::cout << "Your balance is:$" << balances << '\n';
    balances =  Bet(balances, bet);
    balances -= bet;
    
    std::cout << "Spinning...\n";
    std::cout << "*********\n";
    spin(pictures, size);
    std::cout << "*********\n";
    winn = win(balances, pictures);
        balances += (winn - bet);
    if(winn > bet){
        std::cout << "Yea you won:$" << winn << '\n';
        std::cout << "Your balances:$" << balances << '\n';
    }else{
        std::cout << "You lost\n";
        std::cout << "Your balance:$ " << balances << '\n';
    }


    std::cout << "Press q to quit: ";
    std::cin >> quit;
    }while(quit != 'q');
    
    std::cout << "Thanks for playing!\n";

    return 0;
}
void spin(std::string *pictures, int size){
    srand(time(0));
    for(int i = 0; i < 3; i++){
        int random = rand() % size;
        std::cout << pictures[random] << ' ';
    }
    std::cout << '\n';
}
// int balance(int balances){
//     return balances;
// }
int Bet(int balances, int &bet){
    std::cout << "How much money do you want to bet:$";
    std::cin >> bet;
    if(bet > balances){
        std::cout << "Invalid bet\n";
        bet = 0;
    }
    return balances;
}
int win(int balances, std::string *pictures){
    int result = 0;
    if(pictures[0] == pictures[1] && pictures[1] == pictures[2]){
        if(pictures[0] == "🍟"){
            result =  100;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍔"){
            result =  150;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍕"){
            result = 200;
            std::cout << "You won!: " << result << '\n';
        }
        return result;
    }
    else if(pictures[0] == pictures[1]){
        if(pictures[0] == "🍟"){
            result =  50;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍔"){
            result =  75;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍕"){
            result = 100;
            std::cout << "You won!: " << result << '\n';
        }
        return result;
    }
    else if(pictures[0] == pictures[2]){
        if(pictures[0] == "🍟"){
            result =  25;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍔"){
            result =  30;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[0] == "🍕"){
            result = 50;
            std::cout << "You won!: " << result << '\n';
        }
        return result;
    }
    else if(pictures[1] == pictures[2]){
        if(pictures[1] == "🍟"){
            result =  25;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[1] == "🍔"){
            result =  35;
            std::cout << "You won!: " << result << '\n';
        }
        else if(pictures[1] == "🍕"){
            result = 45;
            std::cout << "You won!: " << result << '\n';
        }
        return result;
    }
    return result;
}