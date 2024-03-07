package advent2022.days;

import java.io.File;
import java.util.Scanner;

public class Day3 extends Day{

    public String getPart1Answer(){
        File file = getInputFile(false, "3");
        int total = 0;
        try
        {
            for(Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                String line = scanner.nextLine();
                String compartment1 = line.substring(0, line.length()/2);
                String compartment2 = line.substring(line.length()/2, line.length());
                
                for (int i = 0; i < compartment1.length(); i++){
                    char c = compartment1.charAt(i);        
                    if (compartment2.indexOf(c) >= 0)
                    {
                        total += Character.getNumericValue(c) - 9;
                        if (Character.isUpperCase(c))
                        {
                            total += 26;
                        }
                        break;
                    }
                }
            }
        }
        catch(Exception e)
        {
            System.out.println("oops");
        }

        return Integer.toString(total);
    }

    public String getPart2Answer(){
        File file = getInputFile(false, "3");
        int total = 0;
        try
        {
            for(Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                String line1 = scanner.nextLine();
                String line2 = scanner.nextLine();
                String line3 = scanner.nextLine();

                for (int i = 0; i < line1.length(); i++){
                    char c = line1.charAt(i);
                          
                    if (line2.indexOf(c) >= 0 && line3.indexOf(c) >= 0){
                        total += Character.getNumericValue(c) - 9;
                        if (Character.isUpperCase(c))
                        {
                            total += 26;
                        }
                        break;
                    }
                }
            }
        }
        catch(Exception e)
        {
            System.out.println("oops");
        }

        return Integer.toString(total);
    }
}
