#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n, ans, sum, nsum = 0, x; cin >> n;
    sum = n*(n+1)/2;
    for(int i = 1; i<n; i++){
        cin >> x;
        nsum += x;
    }
    ans = sum - nsum;
    cout << ans << '\n';
}
