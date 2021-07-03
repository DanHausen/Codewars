//ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
//Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
//https://www.codewars.com/kata/530e15517bc88ac656000716/train/csharp

public class Kata
{
  public static string Rot13(string message)
  {
    char[] array = message.ToCharArray();
    for(int i = 0;i<array.Length;i++){
      int number = (int)array[i];
      if(number >= 'a' && number <= 'z'){
        if(number > 'm') number -= 13;
        else number += 13;        
      }
      else if(number >= 'A' && number <= 'Z'){
        if(number > 'M') number -= 13;
        else number += 13;
      }
      array[i]=(char)number;
    }
    return new string(array);
  }
}

//BEST PRACTICES:
// using System;
// using System.Linq;
// public class Kata
// {
//   public static string Rot13(string message)
//   {
//      return String.Join("", message.Select(x => char.IsLetter(x) ? (x >= 65 && x <= 77) || (x >= 97 && x <= 109) ? (char)(x + 13) : (char)(x - 13) : x));
//   }
// }

// using System;
// public class Kata
// {
//   public static string Rot13(string message)
//   {
//     string result = "";
//             foreach (var s in message)
//             {
//                 if ((s >= 'a' && s <= 'm') || (s >= 'A' && s <= 'M'))
//                     result += Convert.ToChar((s + 13)).ToString();
//                 else if ((s >= 'n' && s <= 'z') || (s >= 'N' && s <= 'Z'))
//                     result += Convert.ToChar((s - 13)).ToString();
//                 else result += s;
//             }
//             return result;
//   }
// }