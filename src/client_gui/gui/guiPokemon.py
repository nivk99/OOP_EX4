
from pygame import gfxdraw
import pygame
from pygame import *
import time

from src.client_gui.gui.button import Button


class GuiPokemon:
    """
    This is a class that draws the game of Pokemon.
   It can also be as a test between the taker and their algorithm
    """
    def __init__(self, clint) -> None:
        self._clint = clint
        self._graph = self._clint.get_graph()
        self._ttl = 0
        self._grade = 0
        self._moves = 0
        self.__run_pygame()

    # ran pygame
    def __run_pygame(self) -> None:
        # init pygame
        WIDTH, HEIGHT = 1080, 720
        pygame.init()
        screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        clock = pygame.time.Clock()
        pygame.font.init()

        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        # load the json string into SimpleNamespace Object

        # get data proportions
        min_x = min(list(self._graph.get_all_v().values()), key=lambda n: n.getLocation().get_x()).getLocation().get_x()
        min_y = min(list(self._graph.get_all_v().values()), key=lambda n: n.getLocation().get_y()).getLocation().get_y()
        max_x = max(list(self._graph.get_all_v().values()), key=lambda n: n.getLocation().get_x()).getLocation().get_x()
        max_y = max(list(self._graph.get_all_v().values()), key=lambda n: n.getLocation().get_y()).getLocation().get_y()

        def scale(data, min_screen, max_screen, min_data, max_data) -> float:
            """
            get the scaled data with proportions min_data, max_data
            relative to min and max screen dimentions
            """
            return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

        # decorate scale with the correct values

        def my_scale(data, x=False, y=False) -> float:
            if x:
                return scale(data, 50, screen.get_width() - 50, min_x, max_x)
            if y:
                return scale(data, 50, screen.get_height() - 50, min_y, max_y)

        radius = 15
        arr = self._clint.Start_mode()
        for i in range(self._clint.sum_agents()):
            if i >= len(arr):
                self._clint.add_agent(0)
                continue
            self._clint.add_agent(arr[i])

        # the stop pygame
        b = Button('stop', (70, 50), font=FONT)
        b.add_click_listener(lambda: self._clint.stop())

        # this commnad starts the server - the game is running now
        self._clint.start()
        # self._clint.move()
        self._clint.move()
        """
        The code below should be improved significantly:
        The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
        """
        while self._clint.is_running() == 'true':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            # refresh surface
            screen.fill(Color(255, 255, 255))

            # draw nodes
            for n in self._graph.get_all_v().values():
                x1: float = (n.getLocation().get_x())
                y1: float = (n.getLocation().get_y())
                x = my_scale(x1, x=True)
                y = my_scale(y1, y=True)

                # its just to get a nice antialiased circle
                gfxdraw.filled_circle(screen, int(x), int(y),
                                      radius, Color(64, 80, 174))
                gfxdraw.aacircle(screen, int(x), int(y),
                                 radius, Color(255, 255, 255))

                # draw the node id
                id_srf = FONT.render(str(n.getKey()), True, Color(255, 255, 255))
                rect = id_srf.get_rect(center=(x, y))
                screen.blit(id_srf, rect)

            # draw edges
            for v in self._graph.get_all_v():
                for e in self._graph.all_out_edges_of_node(v).keys():
                    # scaled positions
                    src_x = my_scale(self._graph.get_all_v()[v].getLocation().get_x(), x=True)
                    src_y = my_scale(self._graph.get_all_v()[v].getLocation().get_y(), y=True)
                    dest_x = my_scale(self._graph.get_all_v()[e].getLocation().get_x(), x=True)
                    dest_y = my_scale(self._graph.get_all_v()[e].getLocation().get_y(), y=True)

                    # draw the line
                    pygame.draw.line(screen, Color(61, 72, 126),
                                     (src_x, src_y), (dest_x, dest_y))

            agents = self._clint.get_agents()
            pokemos = self._clint.get_pokemon()

            # draw agents
            for agent in agents:
                x = my_scale(agent.get_pos().get_x(), x=True)
                y = my_scale(agent.get_pos().get_y(), y=True)
                pygame.draw.circle(screen, Color(0, 0, 0),
                                   (int(x), int(y)), 10)
                # draw the agent id
                id_srf = FONT.render(str(agent.ged_id()), True, Color(255, 255, 255))
                rect = id_srf.get_rect(center=(x, y))
                screen.blit(id_srf, rect)

            # draw Time
            self._ttl = int(float(self._clint.time_to_end()) / 1000)
            time_but = Button("Time " + str(self._ttl), (70, 50), font=FONT)
            time_but.render(screen, (screen.get_width() / 12, screen.get_height() / 60))

            # draw Grade
            self._grade = self._clint.sum_grade()
            grade_but = Button("Grade " + str(self._grade), (70, 50), font=FONT)
            grade_but.render(screen, (screen.get_width() / 6, screen.get_height() / 60))

            # draw moves
            self._moves = self._clint.sum_moves()
            moves_but = Button("moves " + str(self._moves), (70, 50), font=FONT)
            moves_but.render(screen, (screen.get_width() / 4, screen.get_height() / 60))

            # draw stop
            b.render(screen, (screen.get_width() / 1.1, screen.get_height() / 60))
            b.check()
            # draw the pokemon
            for p in pokemos:
                x11 = my_scale((p.get_pos().get_x()), x=True)
                y11 = my_scale((p.get_pos().get_y()), y=True)
                #  draw the pokemon: if: src < dest => type > 0
                if int(p.get_type()) == 1:
                    pygame.draw.circle(screen, Color(0, 0, 255), (int(x11), int(y11)), 10)
                #  draw the pokemon: if: dest < src => type < 0
                if int(p.get_type()) == -1:
                    pygame.draw.circle(screen, Color(250, 1, 1), (int(x11), int(y11)), 10)

            # update screen changes
            display.update()

            # refresh rate
            clock.tick(60)
            # choose next edge
            for agent in agents:
                if agent.get_dest() == -1:
                    self._clint.algo(self._graph, pokemos, agents)
                    next_node = agent.next_node()
                    if next_node == agent.get_src():
                        next_node = agent.next_node()
                    self._clint.choose_next_edge(agent.ged_id(), next_node)
                    print(GuiPokemon.__repr__(self))
            time.sleep(self._clint.sleep_time(agents))
            self._clint.move()
        # game over:

    def __repr__(self) -> str:
        return f"Time: {self._ttl}, Grade: {self._grade}, Moves: {self._moves}"
