#!/usr/bin/python
# -*- coding: utf-8 -*-
# Apkdown
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Apkdown

import os, sys, time, random, requests, threading
import subprocess as sp
from time import sleep
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

info = """
Nama        : Apkdown
Versi       : 3.0 (Update: 12 Juli 2020, 1:00 AM)
Tanggal     : 01 Januari 2019
Author      : Nedi Senja
Tujuan      : Untuk mendonlot aplikasi
              seperti SIMONTOK
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: https://tinyurl.com/wel4alo

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;44;77;1m[           Apkdown, My Github: @stepbystepexe           ]\033[0m"""

logo = """
      \033[0;37m█▀▀▀█ █▀▀▀█ █   █    \033[0;90m█▀▀▀▄ █▀▀▀█ █  ▄  █ █▀▀▀█
      \033[0;37m█▀▀▀█ █▀▀▀▀ █▀▀▀▄    \033[0;90m█   █ █   █ █  █  █ █   █
      \033[0;37m▀   ▀ ▀     ▀   ▀ \033[0;32m▀  \033[0;90m▀▀▀▀  ▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀   ▀
"""

def restart():
      python = sys.executable
      os.execl(python, python, * sys.argv)
      curdir = os.getcwd()

def loads():
      o = [' .   ',' ..  ',' ... ']
      for i in o:
          print ('\r\033[0m[\033[0;31m●\033[0m] Sedang Mendownload'+i,end=''),;sys.stdout.flush();time.sleep(0.3)

def write(o):
      for i in o + '\n':
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.03)

def apkhome():
      os.system('clear')
      os.system('reset')
      sleep(1)
      print()
      print(logo)
      print(example)
      print()
      write("\033[0m[ \033[32mINFO \033[0m] \033[3mMendownload aplikasi secara berlebihan dapat")
      write("         Menyebabkan system (bug) rentan terhadap Virus\033[0m\n\n")

def home():
      os.system('clear')
      os.system('reset')
      sleep(1)
      print()
      print(logo)
      print(example)
      print()
      print("\033[0m[\033[1;96;2;1m1\033[0m] \033[1;77mhttps://m.apkpure.com")
      print("\033[0m[\033[1;96;2;1m2\033[0m] \033[1;77mhttps://apk-dl.com")
      print()
      print("\033[0m[\033[93;1m&\033[0m] LISENSI")
      print("\033[0m[\033[94;1m#\033[0m] Informasi")
      print("\033[0m[\033[92;1m*\033[0m] Perbarui")
      print("\033[0m[\033[91;1m-\033[0m] Keluar")
      print()
      option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
      if option.strip() in '1 apkpure'.split():
            write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
            sleep(1)
            apkpure()
            back = apkhome()
      elif option.strip() in '2 apkdl'.split():
            write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
            sleep(1)
            apkdl()
            back = apkhome()
      elif option.strip() in '& 3 lisensi'.split():
            print()
            os.system('nano LICENSE')
            print()
            restart()
      elif option.strip() in '# 4 info'.split():
            os.system('clear')
            print(example)
            os.system('toilet -f smslant Download')
            print(info)
            sleep(1)
            print()
            input('[ Tekan Enter ]')
            restart()
      elif option.strip() in '* 5 perbarui'.split():
            print()
            os.system('git pull origin master')
            print()
            input('\033[0m[ \033[32mTekan Enter \033[0m]')
            restart()
      elif option.strip() in '- 0 keluar'.split():
            print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
            print()
            sys.exit(1)
      else:
            print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
            print()
            sleep(1)
            restart()
      trd = threading.Thread(name='Donloder',target=download)
      trd.start()
      back
      print('\033[0mSabar yah Gan, bisa sambil ngupil dulu nunggunya, hehe :v\033[0m')
      print('\033[0mKalo lama berarti servernya lagi gax Fix, Error atau Down.\033[0m\n')
      while trd.isAlive():
            loads()
      back
      print('\n\033[0m[\033[1;96m#\033[0m] \033[77;1mMendownload Sukses\033[0m')
      print('Nama  : '+nm+'.apk')
      print('File  : Hasil/'+nm+'.apk')
      o = input('\n\033[0m[\033[1;95m?\033[0m] Download lagi [Y/n]: ')
      if o.strip() in ' Y y'.split():
            home()
      elif o.strip() in ' N n'.split():
            print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!\n")
            sys.exit(1)
      else:
            print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
            sleep(1)
            restart()

def apkpure():
      global link, nm, linkfile, size
      no = 0
      link = []
      judul = []
      developer = []
      e = "\033[0m"
      apkhome()
      sch = input('\033[0m[\033[103;90;1m Cari Apk \033[0m] ')
      print('\n\033[0;4mHasil pencarian aplikasi\033[0;36m '+sch.upper())
      print('\033[0m')
      req = Request('https://m.apkpure.com/id/search?q='+sch.replace(' ','+'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      for i in sup.find_all('a',attrs={'class':'dd'}):
            o = i.get('href')
            link.append(o)
      for x in sup.find_all('div',attrs={'class':'r'}):
            title = x.find('p',attrs={'class':'p1'})
            peng = x.find('p',attrs={'class':'p2'})
            judul.append(title.get_text())
            developer.append(peng.get_text())
      for jud, dev in zip(judul,developer):
            no += 1
            print(e,no,e+' Nama Aplikasi :'+e,jud[:20]+'..')
            print(e+'    Developer     : '+e+dev[:20]+'..'+e)
      print('\n\033[0m[\033[1;92m#\033[0m] \033[77;1mAplikasi ditemukan\033[0m')
      do = int(input('\n\033[0m[\033[1;93m+\033[0m] Pilih nomor: '))
      do = do - 1
      nm = input('\033[0m[\033[1;95m+\033[0m] Masukkan nama apk: ')
      write('\n\033[0m[\033[1;94m●\033[0m] \033[77;1mSedang memproses ...\033[0m')
      li = 'https://m.apkpure.com'+str(link[do])+'/download?from=details'
      re = Request(li,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      re = urlopen(re).read()
      sp = BeautifulSoup(re,'html.parser')
      donl = sp.find('div',attrs={'class':'fast-download-box'})
      down = donl.find('a',attrs={'class':'ga'})
      size = donl.find('span',attrs={'class':'fsize'})
      linkfile = down.get('href')

def apkdl():
      global link1, nm, linkfile, size
      no = 0
      link1 = []
      judul1 = []
      developer1 = []
      f = "\033[0m"
      apkhome()
      sch = input('\033[0m[\033[103;90;1m Cari Apk \033[0m] ')
      print('\n\033[0;4mHasil pencarian aplikasi\033[0;36m '+sch.upper())
      print('\033[0m')
      req = Request('https://apk-dl.com/search?q='+sch.replace(' ','%20'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      for i in sup.find_all('div',class_='card no-rationale square-cover apps small'):
            o = i.find('div', class_='details')
            x = o.find('a', class_='title')
            link1.append(x.get('href'))
            judul1.append(x.text)
            i = o.find('div',class_='subtitle-container')
            i = i.find('a')
            developer1.append(i.text)
      for jud, dev in zip(judul1,developer1):
            no += 1
            print(f,no,f+'  Nama Aplikasi :'+f,jud[:20]+'..')
            print(f+'     Developer     :  '+f+dev[:20]+'..'+f)
      print('\n\033[0m[\033[1;92m#\033[0m] Aplikasi ditemukan\033[0m')
      do = int(input('\n\033[0m[\033[1;93m+\033[0m] Pilih nomor: '))
      do = do - 1
      nm = input('\033[0m[\033[1;95m+\033[0m] Masukkan nama apk: ')
      write('\n\033[0m[\033[1;94m●\033[0m] \033[77;1mSedang memproses ...\033[0m')
      li = 'https://apk-dl.com/'+str(link1[do])
      re = Request(li,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      re = urlopen(re).read()
      sp = BeautifulSoup(re,'html.parser')
      donl = sp.find('div',class_='download-btn')
      down = donl.find('a')
      dons = down.get('href')
      rq = Request('http://apkfind.com'+dons,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rq = urlopen(rq).read()
      spq = BeautifulSoup(rq,'html.parser')
      dow = spq.find('div',class_='container-content')
      don = dow.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      rj = Request(don.get('href'),headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rj = urlopen(rj).read()
      sh = BeautifulSoup(rj,'html.parser')
      dowp = sh.find('div',class_='container-content')
      donr = dowp.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      linkfile = 'http:'+donr.get('href')

def download():
      try:
            os.mkdir('Hasil')
      except OSError:
            pass
      req = requests.get(linkfile, headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      with open('Hasil/'+nm+'.apk','wb') as dl:
            dl.write(req.content)

if __name__=='__main__':
      home()
