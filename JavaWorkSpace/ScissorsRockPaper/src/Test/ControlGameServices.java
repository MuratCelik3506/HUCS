package src.Test;



public class ControlGameServices {
	public static void whoWinWho(int pcSelect, String peopleSelect) {
		String pcSelectChoose = GameAttiributeEnum.getGameAttiributeEnum(pcSelect);
		PlayerChoose.displaywhoSelect(pcSelectChoose, peopleSelect);
		if (pcSelectChoose.equals(peopleSelect)) {
			System.out.println("Draw");
			winPlayerWin(0);
		}
		else if (peopleSelect.equals("Scissors") && pcSelectChoose.equals("Paper")) {
			System.out.println("Win People");
			winPlayerWin(1);
			}
		else if (peopleSelect.equals("Rock") && pcSelectChoose.equals("Scissors")){
			System.out.println("Win People");
			winPlayerWin(1);
		}
		else if(peopleSelect.equals("Paper") && pcSelectChoose.equals("Rock")) {
			System.out.println("Win People");
			winPlayerWin(1);
		}
		else {
			System.out.println("Win PC");
			winPlayerWin(-1);
		}
		System.out.println("PC Player : " + PlayerChoose.pcWinGame + " -- " + "People Player : " + PlayerChoose.peopleWinGame + "\n");
		
	}
	public static void winPlayerWin(int player) {
		
		if (player == 1) {
			PlayerChoose.peopleWinGame++;
			if (PlayerChoose.peopleWinGame==3) {
				System.out.println("PC Player : " + PlayerChoose.pcWinGame + " -- " + "People Player : " + PlayerChoose.peopleWinGame + "\n");
				System.out.println("Finally Win People"); 
				System.exit(0);
			}
			
		}
		else if (player == -1) {
			PlayerChoose.pcWinGame++;
			if (PlayerChoose.pcWinGame==3) {
				System.out.println("PC Player : " + PlayerChoose.pcWinGame + " -- " + "People Player : " + PlayerChoose.peopleWinGame + "\n");
				System.out.println("Finally Win PC"); 
				System.exit(0);
			}
			else {
		;
			}
		
	}

	}}
