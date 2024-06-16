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
    def __init__(self, name: str, type: str):
        self.name = name

        # hobby, exercise, chore, etc
        self.type = type
        
        # flag for whether the user
        # wants to keep updating this activity
        # values: active, inactive
        self.status = 'active'

        # list of Activities
        self.activities = []

        # regularity
        string1 = '''How regularly will you update this topic?\n
                y: yearly\n
                m: monthly\n
                w: weekly\n
                d: daily\n
                i: irregularly'''
        valid_reg = False
        while not valid_reg:
            reg = input(prompt=string1).lower()
            if reg in ['y','m','w','d','i']:
                valid_reg = True
            else:
                print('That is not a valid option')

        self.reg = reg
        day_vals = []
        if reg in ['y','m','w','d']:
            
            done = False
            while not done:
                string2 = f'''Enter a day value on which you will update
                        this topic. These must be non-negative integers.\n

                        e.g. if regularity is w, then 0 = Monday.\n

                        If you are done entering values, enter "done".\n

                        So far, you have entered {day_vals}.'''
                
                day = input(prompt=string2)
                if day.lower() == 'done':
                    done = True
                else:
                    try:
                        day_int = int(day)
                    except ValueError:
                        print('Entered value is not an integer')
                        continue
                
                    if day_int < 0:
                        print('Entered integer must be non-negative.')
                        continue
                
                    day_vals.append(day_int)
            
        self.day_vals = day_vals



        
    
    def __repr__(self) -> str:
        return f'Topic({self.name}, {self.type}, {self.day_vals})'
    
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


        
        


