from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager

class UserContent(models.Model):
    """Any data that is contributed by one or more Users
    """
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    #contributors = models.ManyToManyField('User', related_name='content')

class ReviewFlag(models.Model):
    type   = models.CharField(max_length=20)
    value  = models.DecimalField(max_digits=3, decimal_places=0)
    review = models.ForeignKey('Review', related_name='flags')

    def __unicode__(self):
        return 'ReviewFlag({}, {})'.format(self.type, self.value)

class Review(UserContent):
    """Defines a Review performed by a user.

    A review can be associated with any type that derrives from Reviewable.
    """
    reviewable = models.ForeignKey('Reviewable', related_name='reviews')
    comments   = models.TextField()

    def __unicode__(self):
        return 'Review({})'.format(self.reviewable)

class Reviewable(UserContent):
    """Defines an item that can be reviewed by a user.
    
    Everything that the user can edit should derive from this type.
    
    This is the mechanism by which we ensure that the data that we provide
    is accurate.  If a user notices an issue with a 'Reviewable' Item,
    they can flag it to be reviewed later, or perhaps even make the
    nessecary change themselves.  Of course, all changes must be reviewed
    before they make it to the main page
    """
    class_name = models.CharField(max_length=20, editable=False)
    
    def __init__(self, *args, **kwargs):
        super(Reviewable, self).__init__(*args, **kwargs)
        if not self.pk and not self.class_name:
            self.class_name = self.CLASS_NAME

    def __unicode__(self):
        return getattr(self, self.class_name).__unicode__()

class Bill(Reviewable):
    """Defines a bill
    """
    CLASS_NAME = 'bill'
    
    name    = models.CharField(max_length=36)
    summary = models.TextField()
    
    def __unicode__(self):
        return 'Bill({})'.format(self.name)

class CongressPerson(Reviewable):
    CLASS_NAME = 'congressperson'

    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)

    def __unicode__(self):
        return 'CongressPerson({}, {}.)'.format(self.last_name, self.first_name[0])
