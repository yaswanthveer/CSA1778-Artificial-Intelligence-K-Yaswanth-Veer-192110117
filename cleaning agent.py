print("K Yaswanth Veer 192110117")

class Reflex_Cleaning_Agent:
    def _init_(self, _location, _enviroment):
        self.my_enviroment = _enviroment
        self.location = _location
        self.room_a_is_dirty = True
        self.room_b_is_dirty = True
        self.my_state = []
        self.initialize(self.location)
    def Run(self):
        if self.my_state[1] == 'dirty':
            self.clean(self.location)
        elif self.location == "room-A":
            self.go_right_room()
        elif self.location == "room-B":
            self.go_left_room()
    def clean(self, _location):
        if _location == 'room-A':
            self.my_enviroment[0] = [str(_location), 'clean']
            self.room_a_is_dirty = False
            self.my_state = [str(_location), 'clean']
        if _location == 'room-B':
            self.my_enviroment[1] = [str(_location), 'clean']
            self.room_b_is_dirty = False
            self.my_state = [str(_location), 'clean']
        print(_location, "is cleaned.")
    def go_right_room(self):
        self.room_a_is_dirty = False 
        self.location = self.my_enviroment[1][0] 
        self.my_state = self.my_enviroment[1]
        print("Room A was clean, therefore robot went to the right room.")
    def go_left_room(self):
        self.room_b_is_dirty = False  
        self.location = self.my_enviroment[0][0] 
        self.my_state = self.my_enviroment[0]
        print("Room B was clean, therefore robot went to the left room.")
    def initialize(self, _location):
        for room in self.my_enviroment:
            if room[0] == _location:
                self.my_state = room
        print("Robot is in the", self.my_state[0])
    def Run_Until_Everywhere_Is_Clean(self):
        while self.room_a_is_dirty or self.room_b_is_dirty:
            self.Run()
        print("Every room is clean.")
    def Return_Enviroment(self):
        return self.my_enviroment
class main:
    def _init_(self):
        my_enviroment = [['room-A', 'dirty'], ['room-B', 'clean']]
        location = 'room-A'
        reflex_agent = Reflex_Cleaning_Agent(location, my_enviroment)
        reflex_agent.Run_Until_Everywhere_Is_Clean()
main()
