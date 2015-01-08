__author__ = 'Martijn Berger'

import OpenGL.GL as gl
import numpy as np
import ctypes
import glfw

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "OpenGL 1.x", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glBegin(gl.GL_TRIANGLE_STRIP)
        gl.glColor4f(1,0,0,1)
        gl.glVertex2f(-1.0,-1.0)
        gl.glColor4f(0,1,0,1)
        gl.glVertex2f(-1.0,+1.0)
        gl.glColor4f(0,0,1,1)
        gl.glVertex2f(+1.0,-1.0)
        gl.glColor4f(1,1,0,1)
        gl.glVertex2f(+1.0,+1.0)
        gl.glEnd()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()



