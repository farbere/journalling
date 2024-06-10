import datetime
class Activity:
    # an activity is an instance of engaging with a topic
    # each activity should have the following information:
    # date
    # duration (minutes)
    # description
    # def __init__(self, date=None, mins_dur=None, description=None):
    #     self.date = datetime.date.today() if date is None else date
    #     self.mins_dur = 0 if mins_dur is None else mins_dur
    #     self.description = '' if description is None else description
    
    def __init__(
            self,
            date: datetime.date = datetime.date.today(),
            mins_dur: int = 0,
            description: str = ''
        ):
        self.date = date
        self.mins_dur = mins_dur
        self.description = description

    def change_date(self, date: datetime.date) -> None:
        self.date = date
    
    def change_duration(self, dur: int) -> None:
        self.mins_dur = dur

    def change_description(self, description: str) -> None:
        self.description = description
    
    def __repr__(self) -> str:
        return f'Activity({self.date}, {self.mins_dur}, {self.description[:20]}...)'

class Topic:
    def __init__(self, name: str, type: str, interval: str = 'Daily'):
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
    
    def __repr__(self) -> str:
        return f'Topic({self.name}, {self.type}, {self.interval})'
    
    # add activity
    def add_activity(
            self,
            date: datetime.date = datetime.date.today(),
            duration: int = 0
        ):

        # description instantiated as empty string
        act = Activity(date, duration)

        description = input('Describe the activity.')
        act.change_description(description)

        self.activities += [act]


        
        


