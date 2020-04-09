package src.Test;


public enum GameAttiributeEnum {
	Scissors,Paper,Rock;

	
	public static String getGameAttiributeEnum(int index) {
		String deger = GameAttiributeEnum.values()[index].toString();
		return deger;
	}
}
