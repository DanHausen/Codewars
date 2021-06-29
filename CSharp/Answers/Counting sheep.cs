//https://www.codewars.com/kata/54edbc7200b811e956000556/train/csharp

using System;

public static class Kata
{
  public static int CountSheeps(bool[] sheeps)
  {
    int answer = 0;
    foreach(bool i in sheeps){
      if(i == true){
        answer++;
      }
    }
    return answer;
  }
}

//BEST PRACTICES:
// using System.Linq;
// class Kata
// {
//   public static int CountSheeps(bool[] sheeps) => sheeps.Count(s => s);
// }

// using System;
// using System.Linq;
// public static class Kata
// {
//   public static int CountSheeps(bool[] sheeps)
//   {
//     return sheeps.Count(s => s);
//   }
// }