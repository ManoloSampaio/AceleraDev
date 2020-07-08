from api.models import User, Agent, Event, Group
import datetime as dt

def get_active_users() -> User:
    delta = dt.timedelta(days = 10)
    User.objects.filter()
    return User.objects.filter(last_login__lte=dt.date.today(),
                               last_login__gte=dt.date.today()-delta)


def get_amount_users() -> User:
    user_number = User.objects.all().count()
    return user_number

def get_admin_users() -> User:
    return User.objects.filter(group__name='admin')

def get_all_debug_events() -> Event:
    return Event.objects.filter(level='debug')
    

def get_all_critical_events_by_user(agent_made) -> Event:
    return Event.objects.filter(level='critical',
                                agent=agent_made)

def get_all_agents_by_user(username) -> Agent:
    return Agent.objects.filter(user__name=username)


def get_all_events_by_group() -> Group:
    return Group.objects.filter(user__agent__event__level
                                ='information')

