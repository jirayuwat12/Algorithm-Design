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


bool is_virus(string str,bool is_left = false){
    // can reverse or not
    if(is_left){
        if(str.size()==2 && (str == "01" || str == "10") ) return true;
        else if(str.size() == 2) return false;
        else{
            // case 1 not reverse
            int mid = str.size()/2;
            string left = str.substr(0,mid);
            string right = str.substr(mid,mid);
            bool not_reverse =  is_virus(left,true) && is_virus(right,false);
            // case 2 reverse
            reverse(str.begin(),str.end());
            mid = str.size()/2;
            left = str.substr(0,mid);
            right = str.substr(mid,mid);
            bool reverse =  is_virus(left,true) && is_virus(right,false);
            return not_reverse || reverse;
        }
    }else{ // cannot reverse
        if(str.size()==2 && str == "01") return true;
        else if(str.size() == 2) return false;
        else{
            int mid = str.size()/2;
            string left = str.substr(0,mid);
            string right = str.substr(mid,mid);
            return is_virus(left,true) && is_virus(right,false);
        }
    }
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
        cout<<(is_virus(str)?"yes" :"no")<<'\n';
    }    
    return 0;
}