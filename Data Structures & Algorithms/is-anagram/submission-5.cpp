class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> freq_s(28, 0);
        vector<int> freq_t(28, 0);

        if(s.size() != t.size()) return false;
        for(int i=0; i < s.size(); i++){
            freq_s[s[i] - 'a'] += 1; 
            freq_t[t[i] - 'a'] += 1; 
        }

        for(int i=0; i < 28; i++){
            if(freq_s[i] != freq_t[i]){
                return false;
            }
        }
        return true;
    }
};
