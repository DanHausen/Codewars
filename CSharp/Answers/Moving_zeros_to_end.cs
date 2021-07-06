//Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
//Kata.MoveZeroes(new int[] {1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) => new int[] {1, 2, 1, 1, 3, 1, 0, 0, 0, 0}

using System.Collections.Generic;

public class Kata
{
  public static int[] MoveZeroes(int[] arr)
  {
    List<int> list = new List<int>();
    int zeros = 0;
    for(int i = 0; i < arr.Length; i++){
      if(arr[i] != 0){
        list.Add(arr[i]);
      }
      else{
        zeros++;
      }
    }
    for(int i = 0; i < zeros; i++){
      list.Add(0);
    }
    arr = list.ToArray();
    return arr;
  }
}

//BEST PRACTICES:

// using System.Linq;
// public class Kata
// {
//   public static int[] MoveZeroes(int[] arr)
//   {
//      return arr.OrderBy(x => x==0).ToArray();
//   }
// }


// using System.Linq;
// public class Kata
// {
//   public static int[] MoveZeroes(int[] arr) => arr.OrderBy(o => o == 0).ToArray();
// }


// using System.Collections.Generic;
// public class Kata
// {
//   public static int[] MoveZeroes(int[] arr)
//   {
//     var ret = new int[arr.Length];
//     var index = 0;    
//     foreach (var item in arr)
//     {
//       if (item == 0) continue;
//       ret[index] = item;
//       index++;
//     }
//     return ret;
//   }
// }