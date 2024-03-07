package advent2022.days;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Day1 extends Day {

    private List<Integer> getElfCalorieList(File file) {
        List<Integer> sumList = new ArrayList<Integer>();
        int sum = 0;

        try {
            for(Scanner scanner = new Scanner(file); scanner.hasNext();) {
                String line = scanner.nextLine();
    
                if(line.isEmpty()) {
                    sumList.add(sum);
                    sum = 0;
                }
                else {
                    sum += Integer.parseInt(line);
                }
            }
        }
        catch(Exception e) {
            System.out.println("Computer says no.");
        }
        
        sumList.add(sum);

        return sumList;
    }

    public String getPart1Answer() {
        File file = getInputFile(false, "1");
        List<Integer> elfCalorieList = getElfCalorieList(file);
        return elfCalorieList.stream().reduce((num1, num2) -> Math.max(num1, num2)).get().toString();
    }

    public String getPart2Answer() {
        File file = getInputFile(false, "1");
        List<Integer> elfCalorieList = getElfCalorieList(file);
        return getTop3ElfCalorieCounts(elfCalorieList);
    }

    private String getTop3ElfCalorieCounts(List<Integer> elfCalorieListelfCalorieList) {
        int sum = 0;
        Collections.sort(elfCalorieListelfCalorieList, Collections.reverseOrder());

        for (int i = 0; i < 3; i++) {
            sum += elfCalorieListelfCalorieList.get(i);
        }

        return Integer.toString(sum);
    }
}
