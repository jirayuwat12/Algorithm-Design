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

ll findQueue(ll t, VI &T){
    ll q = 0;
    REP(i,SZ(T))q+=t/T[i]+1;
    return q;
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int n,a;
    cin>>n>>a;
    VI T(n);
    REP(i,n)cin>>T[i];
    REP(i,a){
        ll q;
        cin>>q;
        // use binary search to find the least time t that serve q dishes
        ll l = 0, r = 1e18;
        while(l<r){
            ll m = (l+r)/2;
            if(findQueue(m,T)<q)l=m+1;
            else r=m;
        }
        cout<<l<<endl;

    }
    return 0;
}