import datetime
import fuji
from fuji import App
from fuji import GitCommit
app = App()

# I should print ['SSD-101']
if __name__ == '__main__':

    ticket = GitCommit("7bdf804ae1e659a19a499f21a1551f00dbc7f868",
                       "Dan Alvizu <dalvizu@pingidentity.com>",
                       "SSD-101 I made a ticket!",
                       datetime.datetime.now())
    print(app.get_jira_tickets([ticket]))
