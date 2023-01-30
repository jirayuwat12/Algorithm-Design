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

int bs(const VI & l,int target){
    int li = 0;
    int ri = l.size()-1;
    while(li<=ri){
        int m = (li+ri)/2;
        if(l[m] > target) li = m+1;
        else ri = m-1;
    }
    return li==l.size()?-1:l[li];
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int n,m;
    cin>>n>>m;
    VI l(n);
    while(n--){
        cin>>l[n];
    }
    while(m--){
        int target;
        cin>>target;
        cout<<bs(l,target)<<'\n';
    }
    return 0;
}