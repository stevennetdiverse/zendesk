from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here
class Ticket(models.Model):
    url = models.CharField(max_length=200)
    id = models.BigIntegerField(default=0)
    external_id = models.BigIntegerField(default=None)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    type = models.CharField(max_length=11)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=11)
    status = models.CharField(max_length=11)
    has_incidents = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    due_at = models.DateTimeField(default=None)
    tags = models.TextField()

    def __str__(self):
        return self.subject


class metric_set(models.Model):
    url = models.CharField(max_length=200)
    id = models.BigIntegerField(default=0)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    group_stations = models.IntegerField()
    assignee_stations = models.IntegerField()
    reopens = models.IntegerField()
    replies = models.IntegerField()
    assignee_updated_at = models.DateTimeField(default=timezone.now())
    requester_updated_at = models.DateTimeField(default=timezone.now())
    status_updated_at = models.DateTimeField(default=timezone.now())
    initially_assigned_at = models.DateTimeField(default=timezone.now())
    assigned_at = models.DateTimeField(default=timezone.now())
    solved_at = models.DateTimeField(default=timezone.now())
    latest_comment_added_at = models.DateTimeField(default=timezone.now())
    #agent_wait_time_in_minutes.calendar
    #agent_wait_time_in_minutes.business
    #requester_wait_time_in_minutes.calendar
    #requester_wait_time_in_minutes.business
    #on_hold_time_in_minutes.calendar


class Dates(models.Model):
    assignee_updated_at = models.DateTimeField(default=timezone.now())
    requester_updated_at = models.DateTimeField(default=timezone.now())
    status_updated_at = models.DateTimeField(default=timezone.now())
    initially_assigned_at = models.DateTimeField(default=timezone.now())
    assigned_at = models.DateTimeField(default=timezone.now())
    solved_at = models.DateTimeField(default=timezone.now())
    latest_comment_added_at = models.DateTimeField(default=timezone.now())
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class Individual(models.Model):
    id = models.BigIntegerField(default=0)
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    time_zone = models.CharField(max_length=200)
    iana_time_zone = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    shared_phone_number = models.CharField(max_length=200)
    locale_id = models.CharField(max_length=200)
    locale = models.CharField(max_length=200)
    organization_id = models.BigIntegerField()
    role = models.CharField(max_length=16)
    verified = models.BooleanField()
    external_id = models.BigIntegerField()
    alias = models.CharField(max_length=200)
    active = models.BooleanField()
    shared = models.BooleanField()
    shared_agent = models.BooleanField()
    last_login_at = models.DateTimeField(default=timezone.now())
    two_factor_auth_enabled = models.BooleanField(default=None)
    signature = models.CharField(max_length=200, default=None)
    details = models.CharField(max_length=200, default=None)
    notes = models.CharField(max_length=200, default=None)
    role_type = models.IntegerField()
    custom_role_id = models.BigIntegerField()
    moderator = models.BooleanField()
    ticket_restriction = models.CharField(max_length=200)
    only_private_comments = models.BooleanField()
    restricted_agent = models.BooleanField()
    suspended = models.BooleanField()
    default_group_id = models.BigIntegerField()
    report_csv = models.BooleanField()


class Submitter(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    submitter_id = models.ForeignKey(Individual, on_delete=models.CASCADE)


class Requester(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    requester_id = models.ForeignKey(Individual, on_delete=models.CASCADE)


class Assignee(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    assignee_id = models.ForeignKey(Individual, on_delete=models.CASCADE)


class Collaborator(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    collaborator_id = models.ForeignKey(Individual, on_delete=models.CASCADE)


class Group(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    id = models.BigIntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    default = models.BooleanField()
    deleted = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())


class Organization(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    id = models.BigIntegerField(default=0)
    name = models.CharField(max_length=200)
    shared_tickets = models.BooleanField()
    shared_comments = models.BooleanField()
    external_id = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    details = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    group_id = models.BigIntegerField(default=0)


class Comment(models.Model):
    id = models.BigIntegerField(default=0)
    type = models.CharField(max_length=27)
    author_id = models.BigIntegerField()
    body = models.TextField()
    public = models.BooleanField()
    audit_id = models.BigIntegerField()
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())


#only thing that matter is channel?
class Via(models.Model):
    channel = models.CharField(max_length=200)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=None)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)


class CustomFields(models.Model):
    value = models.CharField(max_length=200, default=None)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class Fields(models.Model):
    value = models.CharField(max_length=200, default=None)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class Follower(models.Model):
    follower_id = models.ForeignKey(Individual, on_delete=models.CASCADE)#?
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class FollowUp(models.Model):
    follow_up_id = models.ForeignKey(Individual, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)