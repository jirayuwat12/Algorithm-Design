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

void gen(vector<VI> &m,int a,int b,int posx,int posy,int size){
    if(a==0){
        m[posy][posx] = b;
    }else{
        int new_size = size/2;
        gen(m,a-1,b  ,posx         ,posy         ,new_size);
        gen(m,a-1,b+1,posx         ,posy+new_size,new_size);
        gen(m,a-1,b-1,posx+new_size,posy         ,new_size);
        gen(m,a-1,b  ,posx+new_size,posy+new_size,new_size);
    }
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int a,b;
    cin>>a>>b;
    vector<vector<int>> m(pow(2,a),VI(pow(2,a)));
    gen(m,a,b,0,0,pow(2,a));
    for(auto i : m){
        for(auto j : i ) cout<<j<<' ';
        cout<<'\n';
    }
    return 0;
}