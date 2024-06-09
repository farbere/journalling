class Activity:
    def __init__(self):

class Topic:
    def __init__(self, name, type, interval = 'Daily'):
        self.name = name

        # hobby, exercise, chore, etc
        self.type = type

        # interval for updating
        # if e.g. "Monday" then will ask for
        # updates on Monday
        # if e.g. "Daily" then will ask for 
        # updates every day
        # if "Weekly" then checks if last 
        # update was more than a week ago
        # if "15" then will ask for
        # updates on 15th day of month

        self.interval = interval

        # flag for whether the user
        # wants to keep updating this activity
        # values: active, inactive
        self.status = 'active'

        # list of Activities
        self.activities = []
    
    # add activity
    def add_activity(self,):
