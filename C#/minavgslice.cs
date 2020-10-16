//Find the minimal average of any slice containing at least two elements.
using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(new Solution().solution(new int[] 
            {4,2,2,3,4,1,2,3}));
        }
    }

    class Solution
    {
        public int solution(int[] A)
        {
            var B = new int[A.Length];

            for (int i = 1; i < A.Length; i++)
            {
                B[i] = A[i] + A[i - 1];
            }
            //4,6,4,7,6,6,13

            var pos = A.Length - 2;
            var min = (double)B[A.Length - 1] / 2;
            for (int i = A.Length - 1; i >= 1; --i)
            {
                var temp = (double)B[i] / 2;

                if (temp <= min)
                {
                    pos = i - 1;
                    min = temp;
                }
                temp = (double)(A[i] + B[i - 1]) / 3;
                if (i >= 2 && min >= temp)
                {
                    pos = i - 2;
                    min = temp;
                }
            }

            return pos;
        }
    }
}
