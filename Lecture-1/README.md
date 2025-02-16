# Test Case : Verifying Title of a webpage



Firstly, we need to import modules.

<img width="486" alt="Screenshot 2025-02-16 at 02 33 17" src="https://github.com/user-attachments/assets/ad88bc70-e230-47e3-9c30-810311377a15" />


Creating WebDriver for Chrome.

<img width="207" alt="Screenshot 2025-02-16 at 02 37 16" src="https://github.com/user-attachments/assets/cc2a17d1-f6ac-42e1-a520-8d7d6c6de3ed" />


driver.get() is used for reaching URL.

<img width="374" alt="Screenshot 2025-02-16 at 02 40 52" src="https://github.com/user-attachments/assets/be90f44f-7620-4fb2-acc1-73a5c07b1113" />


WebDriver offers a number of ways to find elements using the find_element method.In this example, ID is used for reaching element.Then send_keys() sends keys, this is similar to entering keys using your keyboard.

<img width="339" alt="Screenshot 2025-02-16 at 02 43 09" src="https://github.com/user-attachments/assets/3dc26424-5296-4f5f-a2de-2f0a71224443" />

Instead of ID, we can use other elements.The attributes available for the By class are used to locate elements on a page. 

<img width="421" alt="Screenshot 2025-02-16 at 02 57 04" src="https://github.com/user-attachments/assets/678ba9c5-6064-4df4-b14d-f58880d023ad" />

For clicking a button on webpage, we use click().However before clicking,we need to reach element by using find_elemment

<img width="768" alt="Screenshot 2025-02-16 at 02 58 14" src="https://github.com/user-attachments/assets/ad85cc45-32b3-4d5e-9424-a73ae413b853" />

Finally, to compare actual title and expected title, we need to use a if condition.

<img width="391" alt="Screenshot 2025-02-16 at 02 59 13" src="https://github.com/user-attachments/assets/2d2add20-8d36-4266-b529-7323a601e55b" />



