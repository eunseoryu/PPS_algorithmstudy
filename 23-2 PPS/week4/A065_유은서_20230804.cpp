//beakjoon 좌표 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	int n;
	int X, Y;
	vector<pair<int, int>> v;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> X >> Y;
		v.push_back({ X,Y });

	}
	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) {
		cout << v[i].first << " " << v[i].second <<"\n";
	}




	return 0;
}