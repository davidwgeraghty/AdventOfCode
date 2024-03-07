package advent2022.days;

import java.io.File;
import java.util.Scanner;

public class Day4 extends Day{

    public String getPart1Answer(){
        File file = getInputFile(false, "4");

        int count = 0;

        try{
            for(Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                String line = scanner.nextLine();
                int num1 = Integer.valueOf(line.split("-")[0]);
                int num2 = Integer.valueOf(line.split("-")[1].split(",")[0]);
                int num3 = Integer.valueOf(line.split(",")[1].split("-")[0]);
                int num4 = Integer.valueOf(line.split(",")[1].split("-")[1]);

                if((num1 <= num3 && num2 >= num4) || (num1 >= num3 && num2 <= num4))
                {
                    count++;
                }
            }
        }
        catch(Exception e)
        {
            System.out.println(e.toString());
        }

        return String.valueOf(count);
    }

    public String getPart2Answer(){
        File file = getInputFile(false, "4");

        int count = 0;

        try{
            for(Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                String line = scanner.nextLine();
                int num1 = Integer.valueOf(line.split("-")[0]);
                int num2 = Integer.valueOf(line.split("-")[1].split(",")[0]);
                int num3 = Integer.valueOf(line.split(",")[1].split("-")[0]);
                int num4 = Integer.valueOf(line.split(",")[1].split("-")[1]);

                if (num1 <= num4 && num2 >= num3) {
                    count++;
                }
            }
        }
        catch(Exception e)
        {
            System.out.println(e.toString());
        }

        return String.valueOf(count);
    }
}
