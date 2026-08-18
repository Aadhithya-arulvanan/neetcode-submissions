#include<unordered_map>
#include<vector>
using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int>store;
        for(size_t i=0;i<nums.size();i++){
            if(store.find(nums[i])!=store.end()){
                return true;
            }
            store[nums[i]]=i;
            

        }
        return false;
    }
};