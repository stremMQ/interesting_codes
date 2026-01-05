#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <time.h>
#include <unistd.h>
#include <cstring>
using namespace std;

struct kart{
    char mast;
    unsigned short size_o;
    char krtm = 'E';
};

vector<kart> random_kal(vector<kart> x){
    random_device rd;
    default_random_engine rng(rd());
    shuffle(x.begin(), x.end(), rng);
    return x;
}

void mast_check(char a, char* ms){
    if (a == 'P'){
        strcpy(ms,"spades");
    }
    else if(a == 'K'){
        strcpy(ms,"clubs");
    }
    else if(a == 'B'){
        strcpy(ms,"diamonds");
    }
    else if(a == 'C'){
        strcpy(ms,"hearts");
    }
}

void check_kart(unsigned short b, char* krt, char m){
    const char numst[8][6] = {"two","three","four","five","six","seven","eight","nine"};
    if(b < 10){
        strcpy(krt, numst[b - 2]);
    }
    else if(b == 11){
        strcpy(krt,"ace");
    }
    else if(b == 10 && m == 'T'){
        strcpy(krt,"ten");
    }
    else if(b == 10 && m == 'W'){
        strcpy(krt,"jack");
    }
    else if(b == 10 && m == 'D'){
        strcpy(krt,"lady");
    }
    else if(b == 10 && m == 'K'){
        strcpy(krt,"king");
    }
}

void you_give(int *sum, char *krt, char *ms, vector<kart> &koloda){
    check_kart(koloda.front().size_o, krt, koloda.front().krtm);
    mast_check(koloda.front().mast, ms);

    cout << "You've been given - "<< krt << " "<< ms << endl;
    *sum += koloda.front().size_o;
    cout << "You score: " << *sum << endl;

    koloda.erase(koloda.begin());
    cout << "<-------------------------->" << endl;
    sleep(3);
}

void diler_give(int *suma, char *krt, char *ms, vector<kart> &koloda){
    check_kart(koloda.front().size_o, krt, koloda.front().krtm);
    mast_check(koloda.front().mast, ms);

    cout << "The dealer received - "<< krt << " "<< ms << endl;
    *suma += koloda.front().size_o;
    cout << "dealer score: " << *suma << endl;

    koloda.erase(koloda.begin());
    cout << "<-------------------------->" << endl;
    sleep(3);
}

int main(){
    char ms[10];
    char krt[10];
    char end;
    while(end != '/'){
        vector<kart> koloda;
        const char mst[4] = {'P', 'K', 'B', 'C'};
        for(unsigned short i = 2; i <= 14; i ++){
            for(unsigned short j = 0; j <= 3; j ++){
                if(i <= 9){
                    kart kr{mst[j], i};
                    koloda.push_back(kr);
                }
                else if(i == 10){
                    kart kr{mst[j], 10, 'T'};
                    koloda.push_back(kr);
                }
                else if(i == 11){
                    kart kr{mst[j], 10, 'W'};
                    koloda.push_back(kr);
                }
                else if(i == 12){
                    kart kr{mst[j], 10, 'D'};
                    koloda.push_back(kr);
                }
                else if(i == 13){
                    kart kr{mst[j], 10, 'K'};
                    koloda.push_back(kr);
                }
                else if(i == 14){
                    kart kr{mst[j], 11};
                    koloda.push_back(kr);
                }
            }
        }
        koloda = random_kal(koloda);
    // cout << koloda.size() << endl;
    // for(int h = 0; h < koloda.size(); h++){
    //     cout << koloda[h].mast << " | ";
    //     cout << koloda[h].size_o << endl; 
    // }
        char command;
        cout << "Start game - 's' \n end game '/' " << endl;
        cout << "input command > ";
        cin >> command;
        if(command == 's'){
            int sum_y = 0;
            int sum_d = 0;
            cout << "dealer distributes the cards:" << endl;
            sleep(3);

            you_give(&sum_y, krt, ms, koloda);

            diler_give(&sum_d, krt, ms, koloda);

            you_give(&sum_y, krt, ms, koloda);
            if(sum_y == 21){
                cout << "you 21 otchko!!!" << endl;
                cout << "You win!!!" << endl;
                continue;
            }
            diler_give(&sum_d, krt, ms, koloda);
            char cm = '/';
            while(cm != 'p'){
                cout << "give kart - 'g' \n pass - 'p'" << endl;
                cout << "input > ";
                cin >> cm;
                if(cm == 'g'){
                    you_give(&sum_y, krt, ms, koloda);
                }
                if(sum_y > 21){
                    cout << "Game Over" << endl;
                    cout << "Diler win!!!" << endl;
                    break;
                }
            }
            if(sum_y > 21){
                continue;
            }
            while(sum_d < sum_y){
                diler_give(&sum_d, krt, ms, koloda);
                if(sum_d > 21){
                    cout << "you 21 otchko!!!" << endl;
                    cout << "You win!!!" << endl;
                    break;
                }
            }
            if(sum_d > 21){
                continue;
            }
            if(sum_d > sum_y){
                cout << "Game Over" << endl;
                cout << "Diler win!!!" << endl;
                continue;
            }



        }
    }
}
