# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from gtts import gTTS
import urllib
import urllib2
import urllib3
import requests
import wikipedia
import goslate
from bs4 import BeautifulSoup
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from threading import Thread
from pyowm import OWM

cl = LINETCR.LINE()
cl.login(token="EnQcRQh5qNcc6SRZOk1b.VHH0q0Dhr8pSns5/+RsmgW.ByD5LqWI3VlNICrUhqkfaXYIEouZ1XA+Vi7MGRS5Z+I=")
cl.loginResult

kk = LINETCR.LINE()
kk.login(token="EnJETWHEB6WS53xWBhyd.UvZQ8iaX1kDhGbAShThZ3q.UJETGlvztGIcR+Cf+2hf0G0Jtw6uy4Z4eO/X9gxxGG0=")
kk.loginResult

ki = LINETCR.LINE()
ki.login(token="EnM1lVb9dGNBr5yVzP53.b151yOadpUwvZ3Q/9r80aW.uGMAEOXf6tV7IY+HLpmwkvwGWRkcHvCt84TFeLQ9DU0= ")
ki.loginResult

kc = LINETCR.LINE()
kc.login(token="En6vsH5b0qVPtS1Tl9g8.bfmfUwtccO+1N7EuVwD+Ma.Th6h1SUJHS0EE/rAC0cj9eenke1132oNqGcSBi11kfw=")
kc.loginResult

print "Login Suscess"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""Bot Command
========================
> Hi
> Creator
> Me
> Gift
> Ginfo
> Welcome
> Cancel
> Tagall
> pp @
> cover @
> Kedapkedip (Text)
> /apakah (Pertanyaan)
> Rate (Penilaian)
> /translate-en
> /translate-id
> /set
> /check
> /lagu (Contoh) : /lagu iwan fals ibu #
> /lirik (Contoh) : /lirik Payung teduh Akad #
> /ig  (Contoh) : /ig dekaprabowoo #
> /Youtube (Contoh) : /youtube young dumb & broke #
> /status
> Ambilkan @ Steal dp target
> Sampul @ Steal cover target
> Copy @ All bot copy target
> Keluar @ target
> music
> .lyric
> .instagram
> .Youtube
> .reboot
> Rutime
> Pahala @
> Dosa @
========================
========================
    Status Group
========================
> contact on/off
> join on/off
> leave on/off
> protect on/off
> qr on/off
> invite on/off
> cancel on/off
========================
========================
 Command Creator & Admin
========================
> Admadd @
> Admrem @
> Adminlist
> InviteMeTo:
> Kawan | join
> Invite (Mid)
> Gcreator:inv
> /spam (jumlah) (text)
> apakabar (Meratakan)
========================
     Command Mimic
========================
> Mimic:on
> Mimic:add: @
> Mimic:del: @
> ListTarget"""

KAC=[cl,ki,kk,kc]
DEF=[ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Amid,Bmid,Cmid]
admin = ["ube187443474747c3ec352e7efeb48c1b"]
owner = ["ube187443474747c3ec352e7efeb48c1b"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Terima Kasih Sudah Add, Salken Ya :)",
    "lang":"JP",
    "comment":"Jangan Lupa Like Back",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":True,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":True,
    "protectionOn":True,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    "atjointicket":True,
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kd.getGroup(op.param1)
				    except:
					try:
                                            G = ke.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kd.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Nama Grup dikunci")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wkwkkww mampus")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 17:
                group = random.choice(DEF).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = random.choice(DEF).getContact(op.param2).displayName + " [NewMemb]\n\nSelamat Datang" + random.choice(KAC).getContact(op.param2).displayName + " di [" + group.name + "]\nJGN NAKAL OK!!" + "\n\nCreator => " + group.creator.displayName
                random.choice(DEF).sendMessage(cb)
        if op.type == 15:
            if op.param2 in Bots:
                return
            kc.sendText(op.param1, "Dia Ga Betah, Yah Tenang Ya Hidupnya")
            print "MemberLeft"

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Jmid:
                        X = kj.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kj.updateGroup(X)
                        Ti = kj.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Nmid:
                        G = kn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)

                if op.param3 in Nmid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)

                if op.param3 in Omid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                if op.param3 in Pmid:
                    if op.param2 in Qmid:
                        X = kq.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                        kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                if op.param3 in Qmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                if op.param3 in Rmid:
                    if op.param2 in Smid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Smid:
                    if op.param2 in Tmid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                if op.param3 in Tmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki,kk,kc]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki,kk,kc]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki,kk,kc]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,kk,kc]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ticket = kd.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kf.updateGroup(X)
                    Ticket = kf.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kg.updateGroup(X)
                    Ticket = kg.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kj.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ticket = kh.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kj.updateGroup(X)
                    Ticket = kj.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ti = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kn.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Omid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kp.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ticket = ko.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kq.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kq.updateGroup(X)
                    Ti = kq.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kp.updateGroup(X)
                    Ticket = kp.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Qmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kr.updateGroup(X)
                    Ti = kr.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kq.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kq.updateGroup(X)
                    Ticket = kq.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Rmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    Ticket = kr.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Smid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = ks.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Tmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kt.updateGroup(X)
                    Ticket = kt.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    #cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","key","ked list"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: "," ")
                klist=[kt,ks,kr,kq,kp,ko,kn,kj,kh,kg,kf,ke,kd,kc,kk,ki,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: "," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#---------------------------- SPAM CHAT -------------------------------------
            elif "/spam " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace("/spam " + str(jmlh) + " ","")
                    if jmlh <= 999:
                        for x in range(jmlh):
                            cl.sendText(msg.to,teks)
#----------------------------------------------------------------------------
#---------------------------- CHANGE GROUP NAME -----------------------------
            elif "/gn " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("/gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
#----------------------------------------------------------------------------
#-------------------------------- MID ---------------------------------------
            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------- CREATOR ------------------------------------
            elif msg.text.lower() in ["creator","admin"]:
                msg.contentType = 13
                adm = 'ube187443474747c3ec352e7efeb48c1b'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Instagram : @dekaprabowoo\nJodiak : Taurus\nHubungan : Sedang Menjalani")
#----------------------------------------------------------------------------
#--------------------------------- GIFT -------------------------------------
            elif msg.text.lower() in ["gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------ CANCEL PENDING ------------------------------
            elif msg.text.lower() in ["cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ OPEN URL ------------------------------------
            elif msg.text.lower() in ["ourl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ CLOSE URL -----------------------------------
            elif msg.text.lower() in ["curl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GET GROUP LINK ------------------------------
            elif  msg.text.lower() in ["gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,x.name + " : line://ti/g/" + gurl)
                    print "[Command] Get Grup Link"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GROUP INFO ----------------------------------
            elif msg.text.lower() in ["ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"「 Grup Name 」 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n「 Grup Creator 」 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nTotal Anggota : " + str(len(ginfo.members)) + " Orang\nPending : " + sinvitee + " Orang")#URL : " + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"「 Grup Name 」 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n「 Grup Creator 」 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Grup Only Boy")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#---------------------------------- MID -------------------------------------
            elif msg.text.lower() in ["mid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)
#----------------------------------------------------------------------------
            elif msg.text in ["Wkwk","wk","wkwkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","eh","hehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Galak","galak"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["You","kamu","Kamu"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh","hadeh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Please","Hati"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Haaa","apaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Lol","ngakak","Ngakak"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
#------------------------------ CHANGE NAME ---------------------------------
            elif "/cn " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/cn ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        ki.updateProfile(profile)
                        kc.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------
#------------------------------ CHANGE BIO ----------------------------------
            elif "/bio " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        kk.updateProfile(profile)
                        ki.updateProfile(profile)
                        kc.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------                    
            elif msg.text.lower() in ["contact on"]:
                if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")

            elif msg.text.lower() in ["contact off"]:
                if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")

            elif msg.text.lower() in ["join on"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")

            elif msg.text.lower() in ["join off"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")

            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text.lower() in ["leave on"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")

            elif msg.text.lower() in ["leave off"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")

            elif msg.text.lower() in ["protect on"]:
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")

            elif msg.text.lower() in ["protect off"]:
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")

            elif msg.text.lower() in ["qr on"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")

            elif msg.text.lower() in ["qr off"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")

            elif msg.text.lower() in ["invite on"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")

            elif msg.text.lower() in ["invite off"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")

            elif msg.text.lower() in ["cancel on"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")

            elif msg.text.lower() in ["cancel off"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
#------------------------------ STATUS BOT ----------------------------------
            elif "/status" in msg.text.lower():
                md = ""
                if wait["contact"] == True: md+="[*] Contact : on\n"
                else: md+="[*] Contact : off\n"
                if wait["autoJoin"] == True: md+="[*] Auto join : on\n"
                else: md +="[*] Auto join : off\n"
                if wait["leaveRoom"] == True: md+="[*] Auto leave : on\n"
                else: md+="[*] Auto leave : off\n"
                if wait["autoAdd"] == True: md+="[*] Auto add : on\n"
                else:md+="[*] Auto add : off\n"
                if wait["protect"] == True: md+="[*] Protect : on\n"
                else:md+="[*] Protect : off\n"
                if wait["linkprotect"] == True: md+="[*] Link Protect : on\n"
                else:md+="[*] Link Protect : off\n"
                if wait["inviteprotect"] == True: md+="[*] Invite Protect : on\n"
                else:md+="[*] Invite Protect : off\n"
                if wait["cancelprotect"] == True: md+="[*] Cancel Protect : on"
                else:md+="[*] Cancel Protect : off"
                cl.sendText(msg.to,md)
#----------------------------------------------------------------------------

            elif msg.text in ["Ruqyah"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Dasar Laknat")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "apakabar" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("apakabar","")
                    klist=[cl,ki,kk,kc]
                    kicker = random.choice(klist)
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    kicker.sendText(msg.to,"Virus!")
                    kicker.sendText(msg.to,"Maaf!")
                    kicker.sendText(msg.to,"Kami Sopan!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                               klist=[cl,ki,kk,kc]
                               kicker = random.choice(klist)
                               kicker.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Iyaaaaaaaa")
                                kk.sendText(msg,to,"Hajaaaar")
                            pass
#---------------------------- GROUP ID / LIST--------------------------------
            elif msg.text.lower() in ["/grup id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)

            elif msg.text.lower() in ["/list grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s \n" % (cl.getGroup(i).name + " : " + str(len(cl.getGroup(i).members)) + " Members")
                    cl.sendText(msg.to,"「List Group」\n" + h + "Total Group : " + str(len(gid)))

            elif msg.text in ["Glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = kk.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kk.getGroup(i).name + " | [ " + str(len (kk.getGroup(i).members)) + " ]")
                kk.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = kc.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kc.getGroup(i).name + " | [ " + str(len (kc.getGroup(i).members)) + " ]")
                kc.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
#----------------------------------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    kk.cloneContactProfile(target)
                                    kc.cloneContactProfile(target)
                                    kd.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#------------------------------ CANCEL GROUP --------------------------------
            elif msg.text.lower() in ["cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Done")
                else:
                    cl.sendText(msg.to,"Nothing invite.")
#----------------------------------------------------------------------------
#------------------------------- JOIN GROUP ---------------------------------
            elif msg.text.lower() in ["join","kawan"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "[Command] Join"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#----------------------------------------------------------------------------
#-------------------------------- OUT GROUP ---------------------------------
            elif msg.text.lower() in ["kamu keluar"]:
                if msg.toType == 2:
                  if msg.from_ in admin:
                    print "[Command] Bye"
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------------------------------------
#------------------------------ BROADCAST PC --------------------------------
            elif "/bc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bc ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        kc.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"
#----------------------------------------------------------------------------
#----------------------------- BROADCAST Group ------------------------------
            elif "/bcgc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bcgc ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"
#----------------------------------------------------------------------------
#-------------------------------- WELCOME -----------------------------------
            if msg.text.lower() in ["wc","welcome"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
#----------------------------------------------------------------------------
#------------------------------- KICK BY TAG --------------------------------
            elif "nk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                      print "[Command] Kick"
                   except:
                      pass
#----------------------------------------------------------------------------
#------------------------------ Undang Admin Ke Grup ----------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalam grup itu")

            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       ki.sendText(msg.to,"Grup Creator Telah Diinvite")
                       print "success inv gCreator"
                    except:
                       pass

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: "," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#----------------------------------------------------------------------------
#------------------------------ Penambahan Admin ----------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                                ki.sendText(msg.to,"Selamat Kamu Admin Baru")
                                kk.sendText(msg.to,"Selamat Ya Selamat")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Lu bukan Creator")
                    cl.sendText(msg.to,"Admin/Member Tidak Bisa Menggunakan Command Add Admin")
                    ki.sendText(msg.to,"Cuma Creator Yang bisa Menggunakan")
            elif "Admrem @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                kk.sendText(msg.to,"Admin Dihapus")
                                kk.sendText(msg.to,"Kamu DiPecat Jadi Admin :(")
                                kk.sendText(msg.to,"Yang Sabar Ya Boss..")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    ki.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")
                    ki.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                    ki.sendText(msg.to,"The adminlist is empty")
                    kk.sendText(msg.to,"Tidak Ada Admin")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    ki.sendText(msg.to,"Tunggu...")
                    kk.sendText(msg.to,"Sabar Jink")
                    mc = ""
                    for mi_d in admin:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#----------------------------------------------------------------------------
#------------------------------ BAN BY TAG ----------------------------------
            elif "/ban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "/unban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#----------------------------- TAG ALL MEMBER -------------------------------
            if msg.text.lower() in ["tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#----------------------------------------------------------------------------
#------------------------------- CHECK SIDER --------------------------------
            if msg.text.lower() in ["/set"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "Ada Apaaa..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Set"

            if msg.text.lower() in ["/check"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ Read : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] Set"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik /set untuk membuat Read point.")
#----------------------------------------------------------------------------
#------------------------------- COVER BY TAG -------------------------------
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Ambilkan " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Ambilkan ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
#----------------------------------------------------------------------------
#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Sampul @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Sampul @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#----------------------------------------------------------------------------
#--------------------------------- HI / HAI ---------------------------------
            elif msg.text.lower() in ["hi","hai","hy"]:
                if msg.from_ in admin:
                    beb = "Hi Beb " + cl.getContact(msg.from_).displayName #+ " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,beb)
                else:
                    hi = "Hi " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
#----------------------------------------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#----------------------------------------------------------------------------
#--------------------------------- Remove Chat ------------------------------
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#----------------------------------------------------------------------------
#------------------------------- Kerang Ajaib -------------------------------
            elif "/apakah " in msg.text.lower():
                apk = msg.text.replace("/apakah ","")
                rnd = ['Ya','Tidak']
                p = random.choice(rnd)
                ki.sendText(msg.to,p)
                print "[Command] Kerang Ajaib"

            elif "Rate" in msg.text:
                tanya = msg.text.replace("Rate","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                ki.sendText(msg.to,jawaban)

            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                ki.sendText(msg.to,"Dosanya " + tanya + " adalah " + jawaban + " Tobat dong ")

            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                ki.sendText(msg.to,"Pahalanya " + tanya + " adalah " + jawaban + "Tingkatkan lagi  ")
#----------------------------------------------------------------------------
#---------------------------------- SONG ------------------------------------
            elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif "/lagu " in msg.text.lower():
                songname = msg.text.replace("/lagu ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])
                    print "[Command] Lagu"

            elif ".Music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])

    #-------------------Music------------------ 
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#----------------------------------------------------------------------------
#--------------------------------- Mimic --------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            		ki.sendText(msg.to,text)
            		kk.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				ki.sendText(msg.to,"Mimic on")
            				kk.sendText(msg.to,"Mimic Aktif")
            			else:
            				ki.sendText(msg.to,"Mimic already on")
            				kk.sendText(msg.to,"Mimic Sudah On")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				ki.sendText(msg.to,"Mimic off")
            				kk.sendText(msg.to,"Mimic Mati")
            			else:
            				ki.sendText(msg.to,"Mimic already off")
            				kk.sendText(msg.to,"Mimic Telah Mati")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						ki.sendText(msg.to,"Success added target")
            						kk.sendText(msg.to,"Berhasil Menambahkan Target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						ki.sendText(msg.to,"Failed")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						ki.sendText(msg.to,"Success deleted target")
            						kk.sendText(msg.to,"Berhasil Menambahkan Target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						ki.sendText(msg.to,"Failed!")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
            				ki.sendText(msg.to,"No target")
            				kk.sendText(msg.to,"Tidak Ada Target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + ki.getContact(mi_d).displayName +" | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
                                ki.sendText(msg.to,lst + "\nTotal:" + total)
#--------------------------------- INFO --------------------------------
            elif "Kepo @" in msg.text:
                nama = msg.text.replace("Kepo @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        mid = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + tob.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass

            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        mid = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + tob.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#----------------------------------------------------------------------------
            elif msg.text.lower() == 'Runtime':
                eltime = time.time() - mulai
                van = "Serk_Bot Sudah Berjalan Selama "+waktu(eltime)
                cl.sendText(msg.to,van)
                
            elif msg.text is None:
                return
#--------------------------------- INSTAGRAM --------------------------------
            elif "/ig " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig hairu.ones")


            elif '/cekig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/cekig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Nama: " + text[-2] + "\n"
                    user1 = text[-1]
                    followers = "Pengikut: " + text[0] + "\n"
                    following = "Mengikuti: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "Info Akun: " + user1 + "\n\n"
                    #details = ""
                    cl.sendText(msg.to, detail + user + followers + following + post + link)
                    cl.sendImageWithURL(msg.to, text1[0])
                    #cl.sendImage(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "/Youtube " in msg.text:
                query = msg.text.replace("/Youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'

            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#----------------------------------------------------------------------------
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])


            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')

#-----------------------------------------------
            elif "/say-id: " in msg.text.lower():
                    query = msg.text.lower().replace("/say-id: ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
#-----------------------------------------------
            elif "/say-en: " in msg.text.lower():
                    query = msg.text.lower().replace("/say-en: ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
#-----------------------------------------------
            elif "/say-jp: " in msg.text.lower():
                    query = msg.text.lower().replace("/say-jp: ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ja', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
#----------------------------------------------------------------------------
#---------------------------------------------------------------
            elif "cek" in msg.text:
            	cl.sendText(msg.to,"contoh : /cek 16-05-2004")
#---------------------------------------------------------
            elif "/cek " in msg.text:
                tanggal = msg.text.replace("/cek ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir : "+lahir+"\n\nUmur : "+usia+"\n\nUltah : "+ultah+"\n\nZodiak : "+zodiak)
#--------------------------------- ABSEN ------------------------------------
            elif msg.text.lower() in ["absen"]:
                ki.sendText(msg.to,"Siap Boy  􀜁􀅹Salute􏿿")
                kk.sendText(msg.to,"Siap Boy 􀜁􀅹Salute􏿿")
                kc.sendText(msg.to,"Siap Boy 􀜁􀅹Salute􏿿")
#----------------------------------------------------------------------------
            elif msg.text in ["/quote"]:
                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL']
                rio = random.choice(quote)
                cl.sendText(msg.to,rio)
#---------------------------------------------------------
#---------------------------------------------------------
            elif msg.text in ["/time","/waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
#---------------------------------------------------------
#---------------------------------------------------------
            elif msg.text in ["/kalender"]:
	    	    wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	            cl.sendText(msg.to, "KALENDER\n\n" + (wait2['setTime'][msg.to]))
#---------------------------------------------------------    
#------------------------------ RESPON SPEED --------------------------------
            elif msg.text.lower() in ["respon"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Respon : %s /Detik" % (elapsed_time))

            elif msg.text in ["Sp","Speed","speed"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "SpeedBot..")
					elapsed_time = time.time() - start
					ki.sendText(msg.to, "%s /Detik" % (elapsed_time))
					kk.sendText(msg.to, "%s /Detik" % (elapsed_time))
#----------------------------------------------------------------------------
#---------------------------- CEK BAN LIST ----------------------------------
            elif msg.text.lower() in ["banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "[*] " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#----------------------------------------------------------------------------
#------------------------- CEK BAN LIST ( MID ) -----------------------------
            elif msg.text.lower() in ["banlist mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
#----------------------------------------------------------------------------

#==================================================
            elif '.lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == '.reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#-------------------------------- KILL BAN ----------------------------------
            elif msg.text.lower() in ["kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        pass
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "ube187443474747c3ec352e7efeb48c1b"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				kd.kickoutFromGroup(op.param1,[op.param2])
				ke.kickoutFromGroup(op.param1,[op.param2])
				kf.kickoutFromGroup(op.param1,[op.param2])
				kg.kickoutFromGroup(op.param1,[op.param2])
				kh.kickoutFromGroup(op.param1,[op.param2])
				kj.kickoutFromGroup(op.param1,[op.param2])
				kn.kickoutFromGroup(op.param1,[op.param2])
				ko.kickoutFromGroup(op.param1,[op.param2])
				kp.kickoutFromGroup(op.param1,[op.param2])
				kq.kickoutFromGroup(op.param1,[op.param2])
				kr.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kt.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					cl.sendText
            except:
                pass
						
						
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
