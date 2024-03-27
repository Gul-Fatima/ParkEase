**Parking Lot Position Management System for Administrators**


**1. Introduction:**
The Parking Lot Position Management System is a specialized tool designed for administrators to efficiently manage parking spaces within a parking lot. This system provides intuitive features for marking and deleting parking spaces on an image representation of the parking lot. By leveraging the OpenCV library, the system offers a user-friendly interface for administrators to interact with parking space data effectively.



**2. Features:**

5. **Main Interface**:
   - The main window (`root`) displays an image background (`mainwin.png`), providing a graphical user interface (GUI) for the application.
   - It includes buttons for users to sign up, access the main functionality, and view contact information.
   ![Login Window](https://github.com/Gul-Fatima/ParkEase/blob/main/Win1ss.png)

1. **User Registration (Sign Up)**:
   - The `database` function is responsible for storing user registration data (username and password) in a database file (`plproj.accdb`).
   - It performs validation checks to ensure that the required fields are not empty and that the password and confirm password fields match.
   - If the data is valid, it inserts the user information into the database.

2. **User Authentication (Sign In)**:
   - The `check_data_in_database` function verifies the user's credentials against the database to allow access to the application.
   - It checks if the entered username exists and if the corresponding password matches the provided one.
   - If the credentials are correct, it opens another window (`getstarted` function) where the user can access the main functionality of the application.

3. **Parking Space Monitoring**:
   - The `getstarted` function displays a video stream (`car video.mp4`) of a parking area.
   - It loads positions of parking spaces from a file (`CarParkPos`) and monitors each space's occupancy by analyzing the video frames.
   - It detects occupied and unoccupied parking spaces based on the pixel count within predefined regions.
   - Occupied spaces are highlighted in red, while unoccupied spaces are highlighted in green.
   - The functionality continuously loops until the user quits the application by pressing the 'q' key.

4. **Contact Information**:
   - The `contactus` function creates a window that displays contact information about the application (e.g., email, phone number, LinkedIn profile).
   - Users can access this window by clicking the "Contact us" button from the main interface.

- **Marking Parking Spaces:** Administrators can mark parking spaces on the parking lot image by simply clicking on the desired position. Upon clicking, a rectangle representing the parking space is drawn, providing a visual representation of the allocated space.
- **Deleting Parking Spaces:** To optimize space allocation, administrators can delete existing parking spaces by right-clicking on the rectangle representing the parking space they wish to remove. This feature facilitates dynamic adjustments to parking space configurations as per requirements.
- **Persistence:** The system ensures the persistence of parking space data across sessions. All marked parking spaces are automatically saved and loaded upon system startup, providing continuity and ease of use for administrators.
![Empty Space Detection](https://github.com/Gul-Fatima/ParkEase/blob/main/recss.png)
**3. Implementation Details:**
- **Image Loading:** The system loads the parking lot image from the file 'carParkImg.png' using the OpenCV `cv2.imread()` function. This image serves as the canvas for marking and managing parking spaces.
- **Event Handling:** Mouse click events are handled using the `cv2.setMouseCallback()` function. Left-clicking on the image triggers the marking of parking spaces, while right-clicking initiates the deletion process.
- **Data Persistence:** The positions of marked parking spaces are stored in a list named `pos`, which is serialized using the pickle module. The serialized data is saved to a file named 'CarParkPos', ensuring that parking space data remains intact between system sessions.

**4. Example Usage:**
1. **Marking Parking Spaces:** To designate a parking space, simply left-click on the desired position on the parking lot image. A rectangle representing the parking space will be drawn automatically.
2. **Deleting Parking Spaces:** To remove an existing parking space, right-click on the rectangle corresponding to the space you wish to delete. The system will promptly erase the parking space from the image and update the data accordingly.
3. **Data Persistence:** All parking space data is automatically saved upon any modifications and is loaded seamlessly upon system startup, ensuring continuity and ease of management.

**5. Conclusion:**
The Parking Lot Position Management System provides administrators with a robust and user-friendly tool for efficient parking space management. By offering intuitive marking and deletion functionalities, along with seamless data persistence, the system streamlines the process of managing parking spaces within a parking lot.

**6. Future Enhancements:**
- Integration of advanced image processing techniques for improved accuracy and visualization.
- Implementation of user authentication and access control features for enhanced security.


Overall, the Parking Lot Position Management System serves as a valuable asset for administrators seeking to optimize parking space allocation and streamline parking lot management operations.
