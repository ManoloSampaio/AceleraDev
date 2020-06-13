from django.db import models

class User(models.Model):
    name = models.CharField('name',max_length=50)
    last_login = models.DateField('last_login',auto_now=True)
    email = models.CharField('email',max_length=254)
    password = models.CharField('password',max_length=50)

class Agent(models.Model):
    name = models.CharField('name',max_length=50)
    status = models.BooleanField('status')
    env = models.CharField('env',max_length=20)
    version = models.CharField('version',max_length=5)
    address = models.CharField('adress',max_length=39)


class Event(models.Model):
    level = models.CharField('level',max_length=20)
    data = models.TextField('Data')
    arquivado = models.BooleanField('arquivado')
    date = models.DateField('date',auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField('name',max_length=50)


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
