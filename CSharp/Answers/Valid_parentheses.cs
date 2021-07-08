//https://www.codewars.com/kata/52774a314c2333f0a7000688/train/csharp
//Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

// Examples
// "()"              =>  true
// ")(()))"          =>  false
// "("               =>  false
// "(())((()())())"  =>  true
// Constraints
// 0 <= input.length <= 100

// Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


// //BEST PRACTICES:
// public class Parentheses
// {
//     public static bool ValidParentheses(string input)
//     {
//         int parentheses = 0;
//         foreach (char t in input)
//         {
//             if (t == '(')
//             {
//                 parentheses++;
//             }
//             else if (t == ')')
//             {
//                 parentheses--;

//                 if (parentheses < 0)
//                 {
//                     return false;
//                 }
//             }
//         }

//         return parentheses == 0;
//     }
// }


// using System.Linq;
// public class Parentheses
// {
//   public static bool ValidParentheses(string input)
//   {
//     input = string.Concat(input.Where(x => "()".Contains(x)));
//     while (input.Contains("()"))
//     {
//       input = input.Replace("()", "");
//     }
    
//     return !input.Any();
//   }
// }


// public class Parentheses
// {
//     public static bool ValidParentheses(string input)
//     {
//       int numOpen = 0;
//       for(int i = 0; i < input.Length; i++){
//         if(input[i] == '(') numOpen++;
//         if(input[i] == ')') numOpen--;
//         if(numOpen < 0) return false;
//       }
//       return (numOpen == 0);
//     }
// }