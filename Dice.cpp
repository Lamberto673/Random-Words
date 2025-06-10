#include <iostream>
#include <ctime>
#include <iomanip>
#include<map>
#include<unordered_map>
#include <string>
#include <list>

int roll(std::map<int, std::string>&dice, int moves);

int main(){
    int moves;
    std::map<int, std::string>dice;
        dice[1] = R"(┌─────────┐
│         │
│    ●    │
│         │
└─────────┘)";

        dice[2] = R"(┌─────────┐
│ ●       │
│         │
│       ● │
└─────────┘)";

        dice[3] = R"(┌─────────┐
│ ●       │
│    ●    │
│       ● │
└─────────┘)";

        dice[4] = R"(┌─────────┐
│ ●     ● │
│         │
│ ●     ● │
└─────────┘)";

        dice[5] = R"(┌─────────┐
│ ●     ● │
│    ●    │
│ ●     ● │
└─────────┘)";

        dice[6] = R"(┌─────────┐
│ ●     ● │
│ ●     ● │
│ ●     ● │
└─────────┘)";
    

    std::cout << "How many moves: ";
    std::cin >> moves;
    
    roll(dice, moves);
    
    return 0;
}

int roll(std::map<int, std::string>&dice, int moves){
    std::srand(std::time(nullptr));
    std::list<int> results;

    int total = 0;

    for(int i = 0; i < moves;i++){
        int result = (std::rand() % 6) + 1;
        results.push_back(result);
        total += result;
    }

    int i = 1;
   
    for(const auto& face : results){
        std::cout << "Roll " << i++ << ":\n" << dice.at(face) << '\n';
    }
    std::cout << "Total: " << total << '\n';
   
    return total;
}