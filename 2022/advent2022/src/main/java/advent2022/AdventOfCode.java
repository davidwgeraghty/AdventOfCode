package advent2022;
import java.io.FileNotFoundException;

import advent2022.days.*;

public final class AdventOfCode {
    private AdventOfCode() {
    }

    public static void main(String[] args) throws FileNotFoundException {
        Day8 day = new Day8();

        String part1 = day.getPart1Answer();
        String part2 = day.getPart2Answer();
        
        System.out.println("Part 1: " + part1);
        System.out.println("Part 2: " + part2);
    }
}
