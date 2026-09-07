class Solution(object):
    def maximum69Number (self, num):

        num_list = list(str(num))


        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break 

        ans = "".join(num_list)
        return int(ans)
            