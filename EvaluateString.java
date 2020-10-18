package practice_dinesh;

import java.util.Stack;

public class EvaluateString
{
    public static int evaluate(String expression)
    {
        char[] express_char = expression.toCharArray();

         // I used this stack for numbers: 'stack_value'
        Stack<Integer> stack_value = new Stack<Integer>();

        // I used this stack for Operators: 'stack_ops'
        Stack<Character> stack_ops = new Stack<Character>();

        for (int i = 0; i < express_char.length; i++)
        {
             // If Current token is a whitespace,We will skip it
            if (express_char[i] == ' ')
                continue;

            // If Current token is a number, push it to stack for numbers
            if (express_char[i] >= '0' && express_char[i] <= '9')
            {
                StringBuffer buffer = new StringBuffer();
                // We know that, There may be more than one digits in number
                while (i < express_char.length && express_char[i] >= '0' && express_char[i] <= '9')
                    buffer.append(express_char[i++]);
                stack_value.push(Integer.parseInt(buffer.toString()));
            }

            // If Current token is an opening brace, push it to 'stack_ops'
            else if (express_char[i] == '(')
                stack_ops.push(express_char[i]);

            // If Closing brace encountered, solve entire brace
            else if (express_char[i] == ')')
            {
                while (stack_ops.peek() != '(')
                  stack_value.push(applyOp(stack_ops.pop(), stack_value.pop(), stack_value.pop()));
                stack_ops.pop();
            }

            // If Current token is an operator.
            else if (express_char[i] == '+' || express_char[i] == '-' ||
                     express_char[i] == '*' || express_char[i] == '/')
            {
                // While top of 'stack_ops' has same or greater precedence to current
                // token, which is an operator. Apply operator on top of 'stack_ops'
                // to top two elements in stack_value stack
                while (!stack_ops.empty() && hasPrecedence(express_char[i], stack_ops.peek()))
                  stack_value.push(applyOp(stack_ops.pop(), stack_value.pop(), stack_value.pop()));

                // We will Push current token to 'stack_ops'.
                stack_ops.push(express_char[i]);
            }
        }

        // Entire expression has been parsed at this point, apply remaining
        // stack_ops to remaining stack_value
        while (!stack_ops.empty())
            stack_value.push(applyOp(stack_ops.pop(), stack_value.pop(), stack_value.pop()));

        // Top of 'stack_value' contains result, return it
        return stack_value.pop();
    }

    // It will Returns true if 'op2' has higher or same precedence as 'op1',
    // otherwise returns false.
    public static boolean hasPrecedence(char op1, char op2)
    {
        if (op2 == '(' || op2 == ')')
            return false;
        if ((op1 == '*' || op1 == '/') && (op2 == '+' || op2 == '-'))
            return false;
        else
            return true;
    }

    // A utility method to apply an operator 'op' on operands 'a' 
    // and 'b'. Return the result.
    public static int applyOp(char op, int b, int a)
    {
        switch (op)
        {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0)
                throw new
                UnsupportedOperationException("Cannot divide by zero");
            return a / b;
        }
        return 0;
    }

    // Driver method to test above methods
    public static void main(String[] args)
    {
    	System.out.print("The output of the given expression is: ");
        System.out.println(EvaluateString.evaluate("2+(5*(2-2)))"));
    }
}