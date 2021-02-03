package com.GoCompare.pageobjects;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

import com.GoCompare.base.TestBase;

public class QuotePage extends TestBase {
	
	
	//OR
	
	@FindBy(xpath="//*[@id='form0']/fieldset/div[2]/span[2]/div[1]/label")
	WebElement Ownbutton;
	
	@FindBy(xpath="//*[@id='form0']/fieldset/div[3]/div[1]/span[2]/div[2]/label")
	WebElement outrightbtn;

	@FindBy(xpath="//*[@id='form0']/fieldset/div[3]/div[2]/span[2]/div[1]/label")
	WebElement combinedcoverbtn;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_FirstName']")
	WebElement firstname;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_Surname']")
	WebElement lastname;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_DateOfBirth_Day']")
	WebElement dayofbirth;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_DateOfBirth_Month']")
	WebElement monthofbirth;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_DateOfBirth_Year']")
	WebElement yearofbirth;
	
	@FindBy(xpath="//*[@id='HomeNewCustomerViewModel_EmailAddress']")
	WebElement emailaddress;
	
	
	@FindBy(xpath="//*[@id='form0']/div[2]/div/div[2]/div[2]/ul/li[2]/label")
	WebElement Noupdatesbtn;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

}
