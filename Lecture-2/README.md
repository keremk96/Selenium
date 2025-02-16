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

## 3- LINK_TEXT Locater

Specifically used to locate anchor (<a>) elements by their visible text. This is helpful for finding links.

Syntax ==> driver.find_element(By.LINK_TEXT, “Visible Text”))

For example, we try to click Forgotten password?.

<img width="385" alt="Screenshot 2025-02-16 at 17 41 24" src="https://github.com/user-attachments/assets/484502a6-4ed7-4072-a89e-3295c91da1a7" />

For instance, consider this page source:

<img width="402" alt="Screenshot 2025-02-16 at 17 41 43" src="https://github.com/user-attachments/assets/2cf4f462-f27e-47f7-8515-a81d8d2206e0" />

We need to find LINK_TEXT location by using find_element().The form element can be located like this:

<img width="499" alt="Screenshot 2025-02-16 at 17 46 46" src="https://github.com/user-attachments/assets/524c46ef-804f-4371-94a8-d51b633db6fe" />

Then, using click(), we can go website.

<img width="128" alt="Screenshot 2025-02-16 at 17 47 11" src="https://github.com/user-attachments/assets/b67699d4-7f57-40e9-8f64-2b356b6a1481" />

Result:

<img width="493" alt="Screenshot 2025-02-16 at 17 42 37" src="https://github.com/user-attachments/assets/c5466822-e119-485c-9716-aa565616fea8" />

## 4- PARTIAL_LINK_TEXT Locater

Similar to Link Text, but allows for partial matching of the anchor text, making it useful for long or dynamic link text.

Syntax ==> driver.find_element(By.PARTIAL_LINK_TEXT, “Partial Text”);

For instance, we try to click Forgotten password?.

<img width="385" alt="Screenshot 2025-02-16 at 17 41 24" src="https://github.com/user-attachments/assets/5d337a65-3e09-43cf-9ff2-ead2eb28667e" />

For instance, consider this page source:

<img width="402" alt="Screenshot 2025-02-16 at 17 41 43" src="https://github.com/user-attachments/assets/6cce6298-36bc-43ae-9713-349d2fc34a56" />

We need to find PARTIAL_LINK_TEXT location by using find_element().The form element can be located like this:

<img width="546" alt="Screenshot 2025-02-16 at 17 51 12" src="https://github.com/user-attachments/assets/702614d1-59a9-4d0c-b77b-384ace1573f3" />

Then, using click(), we can go website.

<img width="196" alt="Screenshot 2025-02-16 at 17 56 13" src="https://github.com/user-attachments/assets/ae8f4078-c6c7-4ba0-a33b-715ef5a44f2a" />

Result:

<img width="493" alt="Screenshot 2025-02-16 at 17 42 37" src="https://github.com/user-attachments/assets/b6721ccf-94eb-4256-b0bf-434e88d5ff7c" />

## 4- CLASS_NAME Locater

Targets elements based on their class attribute. This is useful for selecting multiple elements that share a class.

Syntax ==> driver.find_element(By.CLASS_NAME, “className”)

For exampele, we want to write Selenium in serch box.

<img width="653" alt="Screenshot 2025-02-16 at 18 09 46" src="https://github.com/user-attachments/assets/0e9b79bc-2448-48b5-b193-5e1a7c56097f" />

For instance, consider this page source:

<img width="561" alt="Screenshot 2025-02-16 at 18 09 29" src="https://github.com/user-attachments/assets/89241219-8035-4a58-90b6-a9b19041bbd8" />

We need to find CLASS_NAME location by using find_element().The form element can be located like this:

<img width="439" alt="Screenshot 2025-02-16 at 18 12 25" src="https://github.com/user-attachments/assets/1028ad43-122c-40c4-9b1c-0b714e441e39" />

Result:

<img width="728" alt="Screenshot 2025-02-16 at 18 12 04" src="https://github.com/user-attachments/assets/894dc87a-8602-4309-a5a0-cf352e4e3725" />


