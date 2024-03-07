package advent2022.days;

import java.io.File;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Stream;

public class Day2 extends Day {

    public enum ElfHand {
        ROCK('A'),
        PAPER('B'),
        SCISSORS('C');
    
        public final char letter;
    
        private ElfHand(char letter) {
            this.letter = letter;
        }
    }

    public enum YourHand {
        ROCK('X', 1, ElfHand.SCISSORS),
        PAPER('Y', 2, ElfHand.ROCK),
        SCISSORS('Z', 3, ElfHand.PAPER);
    
        public final char letter;
        public final int shapeScore;
        public final ElfHand beats;
    
        private YourHand(char letter, int shapeScore, ElfHand beats) {
            this.letter = letter;
            this.shapeScore = shapeScore;
            this.beats = beats;
        }
    }

    public enum Instruction {
        WIN('Z'),
        LOSE('X'),
        DRAW('Y');
    
        public final char letter;
    
        private Instruction(char letter) {
            this.letter = letter;
        }
    }

    private int getPointsForMatch(ElfHand elfHand, YourHand yourHand) {
        int matchPoints = yourHand.shapeScore;

        if(yourHand.beats == elfHand){
            matchPoints += 6;
        }
        else if(yourHand.name().equals(elfHand.name())){
            matchPoints += 3;
        }
        else{
            // no points for losing
        }
        
        return matchPoints;
    }

    private YourHand getHandForInstruction(Instruction instruction, ElfHand elfHand) {
        if(instruction == Instruction.WIN) {
            return Arrays.stream(YourHand.values()).filter(o -> o.beats == elfHand).findFirst().get();
        }
        else if(instruction == Instruction.DRAW)
        {
            return Arrays.stream(YourHand.values()).filter(o -> o.name() == elfHand.name()).findFirst().get();
        }
        else {
            return Arrays.stream(YourHand.values())
                    .filter(o -> o.name() != elfHand.name() && o.beats != elfHand)
                    .findFirst().get();
        }
    }

    public String getPart1Answer() {
        File file = getInputFile(false, "2");

        int total = 0;
        try{
            for(Scanner scanner = new Scanner(file); scanner.hasNext();){

                String line = scanner.nextLine();

                ElfHand elfHand = Arrays.stream(ElfHand.values()).filter(o -> o.letter == line.charAt(0)).findFirst().get();
                YourHand yourHand = Arrays.stream(YourHand.values()).filter(o -> o.letter == line.charAt(2)).findFirst().get();

                total += getPointsForMatch(elfHand, yourHand);
            }
        }
        catch(Exception e)
        {
            System.out.println("oops");
        }

        return Integer.toString(total);
    }

    public String getPart2Answer() {
        File file = getInputFile(false, "2");

        int total = 0;
        try{
            for(Scanner scanner = new Scanner(file); scanner.hasNext();){

                String line = scanner.nextLine();

                ElfHand elfHand = Arrays.stream(ElfHand.values()).filter(o -> o.letter == line.charAt(0)).findFirst().get();
                Instruction instruction = Arrays.stream(Instruction.values()).filter(o -> o.letter == line.charAt(2)).findFirst().get();
                YourHand yourHand = getHandForInstruction(instruction, elfHand);

                total += getPointsForMatch(elfHand, yourHand);
            }
        }
        catch(Exception e)
        {
            System.out.println("oops");
        }

        return Integer.toString(total);
    }
}
