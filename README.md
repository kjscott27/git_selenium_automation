#Description
Github has added a button for marking files as read. I work often with Apollo and GraphQL where we are auto generated files and I want to auto mark these files as viewed as they're generated and reviewing them is pointless.

#TODO:
* Authentication of some kind
    * This is going to require a piece of research as I don't think using a username and password is a good idea from the user perspective. Some kind of a key with read-only permissions and SSO would be ideal.
* Get selenium to click all of the read options for __GENERATED__ files only
    * Need to check that this viewed option isn't some kind of asynchronous API on Github's end or something