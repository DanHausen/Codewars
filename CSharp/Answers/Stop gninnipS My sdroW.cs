//https://www.codewars.com/kata/5264d2b162488dc400000001/train/csharp

using System.Collections.Generic;
using System.Linq;
using System;

public class Kata
{
  public static string SpinWords(string sentence)
  {
    char[] tempArray = new char[]{};
    string[] words = sentence.Split(' ');
    for(int i = 0; i < words.Length;i++){
      if (words[i].Length >= 5){
        tempArray = words[i].ToCharArray();
        Array.Reverse(tempArray);
        words[i] = new String(tempArray);
      }
    }
    return string.Join(" ",words);
  }
}

//Smart Practices:
// using System.Collections.Generic;
// using System.Linq;
// using System;

// public class Kata
// {
//   public static string SpinWords(string sentence)
//   {
//     return String.Join(" ", sentence.Split(' ').Select(str => str.Length >= 5 ? new string(str.Reverse().ToArray()) : str));
//   }
// }


// using System.Linq;
// using System.Text.RegularExpressions;
// public class Kata
// {
//   public static string SpinWords(string sentence)
//   {
//     return Regex.Replace(sentence, @"\w{5,}", m => string.Concat(m.Value.Reverse()));
//   }
// }