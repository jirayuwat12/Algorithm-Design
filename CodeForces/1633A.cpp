// Brute force : accepted
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

int count_dif_digit(int a,int b){
    int dif = 0;
    while(a > 0 && b > 0) {
        if(a%10 != b%10) dif ++;
        a/=10;
        b/=10;
    }
    while(a>0) dif++,a/=10;
    while(b>0) dif++,b/=10;
    return dif;
}

int solve(int n){
    int start = n;
    int m = 1;
    while(start > 10) start /= 10,m*=10;
    start *= m;
    int digit_count = 100000;
    int ret = 0;
    while(start <1000){
        if(count_dif_digit(start,n) < digit_count && start %7==0) {
            digit_count = count_dif_digit(start,n);
            ret = start;
        }
        start ++; 
    }
    return ret;
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        cout<<solve(n)<<'\n';
    }
    return 0;
}