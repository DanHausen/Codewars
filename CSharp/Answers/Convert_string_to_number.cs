//https://www.codewars.com/kata/544675c6f971f7399a000e79/train/csharp

// Description
// We need a function that can transform a string into a number. What ways of achieving this do you know?

// Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

using System;
  public class Kata
  {
    public static int StringToNumber(String str) {
        return Int32.Parse(str);
  }
}
  
  //BEST PRACTICES:
//   using System;
// public class Kata {
//   public static int StringToNumber(String str) => int.Parse(str);
// }

// using System;
//   public class Kata
//   {
//     public static int StringToNumber(String str) {
//          return (int.Parse(str));
//   }
// }