package src.Test;


import java.util.Random;
import java.util.Scanner;

public class PlayerChoose {
	public static int pcWinGame = 0;
	public static int peopleWinGame = 0;
	public static int pcPlayer() {
		Random random = new Random(); 	
		int pcSelect = random.nextInt(3);
		return pcSelect;
		
	}
	public static String peoplePlayer() {
		System.out.print("Select : Scissors, Paper, Rock ==> ");
		Scanner scan = new Scanner(System.in);
		String peopleSelect = scan.nextLine();
		while(!(peopleSelect.equals("Scissors")) && !(peopleSelect.equals("Paper")) && !(peopleSelect.equals("Rock"))) {
			System.out.print("Select : Scissors, Paper, Rock ==> ");
			peopleSelect = scan.nextLine();
		}
		return peopleSelect;
	}
	public static void displaywhoSelect(String pcValue,String peopleValue) {
		System.out.println("PC Player Select : " + pcValue);
		System.out.println("People Player Select : " + peopleValue);
	}
}
