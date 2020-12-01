right_clicks = []
def mouse_callback(event, x, y, flags, params):

    #right-click event value is 2
    if event == 2:
        global right_clicks

        #store the coordinates of the right-click event
        right_clicks.append([x, y])

        #this just verifies that the mouse data is being collected
        #you probably want to remove this later
        print(right_clicks)

ret, frame = video.read()
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', mouse_callback)
cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()