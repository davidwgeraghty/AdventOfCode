package advent2022.days;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Day5 extends Day{

    public static boolean isNumeric(String str) { 
        try {  
            Double.parseDouble(str);  
            return true;
        } catch(NumberFormatException e){  
            return false;  
        }  
    }

    public String getPart1Answer(){
        File file = getInputFile(false, "5");
        String answer = "";
        LinkedHashMap<String, ArrayList<Character>> stack = new LinkedHashMap<String, ArrayList<Character>>();
        try {
            for(Scanner scanner = new Scanner(file); scanner.hasNext();){
                ArrayList<String> stackList = new ArrayList<String>();
                String line = scanner.nextLine();

                if (line.isBlank())
                    continue;

                // parse stack
                if (!line.contains("move") && !line.isBlank())
                {
                    // stacks
                    while (line.contains("[")) {
                        stackList.add(line);
                        line = scanner.nextLine();
                    }
                    
                    for (int i = 0; i < line.length(); i++)
                    {
                        String str = String.valueOf(line.charAt(i));
                        if (!str.isBlank() && isNumeric(str))
                        {
                            ArrayList charList = new ArrayList<Character>();
                            for (int j = stackList.size()-1; j >= 0; j--) {
                                String row = stackList.get(j);
                                if (!String.valueOf(row.charAt(i)).isBlank())
                                    charList.add(row.charAt(i));
                            }
                            stack.put(str, charList);
                        }
                    }
                }
                // do instructions
                else {
                    int iterations = Integer.parseInt(line.split("move ")[1].split(" from")[0]);
                    String source = line.split("from ")[1].split(" to")[0];
                    String destination = line.split("to ")[1];
                    for (int i = 0; i < iterations; i++) {
                        stack.get(destination).add(stack.get(source).remove(stack.get(source).size()-1));
                    }
                }
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }

        for (String key: stack.keySet()) {
            ArrayList<Character> list = stack.get(key);
            answer += list.get(list.size()-1);
        }

        return answer;
    }

    public String getPart2Answer(){
        File file = getInputFile(false, "5");
        String answer = "";

        LinkedHashMap<String, ArrayList<Character>> stack = new LinkedHashMap<String, ArrayList<Character>>();
        try {
            for(Scanner scanner = new Scanner(file); scanner.hasNext();){
                ArrayList<String> stackList = new ArrayList<String>();
                String line = scanner.nextLine();

                if (line.isBlank())
                    continue;

                // parse stack
                if (!line.contains("move") && !line.isBlank())
                {
                    // stacks
                    while (line.contains("[")) {
                        stackList.add(line);
                        line = scanner.nextLine();
                    }
                    
                    for (int i = 0; i < line.length(); i++)
                    {
                        String str = String.valueOf(line.charAt(i));
                        if (!str.isBlank() && isNumeric(str))
                        {
                            ArrayList charList = new ArrayList<Character>();
                            for (int j = stackList.size()-1; j >= 0; j--) {
                                String row = stackList.get(j);
                                if (!String.valueOf(row.charAt(i)).isBlank())
                                    charList.add(row.charAt(i));
                            }
                            stack.put(str, charList);
                        }
                    }
                }
                // do instructions
                else {
                    int iterations = Integer.parseInt(line.split("move ")[1].split(" from")[0]);
                    String sourceStr = line.split("from ")[1].split(" to")[0];
                    String destinationStr = line.split("to ")[1];
                    ArrayList<Character> source = stack.get(sourceStr);
                    ArrayList<Character> destination = stack.get(destinationStr);

                    destination.addAll(source.subList(source.size() - iterations, source.size()));
                    for (int i = 0; i < iterations; i++) {
                        source.remove(source.size() - 1);
                    }
                }
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }

        for (String key: stack.keySet()) {
            ArrayList<Character> list = stack.get(key);
            answer += list.get(list.size()-1);
        }

        return answer;
    }
}
