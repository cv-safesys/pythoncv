# System for recognizing people in the room with e-mail notification

The concept of the project is to develop a security system based on computer vision. The algorithm is based on color segmentation - whether a person has a uniform of a unique color for this room, and on identifying a person using facial recognition.

## Principle of operation.

A person entering a room from a distance is identified as a person (using facial recognition). Next, the algorithm looks at the presence of a unique color in the frame (uniform). If the color in the required range is not detected, a message is sent to the email about the presence of a stranger. If the result is positive for face and color recognition, the second step is identification. A person in a limited period of time must approach the camera to identify him as an employee (his face is present in the database in advance). This step is used to prevent unauthorized persons wearing uniforms from being found. If identification is successful, an informational message is sent with the name of the employee who is in the room. Otherwise, a warning message is sent about the presence of an unauthorized person in the room. In order to pass the identification, a similarity threshold will be set (the minimum tolerance value), which will be set by us in practice.

The algorithm is based on Python 3.7 using the OpenCV library.
