package advent2022.days;

import java.io.File;
import java.util.Scanner;

public class Day6 extends Day{

    private String findMarker(File file, int markerSize) {
        try {
            for (Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                String line = scanner.nextLine();
                for (int i = markerSize-1; i < line.length(); i++)
                {
                    boolean duplicateFound = false;
                    String charStr = "";
                    for (int j = 0; j < markerSize; j++)
                    {
                        char character = line.charAt(i - j);
                        if (charStr.indexOf(character) >= 0)
                        {
                            duplicateFound = true;
                            break;
                        }
                        charStr += character;
                    }
                    if (!duplicateFound)
                        return String.valueOf(i + 1);
                }
            }
        }
        catch(Exception e) {
            System.out.println(e.toString());
        }

        return "No result found";
    }

    public String getPart1Answer(){
        File file = getInputFile(false, "6");
        return findMarker(file, 4);
    }

    public String getPart2Answer(){
        File file = getInputFile(false, "6");
        return findMarker(file, 14);
    }
}
