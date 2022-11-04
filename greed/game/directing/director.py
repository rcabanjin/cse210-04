class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0 # for the computation of score
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        banner = cast.get_first_actor("banners")
        banner2 = cast.get_first_actor("banners2") # added
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("Score: "+str(self.score))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if robot.get_position().equals(artifact.get_position()):
                # conditions if gems(*) are hit. with corresponding scores based on font size
                if artifact.get_text() == '*' and artifact.get_font_size() == 15:
                    self.score += 1
                    artifact.set_text("")
                elif artifact.get_text() == '*' and artifact.get_font_size() == 20:
                    self.score += 3
                    artifact.set_text("")
                elif artifact.get_text() == '*' and artifact.get_font_size() == 25:
                    self.score += 5
                    artifact.set_text("")
                # else condition when rocks(O) are hit with corresponding deduction of score based on font size
                else:
                    if self.score == 0:
                        self.score = 0
                        artifact.set_text("")
                    else:
                        if artifact.get_font_size() == 15:
                            self.score -= 1
                            artifact.set_text("")
                        elif artifact.get_font_size() == 20:
                            self.score -= 3
                            artifact.set_text("")
                        elif artifact.get_font_size() == 25:
                            self.score -= 5
                            artifact.set_text("")
                # message = artifact.get_message()
            banner2.set_text(chr(self.score))
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()