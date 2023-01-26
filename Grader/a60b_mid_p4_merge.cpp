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

template<typename T1>
bool is_sort(T1 b,T1 e){
    int l = *b;
    b++;
    while(b != e){
        if(*b < l) return false;
        b++;
    }
    return true;
}

int merge_count(const VI & t ,int l,int r ){
    if (l != r-1 && !is_sort(t.begin()+l,t.begin()+r)){
        return 1 + merge_count(t,l,(l+r)/2) + merge_count(t,(l+r)/2,r);
    }else return 1;
}

int main(){
    std::ios_base::sync_with_stdio(false); std::cin.tie(0); 
    int n,k;
    cin>>n>>k;
    if(k > n*log(n) || k % 2 == 0){
        cout<<-1;
    }else{
        VI t(n);
        REP(i,n) t[i] =i+1;
        int temp = int(k / 2);
        do{
            if(temp -- ) continue;
            if(merge_count(t,0,t.size()) == k){
                REP(i,t.size()) cout<<t[i]<<' ';
                return 0;
            }
        }while(next_permutation(t.begin(),t.end()));
        cout<<-1;
    }
    return 0;
}

/*
1 2 -> 1
2 1 -> 3

1 2 3 -> 1
2 1 3 -> 3
2 3 1 -> 5

1 2 3 4 -> 1
2 1 3 4 -> 3
2 3 1 4 -> 3
2 3 4 1 -> 5

1 2 3 4 5 -> 1
2 1 3 4 5 -> 3
2 3 1 4 5 -> 5
2 3 4 1 5 -> 5
2 3 4 5 1 -> 7

1 2 3 4 5 6 -> 1
2 1 3 4 5 6 -> 5
2 3 1 4 5 6 -> 5

*/