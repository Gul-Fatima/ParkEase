**Parking Lot Position Management System for Administrators**


**1. Introduction:**
The Parking Lot Position Management System is a specialized tool designed for administrators to efficiently manage parking spaces within a parking lot. This system provides intuitive features for marking and deleting parking spaces on an image representation of the parking lot. By leveraging the OpenCV library, the system offers a user-friendly interface for administrators to interact with parking space data effectively.
![Login Window](https://github.com/Gul-Fatima/ParkEase/blob/main/Win1ss.png)


**2. Features:**
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
