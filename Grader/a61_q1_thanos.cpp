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
int h = 1;
int f(const VI & a, int l, int r, int A,int B){
    int la = lower_bound(a.begin(),a.end(),l) - a.begin();
    if(la-1 >= 0 && a[la-1] == l) la--;
    int ra = lower_bound(a.begin(),a.end(),r) - a.begin();
    int num_hero = ra-la;
    // no partail
    int min_power = A;
    if(num_hero) min_power = B * num_hero * (r-l+1);
    cout<<l<<' '<<r<<" no part : "<<min_power<<' ';
    // partial
    if(l!=r){
        int lans = f(a,l,(l+r)/2,A,B);
        int rans = f(a,(l+r)/2+1,r,A,B);
        cout<<"partial : "<<lans+rans;
        min_power = min(min_power,lans+rans);
    }
    cout<<endl;
    return min_power; 
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int p,k,A,B;
    cin>>p>>k>>A>>B;
    VI a(k);
    while(k--) cin>>a[k];
    sort(a.begin(),a.end());

    int l = 1;
    int r = 1<<p;

    cout<<f(a,l,r,A,B);

    return 0;
}