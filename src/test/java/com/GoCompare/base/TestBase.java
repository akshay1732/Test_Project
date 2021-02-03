package com.GoCompare.base;

import java.io.FileInputStream;
import java.util.Properties;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;



public class TestBase {
	
	public static final Properties prop = new Properties();
	protected final static String workDir = System.getProperty("user.dir");
	static WebDriver driver;

	public static void Initialize() throws Exception {
		
		
		//Read properties file
		FileInputStream ip = new FileInputStream(workDir +"\\src\\test\\java\\com\\GoCompare\\config\\config.properties");
		prop.load(ip);
		
		
		
		//Launch browser
		if (prop.getProperty("browser").equals("chrome")) {
			
			System.setProperty("webdriver.chrome.driver", workDir +"\\src\\test\\java\\com\\GoCompare\\driver\\chromedriver.exe");
			driver = new ChromeDriver();
			
			
			
		}
		else {
			System.out.println("Hello");
		}
		
		
	}

}
