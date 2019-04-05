#include <iostream>
#include <map>
#include<vector>
#include<unordered_map>

using namespace std;
 vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash_map;
        int size=nums.size();
        vector<int> result;
        for (int i=0;i<size;i++){
             hash_map.insert(make_pair(nums[i],i));
        }
        int tmp = 0;

        for(int i = 0;i<size;i++){
            tmp =target-nums[i];
            if(hash_map.find(tmp)!=hash_map.end()){
                if(hash_map[tmp]!=i){
                    result.push_back(i);
                    result.push_back(hash_map[tmp]);
                    return result;
                    
                                    } 
                                                    }                 
                                }
    
    }

int main(){
    int iarr[] = {3,2,3};
    vector<int> nums(iarr,iarr+3); 
    int target = 6;

    unordered_map<int, int> hash_map;
    int size=nums.size();

    cout<<twoSum(nums,target)[0]<<" "<<twoSum(nums,target)[1];

    return 0;
}