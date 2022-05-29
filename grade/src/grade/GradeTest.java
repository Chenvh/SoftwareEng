package grade;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class GradeTest {

	@Test
	@DisplayName("when_numberofPerson_greater_than_2000_return_1")
	void when_numberofPerson_greater_than_2000_return_1() {
		Grade grade = new Grade();
		int result =grade.grade(2020);
		assertEquals(1,result);
	}
@ParameterizedTest
@CsvSource({"2020,1","1990,2","1200,3","700,4","400,5","100,6","40,7","-5,0"})
void test1(int numberofPerson,int expectedlevel) {
	Grade grade =new Grade();
	int  result =grade.grade(numberofPerson);
	assertEquals(expectedlevel,result);
}
}
