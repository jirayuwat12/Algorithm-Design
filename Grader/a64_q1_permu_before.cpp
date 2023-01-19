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

int c[21];

int find_pos(int n,int t){
    FOR(i,0,n){
        if(c[i] == t) return i;
    }
    return -1;
}

bool is_in_condition(int n,const VI & a,const VI & b){
    FOR(i,0,a.size()){
        int pos_a = find_pos(n,a[i]);
        int pos_b = find_pos(n,b[i]);
        // a is in before b
        if(pos_a != -1 && pos_b == -1 ) continue;
        // b is in before a
        if(pos_b != -1 && pos_a == -1) return false;
        // both not in
        if(pos_a == -1 && pos_b == -1) continue;
        // all in 
        if(pos_a >= pos_b) return false;
    }
    return true;
}

void make_all_per(int n,const VI & a,const VI & b,int idx = 0){
    if(idx == n){
        if(!is_in_condition(n,a,b)) return;
        FOR(i,0,n) cout<<c[i]<<' ';
        cout<<'\n';
    }else{
        // continue makeing process
        FOR(i,0,n){
            bool ck = true;
            FOR(j,0,idx) if(c[j] == i) ck = false;
            if(!ck || !is_in_condition(idx,a,b)) continue; 
            c[idx] = i;
            make_all_per(n,a,b,idx+1);
        }
    }
}
int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int n,m;
    cin>>n>>m;
    VI a(m),b(m);
    while(m--){
        cin>>a[m]>>b[m];
    }
    FOR(i,0,21) c[i]=0;
    make_all_per(n,a,b);
    return 0;
}