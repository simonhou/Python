#!/usr/bin/python
#-*- coding:utf8 -*-
#
#  Author      : hackergodness
#  Email       : houjun612@gmail.com
#  Descsription: A simple script to access Github API.
#              
#


import github

def main():
    gh = github.GitHub() # Initialize
    lists_dic = {}
    statis = {}
    username = raw_input('Please input username:') 
    repos_lists = gh.users(username).repos.get() # Get all the repos name
    for repo in repos_lists:
        lists_dic[repo.name] = repo.language  # Get the language of specified repos

    language_name_lists = lists_dic.values()

    for name in language_name_lists:
        if statis.has_key(name) == False:
            statis[name] = 1
        else:
            statis[name] = statis[name] + 1   # Count the number of one language
    print statis 


if __name__ = = "main":
    main()