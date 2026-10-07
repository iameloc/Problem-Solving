#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x, aux; cin >> n;
    vector <int> par;
    vector <int> impar;

    if(n<4 and n>1){
        cout << "NO SOLUTION" << '\n';
    }
    else{
        for(int i = 1; i<=n; i++){
            if(i%2==0){
                par.push_back(i);
            }
            else{
                impar.push_back(i);
            }
        }

        for(int i = 0; i<par.size(); i++){
            cout << par[i] << " ";
        }

        for(int i = 0; i<impar.size()-1; i++){
            cout << impar[i] << " ";
        }

        cout << impar[impar.size()-1] << '\n';
    }
}