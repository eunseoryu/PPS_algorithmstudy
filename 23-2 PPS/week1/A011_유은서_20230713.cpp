#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;


vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<double> p;
    map<int, double> m;
    int total = 0, clear = 0;
    double percent;

    for(int i=0; i<N; i++) {
        total = 0;
        clear = 0;

        for(int j=0; j<stages.size(); j++) {
            if(stages[j] == i+1) {
                clear++;
            }
            if(stages[j] >= i+1) {
                total++;
            }
        }
        
        percent = (total == 0) ? 0 : (double)clear / total;
        m.insert(make_pair(i+1, percent));
        p.push_back(percent);
    }

    sort(p.begin(), p.end(), greater<double>());
    for(int i=0; i<N; i++) {
        for(auto it : m) {
            if(p[i] == it.second) {
                answer.push_back(it.first);
                m.erase(it.first);
                break;
            }
        }
    }

    return answer;
}
