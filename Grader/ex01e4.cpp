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

int calc(int x,int n,int k){
    if(pow(x,n) < INT_MAX){
        return ((int)pow(x,n) % k);
    }else{
        return (calc(x,floor(n/2),k) * calc(x,n-floor(n/2),k)) %k;
    }
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int x,n,k;
    cin>>x>>n>>k;
    cout<<calc(x,n,k);
    return 0;
}