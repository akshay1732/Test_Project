package com.GoCompare.pageobjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.GoCompare.base.TestBase;

public class LandingPage extends TestBase {
	
	
@FindBy(id="postcode__input")
WebElement postcodeinput;


LandingPage(){
	
	super();
}

public static QuotePage Enterpostcode(){
	
	return new QuotePage();
//	Wait wait = new WebDriverWait(driver);
	
	
	
}



}
