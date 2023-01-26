// 100 
#include<bits/stdc++.h>
#define FOR(i,s,n) for(int i=s;i<n;i++)
#define FORR(i,s,n) for(int i=n-1;i>=s;i--)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(i,t) for(__typeof(t.begin()) i=t.begin();i!=t.end();i++)
#define PB push_back
#define MP make_pair
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x)*(x))
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VLL vector<long long>
#define SII set<int>
#define MII map<int,int>
#define SI2 set<pair<int,int> >
#define SI3 set<tuple<int,int,int> >
#define MII map<int,int>
#define MIII map<int,map<int,int> >
#define MSS map<string,string>
#define MIS map<int,string>
using namespace std;

bool is_virus(string str){

    if(str.size() == 2) return true;

    string left = str.substr(0,str.size()/2);
    string right = str.substr(str.size()/2,str.size()/2);

    int left_1 = 0;
    int right_1 = 0;

    REP(i,left.size()) if(left[i] == '1') left_1++;
    REP(i,right.size()) if(right[i] == '1') right_1++;

    if(abs(left_1 - right_1) > 1) return false;
    else return is_virus(left) && is_virus(right);
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int t,s;
    cin>>t>>s;
    while(t--){
        string str = "";
        FOR(i,0,pow(2,s)) {
            string tmp = "";
            cin>>tmp;
            str += tmp;
        }
        cout<<(is_virus(str)?"yes" :"no")<<endl;
    } 
    return 0;
}