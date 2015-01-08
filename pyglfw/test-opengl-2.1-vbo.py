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
    window = glfw.create_window(640, 480, "OpenGL 2.1 + VBO", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    vVBO = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vVBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, gl.GL_STATIC_DRAW)

    cVBO = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, cVBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, color_data.nbytes, color_data, gl.GL_STATIC_DRAW)

   
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, cVBO)
        gl.glColorPointer(4, gl.GL_FLOAT, 0, NULL)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vVBO)
        gl.glVertexPointer(2, gl.GL_FLOAT, 0,  NULL)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()



