# cse210-04
# Greed Game
#Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Rules of the game:
* Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
* The player (#) can move left or right along the bottom of the screen.
* If the player touches a gem they earn a point.
* If the player touches a rock they lose a point.
* Gems and rocks are removed when the player touches them.
* The game continues until the player closes the window.
----
## Getting started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python greed game
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- seeker              (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0


## Authors
* Ron Ron Cabanjin
* Robin Dickson
* Nefi Perez Martinez
* Sariah Tanner

```
Requirements
The program must have a README file.
The program must have at least eight classes.
Each module, class and method must have a corresponding comment.
The game must remain generally true to the order of play described earlier.
```

Program Design:
* Ron Ron Cabanjin
* Robin Dickson
* Nefi Perez Martinez
* Sariah Tanner

Main Function
  def main()
  

Casting folder
actor class = The responsibility of Actor is to keep track of its appearance, position and velocity in 2d space.
  def __init__
  def get_color
  def get_font_size
  def get_position
  def get_text
  def get_velocity
  def move_next
  def set_color
  def set_position
  def set_font_size
  def set_text
  def set_velocity
  
  
Display_point class = is to display the earn or lose point of each item that player touches 
  def __init__
  def get_message
  def set_message
  
  
Cast Class = To place the gems and rocks in the game screen
  def __init__
  def add_actor
  def get_actors
  def get_all_actors
  def remove_actor
  
  
Directing Folder
Director Class = control the sequence of play
  def __init__
  def start_game
  def _get_inputs
  def _do_updates
  def _do_outputs
  
Services Folder
  Keyboard services class = to detect player key presses and translate them into  a point representing a direction.
    def __init__
    def __init__
  
  Video_services class = to draw the game state on the screen. 
    def __init__
    def close_window
    def clear_buffer
    def draw_actor
    def flush_buffer
    def get_cell_size
    def get_height
    def get_width
    def is_window_open
    def open_window
    def _draw_grid
 
 Shared Folder
 Color class = Provide colors on the items
 point class = to hold and provide information about itself
    
