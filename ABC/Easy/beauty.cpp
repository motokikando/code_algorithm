#include <bits/stdc++.h>
using namespace std;

int main(){
    string w;
    string ans;
    char moji;
    int cnt;
    cin >> w;
    /* a to z */
    for(moji='a'; moji<='z'; ++moji)
        if(w.find(moji) != string::npos){
            cnt = count(w.begin(), w.end(), moji);
            if (cnt % 2 == 1){
                cout << "No" << endl;
                return 0;
            }
        }
    cout << "Yes" << endl;
    return 0;
}