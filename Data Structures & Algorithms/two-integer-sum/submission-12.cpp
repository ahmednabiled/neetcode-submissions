class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        for(int i=0; i<nums.size(); i++){
            int m = target - nums[i];
            
            if(seen.count(m)){
                return {seen[m], i};
            }

            seen[nums[i]] = i;
        }
    }
};
