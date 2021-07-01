//https://www.codewars.com/kata/5601409514fc93442500010b/train/csharp

public class Kata
{
  public static bool BetterThanAverage(int[] ClassPoints, int YourPoints)
  {
    int sum = 0;
    int media = 0;
    for(int i = 0; i<ClassPoints.Length;i++){
      sum += ClassPoints[i];
    }
    media = (sum + YourPoints) / ClassPoints.Length;
    if(media <= YourPoints){
      return true;
    }
    else{
      return false;
    }
  }
}

//Smart practices:
// using System.Linq;
// public class Kata
// {
//   public static bool BetterThanAverage(int[] ClassPoints, int YourPoints)
//   {
//     return YourPoints > ClassPoints.Average();
//   }
// }

// using System;
// public class Kata
// {
//   public static bool BetterThanAverage(int[] ClassPoints, int YourPoints)
//   {
//      // calculate average points
//       int sum = 0; 
//       foreach (var point in ClassPoints)
//       {
//         sum += point;
//       }
      
//       int avgPoint = Convert.ToInt32(sum / ClassPoints.Length);
      
//      // compare
     
//      return YourPoints > avgPoint? true : false;
  
//   }
// }