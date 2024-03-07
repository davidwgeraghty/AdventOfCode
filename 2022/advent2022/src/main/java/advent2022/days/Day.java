package advent2022.days;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public abstract class Day {
    
    protected File getInputFile(boolean test, String day) {
        String fileName = (test ? "src/main/resources/testdata" : "src/main/resources/input") + day + ".txt";
        File file = null;
        try {
            file = new File(fileName);
        }
        catch(Exception e) {
            System.out.println("computer says no");
        }
        
        return file;
    }

    protected ArrayList<String> getLinesFromFile(File file) {
        ArrayList<String> lines = new ArrayList<>();
        try {
            for (Scanner scanner = new Scanner(file); scanner.hasNext();)
            {
                lines.add(scanner.nextLine());
            }
        }
        catch(Exception e) {
            System.out.println(e.toString());
        }
        return lines;
    }

    public String getPart1Answer(){
        File file = getInputFile(true, "1");
        return "Not implemented";
    }

    public String getPart2Answer(){
        File file = getInputFile(true, "1");
        return "Not implemented";
    }
}
