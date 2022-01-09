#include <stack>
class Solution
{
public:
    bool isValid(string s)
    {
        int strSize = s.size();
        if (strSize % 2)
            return false;
        stack<char> stk;
        char top;
        for (int i = 0; i < strSize; i++)
        {
            if (stk.empty())
                stk.push(s[i]);
            else
            {
                top = stk.top();
                if ((top == '(' && s[i] == ')') || (top == '{' && s[i] == '}') || (top == '[' && s[i] == ']'))
                    stk.pop();
                else
                    stk.push(s[i]);
            }
        }

        return stk.empty();
    }
};