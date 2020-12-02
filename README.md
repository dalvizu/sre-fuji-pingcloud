# SRE Mt Fuji - PingCloud

This is a take-home programming assignment as part of the Ping Identity interview
process. This consists of a coding problem and a two-part DevOps problem.

This whole problem is intended to take 8-16 hours, and we typically encourage this to be
done over the weekend. Please direct any questions to your Ping contact.

## Coding Problem:

As SRE engineer, you are building the pipeline out to production. Ping's
Support group has asked to be notified when a pipeline starts, and wants to
have its JIRA issue tracking system updated.

When the Pipeline starts, you'll have access to a set of git commits,
containing a commit message, sha, authorship. An example git commit:

```
commit 55c0bb88b6e4f096574991dd9217bcf8c745d05e
Author: Example User <example@pingidentity.com>
Date:   Mon May 4 17:09:19 2015 -0600

    SSD-101 super duper feature
    Fix tomcat issue with using forks over spoons.
```

These git commits will be provided as a `GitCommit` object by another program.

Your assignment is to write a method which returns the "issue key" in this commit: `SSD-101`,
and a general solution to return all of the issue keys present in any git commits provided.

Basically, implement this function: [App#get_jira_tickets()](https://github.com/dalvizu/sre-fuji-pingcloud/blob/master/fuji/app.py#L17)

_Note_: The string 'SSD-101' is the 'key' of a JIRA issue. JIRA is a popular ticketing system in
software development and common in the open source community. The key of an issue is its project
name (`SSD`) followed by a hyphen and then a number (`101`). For more information on what an issue
is, see [what is an issue?](https://confluence.atlassian.com/jira064/what-is-an-issue-720416138.html)

This method and the supporting domain objects have been provided in the `fuji/` folder, which follows
a [standard python module layout](https://realpython.com/pipenv-guide/#package-distribution).
The goal of this layout is to provide an 'App' object which other python programs can use.

If you have any questions, feel free to ask through your Ping contact. You'll be asked to present your 
solution to an interview panel of engineers and argue for any decisions you're making, so be prepared
to discuss your solution. Remember to document any assumptions you may be making.

While this is a standard layout and uses standard libraries, feel free to use any modules you feel 
like and structure this any way you like. Be prepared to discuss your reasoning in the panel interview.

## DevOps problem

### Docker problem

Containerize your solution in a Docker container. The container should be able to run both your
tests and the main application by running different commands

* create a Dockerfile
* provide instructions for how to build and run it.
 

### AWS problem

You have been provided an AWS IAM credential and a region to use in AWS. Please do not leave this region, 
as we need clean up resources after the interview is done.

The problem is to take to take the python problem solution and place an archive of it in a public website.
Create this website,  registered under a domain name of your choosing, using the most appropriate technology
you can think of.

This website must include a zipped archive of your repo with any instructions you wish to provide about how
to use or evaluate your submission.

Please ensure this is not searchable by a search engine.

Note your website is not required to run any python code or have any sort of API. We just want to
see how you work with AWS, how you'd build a website with AWS, and how you'd hand off a completed
project for others to read and use.

Fancy HTML not required.

An infrastructure as code solution is required, using a technology of your choice.

**NOTE** You will not be able to create or modify any IAM resources in this account.

## Required Tools

* git
* python3
* pipenv
* docker

### Tool installation

* You're assumed to be familiar with git and python. For pipenv -- follow instructions at 
  [https://pipenv.kennethreitz.org/](https://pipenv.kennethreitz.org/)

* Use Python 3.7

* Some conveniences have been provided for you.

* To run from command line:
  ```
  python main.py
  ```

* To run unit tests:
  ```
  pytest
  ```

## Submitting:

To submit your answer, create a private repository and email that and any instructions for your final submission.
Please do not place any solution in a public git repository or anywhere discoverable by a search engine,
as we want to be able to re-use this test.
