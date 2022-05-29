package grade;

public class Grade {
	public static int grade(int i){
		if(i>2000)
			return 1;
		else if(i>1300&&i<=2000)
			return 2;
		else if(i>800&&i<=1300)
			return 3;
		else if(i>500&&i<=800)
			return 4;
		else if(i>200&&i<=500)
			return 5;
		else if(i>50&&i<=200)
			return 6;
		else if(i>=0&&i<50)
			return 7;
		else return 0;
	}
	
}
