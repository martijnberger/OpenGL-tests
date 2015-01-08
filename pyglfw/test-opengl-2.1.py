__author__ = 'Martijn Berger'

import OpenGL.GL as gl
import numpy as np
import ctypes
import glfw

NULL = ctypes.c_void_p(0)

vertex_data = np.array([-1,-1, -1,+1,  +1,-1, +1,+1 ], dtype=np.float32)

color_data = np.array([1,0,0,1, 0,1,0,1, 0,0,1,1, 1,1,0,1], dtype=np.float32)

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "OpenGL 2.1", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glColorPointer(4, gl.GL_FLOAT, 0, color_data)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)
        gl.glVertexPointer(2, gl.GL_FLOAT, 0,  vertex_data)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()



