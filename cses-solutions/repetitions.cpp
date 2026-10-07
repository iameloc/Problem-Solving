#include <bits/stdc++.h>
using namespace std;

int main(){
    string x; cin >> x;
    int c = 1;
    vector<int> tam;

    for(int i = 0; i < x.length() - 1; i++){
        if(x[i] == x[i+1]){
            c++;
        }
        else{
            tam.push_back(c);
            c = 1;
        }
    }
    tam.push_back(c);

    int maior = tam[0];
    for(int i = 0; i < tam.size(); i++){
        if(tam[i] > maior){
            maior = tam[i];
        }
    }

    cout << maior << '\n';
}