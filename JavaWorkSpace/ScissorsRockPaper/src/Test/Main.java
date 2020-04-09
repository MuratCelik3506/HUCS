package src.Test;


public class Main {

	public static void main(String[] args) {
		for (int i = 0 ; i<1000 ; i++) {
			ControlGameServices.whoWinWho(PlayerChoose.pcPlayer(), PlayerChoose.peoplePlayer());
		}
	}

}
