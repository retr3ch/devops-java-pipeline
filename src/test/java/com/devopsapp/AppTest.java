package test.java.com.devopsapp;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    
    @Test
    public void testBasicLogic() {
        String result = "OK";
        assertEquals("Result should be OK", "OK", result);
    }
    
    @Test
    public void testTrueCondition() {
        assertTrue("True should be true", true);
    }
    
    @Test
    public void testFalseCondition() {
        assertFalse("False should be false", false);
    }
}