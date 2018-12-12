"""
Exam 1, problem 4.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Nathalie Grier.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem4'
    window = rg.RoseWindow(400, 400, title)

    problem4(8, 40, rg.Point(10, 350), window)
    window.close_on_mouse_click()

    # THREE tests on ANOTHER window.
    title = 'Tests 2, 3 and 4 of problem4'
    window = rg.RoseWindow(450, 400, title)

    problem4(5, 50, rg.Point(50, 270), window)
    window.continue_on_mouse_click()

    problem4(20, 10, rg.Point(10, 350), window)
    window.continue_on_mouse_click()

    problem4(3, 100, rg.Point(130, 350), window)
    window.close_on_mouse_click()


def problem4(number_of_stairs, step_size, starting_point, window):
    """
    See   problem4_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- Two positive integers
      -- An rg.Point.
      -- A rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given RoseWindow:
      -- The given starting_point.
      -- A "staircase" of rg.Line objects as DESCRIBED ON THE ATTACHED PDF
            (problem4_picture.pdf).
      -- The last (highest and furthest to the right) point.
           (Draw it as an rg.Point.)
      Must render but   ** NOT close **   the window.

    Type hints:
      :type number_of_stairs:  int
      :type step_size:          int
      :type starting_point:    rg.Point
      :type window:            rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT: For PARTIAL CREDIT, you can draw just the black "bottoms"
    #            of the stair steps.
    # -------------------------------------------------------------------------
    start = starting_point
    end = rg.Point(start.x + (number_of_stairs) * step_size, start.y - (number_of_stairs) * step_size)
    for k in range(number_of_stairs):
        startb = rg.Point(start.x + (k) * step_size, start.y - (k + 1) * step_size)
        endb = rg.Point(startb.x + step_size, startb.y)
        black_line = rg.Line(startb, endb)
        black_line.thickness = 3
        black_line.attach_to(window)

        startm = rg.Point(start.x + (k) * step_size, start.y - k * step_size)
        endm = rg.Point(startm.x, startm.y - step_size)
        magenta_line = rg.Line(startm, endm)
        magenta_line.color = 'magenta'
        magenta_line.thickness = 3

        start.attach_to(window)
        end.attach_to(window)
        magenta_line.attach_to(window)

        window.render()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
