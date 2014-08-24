Developers
==========

Getting Started
---------------
crowd.ed is hosted on Github, but all of our development is done via Gerrit.  Gerrit is a code
review tool developed by Google for the Android Operating System Project, and offers a much more
powerful code control mechanism than Github.  Gerrit is used by many open projects, and has already
been well documented, so we won't get into that here.  If you'd like to learn more about
Gerrit, check out this site.

.. todo::
   Add link to gerrit site.

Project Setup
^^^^^^^^^^^^^
To get going on the code, you'll first need to set up an account at 
`gerrithub.io <http://gerrithub.io/>`_.  The
site uses your Github credentials, so if you don't already have an account with them, you'll
need to `sign up <https://github.com/join>`_ there as well.  During the sign-up process, you'll be
asked if you want to import your Github repositories.  Importing repositories is completely
optional, but doing so will let you use Gerrit with you other projects.

Once you have your gerrithub account set up, you can clone the project by executing the two-part
command below (substituting *<gerrithub username>* with your username)::
  
  git clone ssh://<gerrithub username>@review.gerrithub.io:29418/montaguk/crowd.ed && scp -p -P 29418 <gerrithub username>@review.gerrithub.io:hooks/commit-msg crowd.ed/.git/hooks/

The first command will clone the crowd.ed source code, and the second will set up a git-commit hook
that generates a unique *Change Id* for each commit.  This ID is used by Gerrit to track a specific
change across cherry-picks and rebases.  For more details on this mechanism, see the
`Gerrit Documentation <https://gerrit-documentation.storage.googleapis.com/Documentation/2.9/index.html>`_.

Making a Change
^^^^^^^^^^^^^^^
Once you have the repo set up, you're ready to start making changes!  Go ahead and modify the
code to your hearts desire.  Once you are satisfied with your changes, commit them to your local
repository as you normally would::

  git commit -a

Once that is done, you'll need to submit your changes to Gerrit for review.  To do this, run the
following command (substituting *<branch name>* with the target branch)::

  git push origin HEAD:refs/for/<branch name>

In most instances, the target branch will be **master**, but this will likely depend on the nature
of the change.

Now you just sit tight and wait for someone to review your change on gerrithub.  You can view the
status of your pending review by selecting your review from the *Outgoing reviews* list 
`here <https://review.gerrithub.io/#/dashboard/self>`_.  While your waiting for someone to review
your change, why not make some comments on another change!

Reviewing Changes
^^^^^^^^^^^^^^^^^
Every registered user has the ability to review a change.  You may comment on the change and give
it either a +1 or a -1 vote.  Only *project integrators* have the ability to give a +2 or -2 vote.
In order for a change to make it to the target branch, it must receive at least one +2 review.  If
a change receives a -2 review, that change is cannot ever be merged into the target branch.  See
`this page <http://gerrit-review.googlesource.com/Documentation/config-labels.html>`_ for more
details on the Gerrit scoring system.  ..note:: gerrithub only supports the *Review* and *Verified*
labels.

Verifying Changes
^^^^^^^^^^^^^^^^^
For a change to be submitted to the target branch, it must first be marked as verified.  Normally,
pushing to HEAD:refs/for/* would cause a CI server to build the proposed changes automatically,
but gerrithub does not currently support this.  As the project grows we would like to move towards
a fully automated continuous integration implementation, but for now changes must be verified
manually.

Submitting Changes
^^^^^^^^^^^^^^^^^^
Once your change has received a "Reviewed: +2" and a "Verified: +1", it will then be submitted
to the target branch.  When requested, a submit will cause Gerrit to merge the change into the
target branch, and sync the change back to the repo on Github.  At this point, Github triggers
a continuous integration build on `drone.io <https://drone.io/github.com/montaguk/crowd.ed>`_.

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^
crowd.ed uses `drone.io <https://drone.io>`_ CI builds to monitor the state of each branch.
This helps us to catch any issues/bugs with the code as soon as they are introduced, and ideally
prevent them from making their way into the code in the first place.  Since gerrithub is currently
limited in its implementation, our current CI situation is not ideal.  Perhaps one day we'll have
the resources to manage our own Gerrit server, but for now we'll just have to make due.

Documentation
^^^^^^^^^^^^^
The majority of crow.ed is written in python, and uses `Sphinx <http://sphinx-doc.org/>`_ to
document the code.  The docs are hosted on `ReadTheDocs <http://crowded.readthedocs.org/en/latest/#>`_
and are rebuilt each time master is updated.  When making changes to the code, we request that
you also make the necessary changes to the documentation, as one of our goals is to keep the
code-base as easy to maintain as possible.  Sphinx tracks what percentage the code is documented,
and we'd like to see that number stay as high as possible.

Testing
^^^^^^^
In order to fully utilize the benefits of continuous integration, we use a couple different testing
frameworks.  The web code is tested using Django's built in testing framework, while we use
the python *nosetest* package to test non-web code (scrapers, API interfaces, etc).  If you're
adding new tests, make sure to add the appropriate calls to build.sh, which is the script that
drives the CI build.
