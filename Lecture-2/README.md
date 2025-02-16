# Locaters

Locators in Selenium WebDriver are used to identify and interact with WebElements within a web page’s Document Object Model (DOM). 
They act as unique identifiers for web elements, allowing testers to perform various actions such as clicking buttons, entering text, or validating the presence of elements.
Selenium provides different locator such as ID, Name, TagName, ClassName, XPath, CSS Selector, LinkText, and PartialLinkText. 

## 1- ID Locater

Locates an element using its unique ID attribute. 

Syntax ==> driver.find_element(By.ID, “elementID”)

For example, We try to write standard_user to Username box.

<img width="589" alt="Screenshot 2025-02-16 at 17 00 58" src="https://github.com/user-attachments/assets/1b8ea725-3a19-41b0-8910-e54beff8cc6f" />

For instance, consider this page source:

<img width="576" alt="Screenshot 2025-02-16 at 17 01 17" src="https://github.com/user-attachments/assets/e33d126e-ec41-4f90-a4e0-81f1a8bae7eb" />

Firstly, we need to find ID location by using find_element().The form element can be located like this:

<img width="332" alt="Screenshot 2025-02-16 at 17 01 46" src="https://github.com/user-attachments/assets/966e2812-3efb-4537-aa75-1d4cd4b15a9a" />

Then, we need to write standard_user by using send_keys().

<img width="222" alt="Screenshot 2025-02-16 at 17 01 55" src="https://github.com/user-attachments/assets/3f32fe08-6a96-4adc-bf2e-06f063075aa5" />

Result:

<img width="370" alt="Screenshot 2025-02-16 at 17 02 10" src="https://github.com/user-attachments/assets/5287c152-f0f8-4ed2-afa9-fdffb8bc02cb" />

## 2- NAME Locater
Finds elements by their name attribute.

Syntax ==> driver.find_element(By.NAME, “elementName”)

We can perform the same procedure by using NAME locater.

<img width="589" alt="Screenshot 2025-02-16 at 17 00 58" src="https://github.com/user-attachments/assets/3c92163a-f26a-436e-9201-f2e9b96123d6" />

For instance, consider this page source:

<img width="576" alt="Screenshot 2025-02-16 at 17 01 17" src="https://github.com/user-attachments/assets/aadd2b10-1e68-4cc1-9b39-2696df2b0163" />

We need to find NAME location by using find_element().The form element can be located like this:

<img width="364" alt="Screenshot 2025-02-16 at 17 18 21" src="https://github.com/user-attachments/assets/f8afc9fa-8d7d-44d7-8925-8b380e59a81f" />

Then, we need to write standard_user by using send_keys().

<img width="237" alt="Screenshot 2025-02-16 at 17 18 29" src="https://github.com/user-attachments/assets/f65c30f3-afd3-44de-a3f1-7515de0bd82e" />

Result:

<img width="370" alt="Screenshot 2025-02-16 at 17 02 10" src="https://github.com/user-attachments/assets/951a5a76-3574-4822-a454-99aa001ebdab" />
