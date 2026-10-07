#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    ll n, x, c = 0; cin >> n;
    vector<ll> array;

    for(ll i = 0; i<n; i++){
        cin >> x;
        array.push_back(x);
    }

//3 2 5 1 7

    for(ll i = 0; i<n-1; i++){
        if(array[i]>array[i+1]){
            c += array[i] - array[i+1];
            array[i+1] += array[i] - array[i+1];
        }
    }

    cout << c << '\n';

}