# 05- Experiment Testing

Hey team, great work making it this far!

Now that the FaceGuard system is up and running, it's time to test it thoroughly.

Testing is where we see how well our project holds up in the real world.

We'll test its functionality, accuracy, and performance under different conditions.

Think of this as giving our system a good workout to see how strong it really is!

---

## Step 1: Functional Testing

First, we need to check if each feature of the system works as expected. Here's what to do:

1. **Test the Face Detection Module:**
   - Open your `face_detection.py` file and run it.
   - Move your face into the webcam frame and confirm that the system detects it by drawing a rectangle around your face.
   - Try with multiple faces in the frame and see if it can detect them all.

2. **Test the Facial Recognition Feature:**
   - Use the `face_recognition` functionality.
   - Test with the known image you used earlier (e.g., `known_person.jpg`).
   - Confirm that the system recognizes the face and prints "Face recognized!"
   - Introduce an unfamiliar face and ensure the system does *not* recognize it.

3. **Test the Authentication Logic:**
   - Ensure that recognized faces print "Access Granted" and unrecognized faces print "Access Denied."
   - Experiment with different scenarios, like partially covering your face, to see how the system responds.

---

## Step 2: Accuracy Testing

Accuracy is crucial for biometric systems. Here's how to test it:

1. **Create a Variety of Test Cases:**
   - Use different faces—your own, friends, family, or even printed photos.
   - Test under different lighting conditions: bright light, dim light, and natural light.

2. **Check False Positives:**
   - A false positive happens when the system recognizes someone it shouldn't.
   - Test this by showing the system faces it shouldn't recognize and ensure "Access Denied" is printed.

3. **Check False Negatives:**
   - A false negative happens when the system fails to recognize someone it should.
   - Test this by using the face it’s trained to recognize. Ensure "Access Granted" is printed.

---

## Step 3: Stress Testing

Let's see how the system performs under tougher conditions. Here are some ideas:

1. **Different Angles:**
   - Move your face to different angles: left, right, tilted up, and tilted down.
   - Check if the system can still recognize you.

2. **Different Distances:**
   - Test at varying distances from the camera. Start close and move farther away.
   - Note how far you can be while still being recognized.

3. **Dynamic Movements:**
   - Move your head or walk across the webcam frame.
   - Check if the system can keep up and detect your face.

---

## Step 4: Performance Benchmarking

Let’s evaluate the speed and efficiency of the system:

1. **Measure Detection Time:**
   - Use Python’s `time` module to measure how long it takes to detect and recognize a face.
   - Add timing code like this:
     ```python
     import time

     start_time = time.time()
     # Run face detection/recognition code here
     end_time = time.time()
     print("Processing Time:", end_time - start_time, "seconds")
     ```

2. **Test with High Traffic:**
   - Simulate a busy scenario with multiple faces in the frame.
   - Check if the system’s performance slows down or remains stable.

3. **CPU/GPU Utilization:**
   - Monitor your system’s resource usage while running FaceGuard.
   - Use tools like `top` (Linux) or Task Manager (Windows) to ensure the system doesn’t overburden your machine.

---

## Step 5: User Feedback

If possible, ask others to try your system! Here’s what to do:

1. **Have Friends Test It:**
   - Ask them to try both recognized and unrecognized faces.
   - Note their feedback on how intuitive and reliable the system feels.

2. **Document Observations:**
   - Write down any bugs, unexpected behavior, or areas for improvement.

---

## Step 6: Debugging and Refining

If you encounter issues during testing, here’s how to tackle them:

1. **Review Error Messages:**
   - Carefully read any errors or warnings in your terminal. They’re often the key to fixing problems.

2. **Tweak Parameters:**
   - For example, adjust the `scaleFactor` or `minNeighbors` parameters in the face detection code to improve accuracy.

3. **Optimize Lighting and Camera Position:**
   - Ensure the webcam is positioned correctly, and the lighting is even.

4. **Ask for Help:**
   - If you’re stuck, don’t hesitate to ask classmates or mentors for advice.

---

## Next Steps

Once testing is complete and your system is working like a champ, it’s time to wrap everything up and reflect on what we’ve learned.

In the next section, **06-Troubleshooting & Optimization.md**, we’ll tackle common challenges and explore ways to make the system even better.

Stay tuned & great job so far!

