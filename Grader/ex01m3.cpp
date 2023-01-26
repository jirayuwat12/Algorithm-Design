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

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int n,a;
    cin>>n>>a;
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>> q;
    VI t(n);
    REP(i,n) cin>>t[i];
    for(auto i : t){
        q.push({i,i});
    }
    int last_c = n;
    REP(i,a) {
        int c;
        cin>>c;
        if(c<=n) cout<<0;
        else{
            ll ans = -1;
            while(last_c <= c){
                auto temp = q.top();
                // cout<<temp.first<<' '<<temp.second<<' '<<last_c<<'\n';
                q.pop();
                ans = temp.first;
                temp.first +=  temp.second;
                q.push(temp);
                last_c++;
                // cout<<last_c<<'\n';
            }
            cout<<ans<<'\n';
        }
    }
    return 0;
}
/*
3 4
2 2 5
4 5 6 30

*/